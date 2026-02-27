# ============================================================================
# 文件: examples/vision_usage.py
# 描述: Vision 使用示例
#
# Bash 快速定位:
#   find . -name "vision_usage.py"
# ============================================================================

"""
Vision 模块使用示例

演示如何使用 VisionAnalyzer 进行图像分析。
"""

from vision.analyzer import VisionAnalyzer
from vision.types import ModelType, ModelConfig


def main():
    """主函数"""
    print("Vision Module Usage Example")
    print("=" * 50)

    # 初始化 VisionAnalyzer（无 API key，仅演示）
    config = ModelConfig(
        model_type=ModelType.GLM4V,
        api_key=None
    )
    analyzer = VisionAnalyzer(config)

    # 分析图像
    print("\n1. 分析图像")
    print("   analyzer.analyze_image('image.jpg', 'What is in this image?')")
    print("   返回: 图像的详细描述")

    # 检测对象
    print("\n2. 检测对象")
    print("   objects = analyzer.detect_objects('image.jpg')")
    print("   返回: 检测到的对象列表")

    # 提取文本
    print("\n3. 提取文本 (OCR)")
    print("   text = analyzer.extract_text('image.jpg')")
    print("   返回: 图像中的文本内容")

    # 描述场景
    print("\n4. 描述场景")
    print("   description = analyzer.describe_scene('image.jpg')")
    print("   返回: 场景的详细描述")

    # 比较图像
    print("\n5. 比较图像")
    print("   result = analyzer.compare_images('image1.jpg', 'image2.jpg')")
    print("   返回: 两幅图像的比较结果")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
