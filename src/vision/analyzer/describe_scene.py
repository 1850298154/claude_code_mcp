# ============================================================================
# 文件: src/vision/analyzer/describe_scene.py
# 描述: 描述场景函数
#
# 上游依赖:
#   - vision/models/glm4v.py              (GLM4VModel)
#
# 下游封装:
#   - vision/analyzer.py                      (VisionAnalyzer.describe_scene)
#
# Bash 快速定位:
#   find . -name "describe_scene.py" -path "*/analyzer/*"
# ============================================================================

from pathlib import Path

from vision.models.glm4v import GLM4VModel


def describe_scene(model: GLM4VModel, image_path: Path | str) -> str:
    """描述图像场景

    Args:
        model: 视觉模型实例
        image_path: 图像文件路径

    Returns:
        场景描述
    """
    if isinstance(image_path, Path):
        image_path = str(image_path)

    prompt = "请详细描述这张图片的内容和场景"
    description = model.analyze_image(image_path, prompt)
    return description
