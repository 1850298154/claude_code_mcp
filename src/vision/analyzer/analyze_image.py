# ============================================================================
# 文件: src/vision/analyzer/analyze_image.py
# 描述: 分析图像函数
#
# 上游依赖:
#   - vision/types.py                        (ImageAnalysis)
#   - vision/models/glm4v.py              (GLM4VModel)
#
# 下游封装:
#   - vision/analyzer.py                      (VisionAnalyzer.analyze_image)
#
# Bash 快速定位:
#   find . -name "analyze_image.py" -path "*/analyzer/*"
# ============================================================================

from pathlib import Path

from vision.types import ImageAnalysis
from vision.models.glm4v import GLM4VModel


def analyze_image(
    model: GLM4VModel, image_path: Path | str, prompt: str = ""
) -> ImageAnalysis:
    """分析图像

    Args:
        model: 视觉模型实例
        image_path: 图像文件路径
        prompt: 分析提示词

    Returns:
        图像分析结果
    """
    if isinstance(image_path, Path):
        image_path = str(image_path)

    description = model.analyze_image(image_path, prompt)
    return ImageAnalysis(description=description)
