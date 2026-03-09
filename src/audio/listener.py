# ============================================================================
# 文件: src/audio/listener.py
# 描述: Listener 类定义，用于语音转文字
# ============================================================================

"""Listener - 语音识别

将语音转换为文字。
"""

from typing import Optional, Callable
import threading
from dataclasses import dataclass
from .types import RecognizerBackend, ListenerState

try:
    import speech_recognition as sr
    HAS_SR = True
except ImportError:
    HAS_SR = False

try:
    from pynput import keyboard
    HAS_PYNPUT = True
except ImportError:
    HAS_PYNPUT = False


@dataclass
class RecognitionResult:
    """识别结果

    Attributes:
        success: 是否识别成功
        text: 识别的文本
        error: 错误信息
    """
    success: bool
    text: str = ""
    error: str = ""


class Listener:
    """Listener - 语音识别类

    提供语音转文字(STT)功能，支持按键触发录音和识别。
    """

    def __init__(
        self,
        backend: RecognizerBackend = RecognizerBackend.SPHINX,
        trigger_key: str = "f12",
    ):
        """初始化 Listener

        Args:
            backend: 识别后端 (默认: sphinx 本地离线)
            trigger_key: 触发录音的按键 (默认: f12)
        """
        self._backend = backend
        self._trigger_key = trigger_key
        self._state = ListenerState.IDLE
        self._recognizer = None
        self._keyboard_listener = None
        self._on_result: Optional[Callable[[RecognitionResult], None]] = None
        self._listening = False
        self._lock = threading.Lock()

        if HAS_SR:
            self._recognizer = sr.Recognizer()

    @property
    def state(self) -> ListenerState:
        """获取当前状态"""
        return self._state

    @property
    def is_available(self) -> bool:
        """检查语音识别是否可用"""
        return HAS_SR and self._recognizer is not None

    def listen_once(
        self,
        timeout: Optional[float] = None,
        phrase_time_limit: Optional[float] = None,
    ) -> RecognitionResult:
        """单次录音并识别（同步）

        Args:
            timeout: 等待语音开始的超时时间（秒）
            phrase_time_limit: 单次录音的最长时间（秒）

        Returns:
            RecognitionResult: 识别结果
        """
        if not self.is_available:
            return RecognitionResult(
                success=False,
                error="语音识别模块未安装，请运行: uv add SpeechRecognition pocketsphinx"
            )

        with self._lock:
            self._state = ListenerState.LISTENING

            try:
                with sr.Microphone() as source:
                    # 自动调整环境噪音
                    self._recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = self._recognizer.listen(
                        source,
                        timeout=timeout,
                        phrase_time_limit=phrase_time_limit
                    )
            except sr.WaitTimeoutError:
                self._state = ListenerState.IDLE
                return RecognitionResult(
                    success=False,
                    error="等待语音超时"
                )
            except Exception as e:
                self._state = ListenerState.IDLE
                return RecognitionResult(
                    success=False,
                    error=f"录音失败: {e}"
                )

        # 识别
        self._state = ListenerState.PROCESSING
        result = self._recognize(audio)
        self._state = ListenerState.IDLE
        return result

    def _recognize(self, audio) -> RecognitionResult:
        """识别音频

        Args:
            audio: 音频数据

        Returns:
            RecognitionResult: 识别结果
        """
        try:
            if self._backend == RecognizerBackend.SPHINX:
                text = self._recognizer.recognize_sphinx(audio)
            elif self._backend == RecognizerBackend.GOOGLE:
                text = self._recognizer.recognize_google(audio, language="zh-CN")
            else:
                return RecognitionResult(
                    success=False,
                    error=f"不支持的识别后端: {self._backend}"
                )

            return RecognitionResult(success=True, text=text)

        except sr.UnknownValueError:
            return RecognitionResult(
                success=False,
                error="无法识别语音内容"
            )
        except sr.RequestError as e:
            return RecognitionResult(
                success=False,
                error=f"识别服务错误: {e}"
            )
        except Exception as e:
            return RecognitionResult(
                success=False,
                error=f"识别失败: {e}"
            )

    def start_key_listener(
        self,
        on_result: Optional[Callable[[RecognitionResult], None]] = None,
    ) -> bool:
        """启动按键监听器（按住触发键录音，松开识别）

        Args:
            on_result: 识别结果回调函数

        Returns:
            是否启动成功
        """
        if not HAS_PYNPUT:
            print("pynput 模块未安装，请运行: uv add pynput", flush=True)
            return False

        if not self.is_available:
            print("语音识别模块未安装", flush=True)
            return False

        self._on_result = on_result

        # 获取触发键
        trigger_key = getattr(keyboard.Key, self._trigger_key, keyboard.Key.f12)

        def on_press(key):
            if key == trigger_key and not self._listening:
                self._listening = True
                self._state = ListenerState.LISTENING
                print("开始录音...", flush=True)
                threading.Thread(target=self._record_audio, daemon=True).start()

        def on_release(key):
            if key == trigger_key and self._listening:
                self._listening = False
                print("停止录音，识别中...", flush=True)

        self._keyboard_listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release
        )
        self._keyboard_listener.start()
        print(f"按 {self._trigger_key.upper()} 开始录音，松开停止，按 ESC 退出", flush=True)
        return True

    def _record_audio(self):
        """录音线程"""
        try:
            with sr.Microphone() as source:
                self._recognizer.adjust_for_ambient_noise(source, duration=0.3)
                audio = self._recognizer.listen(source, phrase_time_limit=None)

            # 识别
            self._state = ListenerState.PROCESSING
            result = self._recognize(audio)

            if self._on_result:
                self._on_result(result)
            else:
                if result.success:
                    print(f"识别结果: {result.text}", flush=True)
                else:
                    print(f"识别失败: {result.error}", flush=True)

        except Exception as e:
            print(f"录音/识别错误: {e}", flush=True)
        finally:
            self._state = ListenerState.IDLE

    def stop_key_listener(self):
        """停止按键监听器"""
        if self._keyboard_listener:
            self._keyboard_listener.stop()
            self._keyboard_listener = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_key_listener()
        return False


__all__ = ["Listener", "RecognitionResult"]
