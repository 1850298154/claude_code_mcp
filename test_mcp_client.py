#!/usr/bin/env python
"""
MCP WebSocket 测试客户端
用于测试 MCP WebSocket 服务器连接和工具列表
"""

import asyncio
import json
import websockets
from typing import Any, Dict


class MCPClient:
    """MCP WebSocket 客户端"""

    def __init__(self, uri: str = "ws://127.0.0.1:8765"):
        self.uri = uri
        self.websocket = None

    async def connect(self) -> bool:
        """连接到 MCP 服务器"""
        try:
            print(f"[*] 连接到 {self.uri} ...")
            self.websocket = await websockets.connect(self.uri)
            print("[+] 连接成功!")
            return True
        except Exception as e:
            print(f"[-] 连接失败: {e}")
            return False

    async def disconnect(self):
        """断开连接"""
        if self.websocket:
            await self.websocket.close()
            print("[*] 已断开连接")

    async def send_request(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """发送请求到 MCP 服务器"""
        if not self.websocket:
            return {"error": "未连接到服务器"}

        request_id = 1
        request = {
            "jsonrpc": "2.0",
            "id": request_id,
            "method": method,
        }
        if params:
            request["params"] = params

        message = json.dumps(request)
        print(f"[→] 发送: {method}")

        try:
            await self.websocket.send(message)
            response = await self.websocket.recv()
            result = json.loads(response)
            print(f"[←] 收到响应")
            return result
        except Exception as e:
            print(f"[-] 请求失败: {e}")
            return {"error": str(e)}

    async def initialize(self) -> Dict[str, Any]:
        """初始化连接"""
        return await self.send_request("initialize", {})

    async def list_tools(self) -> Dict[str, Any]:
        """列出所有可用工具"""
        return await self.send_request("tools/list")

    async def call_tool(self, tool_name: str, arguments: Dict[str, Any] = None) -> Dict[str, Any]:
        """调用工具"""
        params = {"name": tool_name}
        if arguments:
            params["arguments"] = arguments
        return await self.send_request("tools/call", params)


async def main():
    """主函数"""
    client = MCPClient()

    try:
        # 连接服务器
        if not await client.connect():
            return

        print("\n" + "=" * 60)
        print("1. 测试初始化")
        print("=" * 60)
        init_result = await client.initialize()
        print(json.dumps(init_result, indent=2, ensure_ascii=False))

        print("\n" + "=" * 60)
        print("2. 列出所有工具")
        print("=" * 60)
        tools_result = await client.list_tools()

        if "result" in tools_result and "tools" in tools_result["result"]:
            tools = tools_result["result"]["tools"]
            print(f"\n找到 {len(tools)} 个工具:\n")
            for i, tool in enumerate(tools, 1):
                print(f"{i}. {tool['name']}")
                if tool.get('description'):
                    desc = tool['description'][:80] + "..." if len(tool['description']) > 80 else tool['description']
                    print(f"   描述: {desc}")
                print()
        else:
            print("获取工具列表失败:")
            print(json.dumps(tools_result, indent=2, ensure_ascii=False))

        print("=" * 60)

        # 可选：测试调用一个工具
        print("\n" + "=" * 60)
        print("3. 测试调用工具 (speak)")
        print("=" * 60)
        speak_result = await client.call_tool("speak", {"text": "Hello from MCP client", "async": True})
        print(json.dumps(speak_result, indent=2, ensure_ascii=False))

    finally:
        await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
