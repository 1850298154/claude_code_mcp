# ============================================================================
# 文件: src/vision/analyzer/compare_images.py
# 描述: 比较图像函数
#
# 上游依赖:
#   - vision/types.py                        (ImageAnalysis)
#   - vision/models/glm4v.py              (GLM4VModel)
#
# 下游封装:
#   - vision/analyzer.py                      (VisionAnalyzer.compare_images)
#
# Bash 快速定位:
#   find . -name "compare_images.py" -path "*/analyzer/*"
# ============================================================================

from pathlib import Path

from vision.models.glm4v import GLM4VModel


def compare_images(
    model: GLM4VModel, image1_path: Path | str, image2_path: Path | str
) -> dict:
    """比较两张图像

    Args:
        model: 视觉模型实例
        image1_path: 第一张图像路径
        image2_path: 第二张图像路径

    Returns:
        比较结果（相似度、差异等）
    """
    if isinstance(image1_path, Path):
        image1_path = str(image1_path)
    if isinstance(image2_path, Path):
        image2_path = str(image2_path)

    prompt = "请详细描述这张图片的内容和场景"
    desc1 = model.analyze_image(image1_path, prompt)
    desc2 = model.analyze_image(image2_path, prompt)

    return {
        "image1_description": desc1,
        "image2_description": desc2,
        "similarity": 1.0 if desc1 == desc2 else 0.0,
    }
