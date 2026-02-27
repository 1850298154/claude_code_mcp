# ============================================================================
# 文件: src/mcp/tools/vision_tools.py
# 描述: Vision MCP 工具定义
#
# 上游依赖: vision/analyzer/
# 下游封装: mcp/server.py
#
# Bash 快速定位:
#   find src -name "vision_tools.py" -path "*/mcp/tools/*"
# ============================================================================

"""Vision MCP 工具"""

from mcp.types import Tool


VISION_TOOLS: list[Tool] = [
    Tool(
        name="analyze_image",
        description="分析图像内容",
        inputSchema={
            "type": "object",
            "properties": {
                "image_path": {
                    "type": "string",
                    "description": "图像文件路径",
                },
                "prompt": {
                    "type": "string",
                    "description": "分析提示词",
                },
            },
            "required": ["image_path", "prompt"],
        },
    ),
    Tool(
        name="detect_objects",
        description="检测图像中的对象",
        inputSchema={
            "type": "object",
            "properties": {
                "image_path": {
                    "type": "string",
                    "description": "图像文件路径",
                },
            },
            "required": ["image_path"],
        },
    ),
    Tool(
        name="extract_text",
        description="提取图像中的文本（OCR）",
        inputSchema={
            "type": "object",
            "properties": {
                "image_path": {
                    "type": "string",
                    "description": "图像文件路径",
                },
            },
            "required": ["image_path"],
        },
    ),
    Tool(
        name="describe_scene",
        description="描述图像场景",
        inputSchema={
            "type": "object",
            "properties": {
                "image_path": {
                    "type": "string",
                    "description": "图像文件路径",
                },
            },
            "required": ["image_path"],
        },
    ),
    Tool(
        name="compare_images",
        description="比较两幅图像",
        inputSchema={
            "type": "object",
            "properties": {
                "image1_path": {
                    "type": "string",
                    "description": "第一幅图像路径",
                },
                "image2_path": {
                    "type": "string",
                    "description": "第二幅图像路径",
                },
            },
            "required": ["image1_path", "image2_path"],
        },
    ),
]


__all__ = ["VISION_TOOLS"]
