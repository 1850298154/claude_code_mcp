# ============================================================================
# 文件: src/vision/__main__.py
# 描述: Vision 模块主入口
#
# Bash 快速定位:
#   find src -name "__main__.py" -path "*/vision/*"
# ============================================================================

"""Vision 模块主入口"""

from vision.analyzer import VisionAnalyzer
from vision.types import ModelType, ModelConfig


def main():
    """主函数"""
    print("Vision Module - Example Usage")
    print("=" * 50)
    print("\nInitialize VisionAnalyzer with API key:")
    print("  analyzer = VisionAnalyzer(ModelConfig(model_type=ModelType.GLM4V, api_key='...'))")
    print("\nAvailable methods:")
    print("  - analyze_image(image_path, prompt)")
    print("  - detect_objects(image_path)")
    print("  - extract_text(image_path)")
    print("  - describe_scene(image_path)")
    print("  - compare_images(image1_path, image2_path)")


if __name__ == "__main__":
    main()
