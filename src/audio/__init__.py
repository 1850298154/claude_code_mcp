# ============================================================================
# 文件: src/audio/__init__.py
# 描述: 音频模块初始化
# ============================================================================

"""音频模块

提供文本转语音(TTS)、语音转文字(STT)和音频播放功能。
"""

from .speaker import Speaker
from .listener import Listener, RecognitionResult
from .types import VoiceType, VoiceSpeed, AudioConfig, RecognizerBackend, ListenerState

__all__ = [
    "Speaker",
    "Listener",
    "RecognitionResult",
    "VoiceType",
    "VoiceSpeed",
    "AudioConfig",
    "RecognizerBackend",
    "ListenerState",
]
