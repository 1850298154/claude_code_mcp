# ============================================================================
# 文件: src/audio/speaker.py
# 描述: Speaker 类定义，用于文本转语音和播放
# ============================================================================

"""Speaker - 语音播报

将文本转换为语音并播放。
"""

from typing import Optional
import threading
from .types import AudioConfig

try:
    import pyttsx3
    HAS_PYTTSX3 = True
except ImportError:
    HAS_PYTTSX3 = False


class Speaker:
    """Speaker - 语音播报类

    提供文本转语音(TTS)和音频播放功能。
    """

    def __init__(self, config: Optional[AudioConfig] = None):
        """初始化 Speaker

        Args:
            config: 音频配置，默认使用默认配置
        """
        self._config = config or AudioConfig()
        self._engine = None
        self._init_engine()

    def _init_engine(self):
        """初始化语音引擎"""
        if HAS_PYTTSX3:
            try:
                self._engine = pyttsx3.init()
            except Exception as e:
                print(f"初始化语音引擎失败: {e}", flush=True)
                self._engine = None

    def speak(self, text: str) -> bool:
        """播放语音（同步）

        Args:
            text: 要播放的文本

        Returns:
            是否播放成功
        """
        if not self._engine:
            print("语音引擎未初始化，无法播放", flush=True)
            return False

        try:
            self._engine.say(text)
            self._engine.runAndWait()
            return True
        except Exception as e:
            print(f"播放失败: {e}", flush=True)
            return False

    def speak_async(self, text: str) -> bool:
        """异步播放语音

        Args:
            text: 要播放的文本

        Returns:
            是否开始播放
        """
        if not self._engine:
            print("语音引擎未初始化，无法播放", flush=True)
            return False

        try:
            # 在新线程中运行同步播放
            thread = threading.Thread(target=self._run_in_thread, args=(text,))
            thread.daemon = True
            thread.start()
            return True
        except Exception as e:
            print(f"异步播放失败: {e}", flush=True)
            return False

    def _run_in_thread(self, text: str):
        """在线程中运行语音播放"""
        try:
            self._engine.say(text)
            self._engine.runAndWait()
        except Exception as e:
            print(f"线程播放失败: {e}", flush=True)


__all__ = ["Speaker"]
