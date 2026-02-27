# ============================================================================
# 文件: src/vision/analyzer/detect_objects.py
# 描述: 检测对象函数
#
# 上游依赖:
#   - vision/types.py                        (DetectedObject)
#   - vision/models/glm4v.py              (GLM4VModel)
#
# 下游封装:
#   - vision/analyzer.py                      (VisionAnalyzer.detect_objects)
#
# Bash 快速定位:
#   find . -name "detect_objects.py" -path "*/analyzer/*"
# ============================================================================

from pathlib import Path
from typing import List

from vision.types import DetectedObject
from vision.models.glm4v import GLM4VModel


def detect_objects(model: GLM4VModel, image_path: Path | str) -> List[DetectedObject]:
    """检测图像中的对象

    Args:
        model: 视觉模型实例
        image_path: 图像文件路径

    Returns:
        检测到的对象列表
    """
    if isinstance(image_path, Path):
        image_path = str(image_path)

    objects_data = model.detect_objects(image_path)
    objects = []

    for obj_data in objects_data:
        obj = DetectedObject(
            label=obj_data.get("label", ""),
            confidence=obj_data.get("confidence", 0.0),
            bbox=tuple(obj_data.get("bbox", [0, 0, 0, 0])),
        )
        objects.append(obj)

    return objects
