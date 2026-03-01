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
        self._play_lock = threading.Lock()  # 播放锁，防止并发调用

    def _get_engine(self):
        """获取或创建语音引擎（每次调用重新创建以确保可重用）"""
        if not HAS_PYTTSX3:
            return None
        try:
            return pyttsx3.init()
        except Exception as e:
            print(f"初始化语音引擎失败: {e}", flush=True)
            return None

    def speak(self, text: str) -> bool:
        """播放语音（同步）

        Args:
            text: 要播放的文本

        Returns:
            是否播放成功
        """
        engine = self._get_engine()
        if not engine:
            print("语音引擎未初始化，无法播放", flush=True)
            return False

        try:
            with self._play_lock:  # 使用锁保护
                engine.say(text)
                engine.runAndWait()
                engine.stop()  # 确保引擎停止
                del engine  # 释放引擎资源
            return True
        except Exception as e:
            print(f"播放失败: {e}", flush=True)
            return False

    def speak_async(self, text: str) -> bool:
        """异步播放语音（带锁保护，防止并发冲突）

        Args:
            text: 要播放的文本

        Returns:
            是否开始播放
        """
        engine = self._get_engine()
        if not engine:
            print("语音引擎未初始化，无法播放", flush=True)
            return False

        try:
            # 在新线程中运行同步播放（使用锁保护）
            thread = threading.Thread(target=self._run_in_thread, args=(text, engine))
            thread.daemon = False  # 非守护线程，确保播放完成
            thread.start()
            return True
        except Exception as e:
            print(f"异步播放失败: {e}", flush=True)
            return False

    def _run_in_thread(self, text: str, engine):
        """在线程中运行语音播放"""
        try:
            with self._play_lock:  # 使用锁保护 runAndWait 调用
                engine.say(text)
                engine.runAndWait()
                engine.stop()  # 确保引擎停止
                del engine  # 释放引擎资源
        except Exception as e:
            print(f"线程播放失败: {e}", flush=True)


__all__ = ["Speaker"]
