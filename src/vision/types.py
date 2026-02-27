# ============================================================================
# 文件: src/vision/types.py
# 描述: Vision 模块类型定义
#
# 上游依赖: 无
# 下游封装: analyzer.py, models/*
#
# Bash 快速定位:
#   find . -name "types.py" -path "*/vision/*"
# ============================================================================

from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from pathlib import Path
from enum import Enum


class ModelType(Enum):
    """支持的视觉模型类型"""

    GLM4V = "glm4v"
    GPT4V = "gpt4v"


@dataclass
class DetectedObject:
    """检测到的对象数据结构

    Attributes:
        label: 对象标签
        confidence: 置信度 (0-1)
        bbox: 边界框 (x1, y1, x2, y2)
    """

    label: str
    confidence: float
    bbox: tuple[int, int, int, int]


@dataclass
class ImageAnalysis:
    """图像分析结果

    Attributes:
        description: 图像描述
        objects: 检测到的对象列表
        text: 提取的文本
        metadata: 额外元数据
    """

    description: str
    objects: Optional[List[DetectedObject]] = None
    text: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


@dataclass
class ModelConfig:
    """模型配置

    Attributes:
        api_key: API 密钥
        api_url: API 端点
        max_tokens: 最大 token 数
    """

    api_key: Optional[str] = None
    api_url: Optional[str] = None
    max_tokens: Optional[int] = None
