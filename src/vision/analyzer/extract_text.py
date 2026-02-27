# ============================================================================
# 文件: src/vision/analyzer/extract_text.py
# 描述: 提取文本函数
#
# 上游依赖:
#   - vision/models/glm4v.py              (GLM4VModel)
#
# 下游封装:
#   - vision/analyzer.py                      (VisionAnalyzer.extract_text)
#
# Bash 快速定位:
#   find . -name "extract_text.py" -path "*/analyzer/*"
# ============================================================================

from pathlib import Path

from vision.models.glm4v import GLM4VModel


def extract_text(model: GLM4VModel, image_path: Path | str) -> str:
    """提取图像中的文本（OCR）

    Args:
        model: 视觉模型实例
        image_path: 图像文件路径

    Returns:
        提取的文本
    """
    if isinstance(image_path, Path):
        image_path = str(image_path)

    return model.extract_text(image_path)
