#!/usr/bin/env python
# 使用FastMCP的streamable-http client测试

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
import asyncio


async def test_speak():
    """测试speak工具"""
    # 使用streamable-http连接
    async with streamable_http_client("http://127.0.0.1:8000/mcp") as (read, write, get_session_id):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 测试speak工具
            print("--- 第一次调用 ---")
            result1 = await session.call_tool("speak", {"text": "第一次语音测试", "async_mode": False})
            print("结果:", result1)

            # 等待一下
            await asyncio.sleep(3)

            # 第二次调用
            print("\n--- 第二次调用 ---")
            result2 = await session.call_tool("speak", {"text": "第二次语音测试", "async_mode": False})
            print("结果:", result2)

            print("\n测试完成")


if __name__ == "__main__":
    asyncio.run(test_speak())
