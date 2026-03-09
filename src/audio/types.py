# ============================================================================
# 文件: src/audio/types.py
# 描述: 音频模块类型定义
# ============================================================================

"""音频模块类型定义"""

from typing import Optional
from enum import Enum


class VoiceType(str, Enum):
    """语音类型"""

    DEFAULT = "default"
    MALE = "male"
    FEMALE = "female"
    CHILD = "child"
    ELDERLY = "elderly"


class VoiceSpeed(str, Enum):
    """语音速度"""

    SLOW = "slow"
    NORMAL = "normal"
    FAST = "fast"


class AudioConfig:
    """音频配置

    Attributes:
        voice_type: 语音类型
        speed: 语音速度
        volume: 音量 (0-100)
    """

    def __init__(
        self,
        voice_type: VoiceType = VoiceType.DEFAULT,
        speed: VoiceSpeed = VoiceSpeed.NORMAL,
        volume: int = 80,
    ):
        self.voice_type = voice_type
        self.speed = speed
        self.volume = max(0, min(100, volume))


class RecognizerBackend(str, Enum):
    """语音识别后端"""

    SPHINX = "sphinx"  # 本地离线识别 (pocketsphinx)
    GOOGLE = "google"  # Google Web Speech API


class ListenerState(str, Enum):
    """监听器状态"""

    IDLE = "idle"  # 空闲
    LISTENING = "listening"  # 正在录音
    PROCESSING = "processing"  # 正在识别


__all__ = [
    "VoiceType",
    "VoiceSpeed",
    "AudioConfig",
    "RecognizerBackend",
    "ListenerState",
]
