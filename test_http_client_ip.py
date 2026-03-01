import json
import urllib.request
import socket

socket.setdefaulttimeout(10)

# 使用IP地址格式连接 - 请根据实际情况修改
# 示例: http://192.168.1.100:9001/mcp 或 http://192.168.1.100:8080/mcp
MCP_URL = "http://127.0.0.1:9001/mcp"


def mcp_request(url: str, session_id: str = None, method: str = None, params: dict = None):
    """发送MCP请求"""
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }
    if session_id:
        headers["mcp-session-id"] = session_id

    data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
    }
    if params:
        data["params"] = params

    req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
    resp = urllib.request.urlopen(req)

    new_session_id = resp.getheader("mcp-session-id") or session_id
    response_text = resp.read().decode("utf-8")

    # 解析SSE响应
    if "event: message" in response_text:
        # 提取data内容
        for line in response_text.split("\n"):
            if line.startswith("data: "):
                try:
                    return json.loads(line[6:]), new_session_id
                except:
                    pass

    return response_text, new_session_id


def test_connection():
    """测试连接"""
    print("=== HTTP MCP Client Test (IP Format) ===")
    print(f"Server: {MCP_URL}")
    print()

    # 1. 初始化连接
    print("1. 初始化连接...")
    init_result, session_id = mcp_request(
        MCP_URL,
        method="initialize",
        params={
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "test-client", "version": "1.0"}
        }
    )
    print(f"   Session ID: {session_id}")
    print(f"   Protocol: {init_result.get('result', {}).get('protocolVersion', 'N/A')}")
    print()

    # 2. 列出工具
    print("2. 列出可用工具...")
    tools_result, session_id = mcp_request(MCP_URL, session_id, method="tools/list")
    tools = tools_result.get("result", {}).get("tools", [])
    print(f"   找到 {len(tools)} 个工具:")
    for tool in tools[:5]:  # 只显示前5个
        print(f"   - {tool.get('name')}: {tool.get('description', '')[:50]}...")
    print()

    # 3. 调用speak工具
    print("3. 调用speak工具 (异步)...")
    speak_result, session_id = mcp_request(
        MCP_URL,
        session_id,
        method="tools/call",
        params={
            "name": "speak",
            "arguments": {"text": "Hello from HTTP client via IP address", "async_mode": True}
        }
    )
    content = speak_result.get("result", {}).get("content", [])
    if content and content[0].get("type") == "text":
        result_text = content[0].get("text", "")
        print(f"   结果: {result_text}")
    print()

    print("=== 测试完成 ===")


if __name__ == "__main__":
    test_connection()
