#!/usr/bin/env python
"""
MCP HTTP 测试客户端
用于测试 MCP HTTP 服务器连接和工具列表
"""

import json
from typing import Dict, Any


class MCPHTTPClient:
    """MCP HTTP 客户端"""

    def __init__(self, base_url: str = "http://127.0.0.1:8000"):
        self.base_url = base_url
        self.mcp_url = f"{base_url}/mcp"
        self.health_url = f"{base_url}/health"

    def _post(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """发送 POST 请求到 MCP 服务器

        Args:
            method: MCP 方法名
            params: 请求参数

        Returns:
            响应数据
        """
        import urllib.request
        import urllib.error

        request_id = 1
        request_data = {
            "jsonrpc": "2.0",
            "id": request_id,
            "method": method,
        }
        if params:
            request_data["params"] = params

        print(f"[→] 发送: {method}")

        try:
            req = urllib.request.Request(
                self.mcp_url,
                data=json.dumps(request_data).encode("utf-8"),
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=30) as response:
                result = json.loads(response.read().decode("utf-8"))
                print(f"[←] 收到响应")
                return result
        except urllib.error.URLError as e:
            print(f"[-] 连接失败: {e}")
            return {"error": str(e)}
        except Exception as e:
            print(f"[-] 请求失败: {e}")
            return {"error": str(e)}

    def _get(self, url: str) -> Dict[str, Any]:
        """发送 GET 请求

        Args:
            url: 请求 URL

        Returns:
            响应数据
        """
        import urllib.request

        try:
            with urllib.request.urlopen(url, timeout=10) as response:
                return json.loads(response.read().decode("utf-8"))
        except Exception as e:
            return {"error": str(e)}

    def health_check(self) -> Dict[str, Any]:
        """健康检查"""
        print("[*] 健康检查...")
        result = self._get(self.health_url)
        print(f"[*] 结果: {result}")
        return result

    def initialize(self) -> Dict[str, Any]:
        """初始化连接"""
        return self._post("initialize", {})

    def list_tools(self) -> Dict[str, Any]:
        """列出所有可用工具"""
        return self._post("tools/list")

    def call_tool(self, tool_name: str, arguments: Dict[str, Any] = None) -> Dict[str, Any]:
        """调用工具"""
        params = {"name": tool_name}
        if arguments:
            params["arguments"] = arguments
        return self._post("tools/call", params)


def main():
    """主函数"""
    client = MCPHTTPClient()

    print("=" * 60)
    print("MCP HTTP Client Test")
    print("=" * 60)
    print(f"Server: {client.base_url}")
    print()

    # 健康检查
    print("=" * 60)
    print("1. 健康检查")
    print("=" * 60)
    health_result = client.health_check()
    print(json.dumps(health_result, indent=2, ensure_ascii=False))
    print()

    # 初始化
    print("=" * 60)
    print("2. 测试初始化")
    print("=" * 60)
    init_result = client.initialize()
    print(json.dumps(init_result, indent=2, ensure_ascii=False))
    print()

    # 列出工具
    print("=" * 60)
    print("3. 列出所有工具")
    print("=" * 60)
    tools_result = client.list_tools()

    if "result" in tools_result and "tools" in tools_result["result"]:
        tools = tools_result["result"]["tools"]
        print(f"\n找到 {len(tools)} 个工具:\n")
        for i, tool in enumerate(tools, 1):
            print(f"{i}. {tool['name']}")
            if tool.get('description'):
                desc = tool['description'][:60] + "..." if len(tool['description']) > 60 else tool['description']
                print(f"   描述: {desc}")
            print()
    else:
        print("获取工具列表失败:")
        print(json.dumps(tools_result, indent=2, ensure_ascii=False))

    # 调用工具测试
    print("=" * 60)
    print("4. 测试调用工具 (speak)")
    print("=" * 60)
    speak_result = client.call_tool("speak", {"text": "Hello from HTTP client", "async": True})
    print(json.dumps(speak_result, indent=2, ensure_ascii=False))

    print("\n" + "=" * 60)
    print("测试完成!")
    print("=" * 60)


if __name__ == "__main__":
    main()
