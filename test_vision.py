#!/usr/bin/env python
# 测试Vision工具 - 使用FastMCP streamable-http client

import asyncio
from pathlib import Path
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


# 测试图片目录
IMAGE_DIR = r"D:\zyt\git_ln\path_agent\ob_2d\004\2026-03-01_21-20-06\savefig"


async def test_vision():
    """测试Vision工具"""
    # 获取所有jpg图片
    image_paths = sorted([str(p) for p in Path(IMAGE_DIR).glob("*.jpg")])
    print(f"找到 {len(image_paths)} 张图片")
    for i, p in enumerate(image_paths[:5], 1):
        print(f"  {i}. {Path(p).name}")

    async with streamable_http_client("http://127.0.0.1:8000/mcp") as (read, write, get_session_id):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 测试1: 单图分析
            print("\n=== 测试1: 单图分析 ===")
            result = await session.call_tool("analyze_image", {
                "image_paths": [image_paths[0]],
                "prompt": "请详细描述这张图片的内容"
            })
            print("结果:", result)

            # 测试2: 多图对比
            print("\n=== 测试2: 多图对比（前3张） ===")
            result = await session.call_tool("analyze_image", {
                "image_paths": image_paths[:3],
                "prompt": "请比较这3张图片的异同"
            })
            print("结果:", result)

            # 测试3: OCR提取文字
            print("\n=== 测试3: OCR提取文字 ===")
            result = await session.call_tool("analyze_image", {
                "image_paths": [image_paths[0]],
                "prompt": "请提取图片中的所有文字内容"
            })
            print("结果:", result)


if __name__ == "__main__":
    asyncio.run(test_vision())
