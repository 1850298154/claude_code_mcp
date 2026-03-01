import json
import urllib.request
import socket

socket.setdefaulttimeout(10)  # 全局超时10秒

# 服务器配置 - 可以使用IP地址格式，如 http://192.168.1.100:9001/mcp
MCP_URL = "http://127.0.0.1:9001/mcp"  # 默认使用localhost，可改为IP地址

def test_list_tools() -> str:
    print("=== 1. List Tools ===")
    # 先发送初始化请求
    init_body = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "test-client", "version": "1.0"}
        }
    })
    req = urllib.request.Request(MCP_URL, data=init_body.encode("utf-8"), headers={
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    })
    try:
        init_resp = urllib.request.urlopen(req)
        print("Init Status:", init_resp.status)
        session_id = init_resp.getheader("mcp-session-id")
        print("Session ID:", session_id)
        init_text = init_resp.read().decode("utf-8")
        print("Init Response:", init_text[:200])
    except Exception as e:
        print("Init Error:", e)
        return None

    # 然后发送 tools/list 请求，携带 session ID
    body = json.dumps({
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list",
    })
    req = urllib.request.Request(MCP_URL, data=body.encode("utf-8"), headers={
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "mcp-session-id": session_id or "",
    })
    try:
        tools_resp = urllib.request.urlopen(req)
        print("Status:", tools_resp.status)
        text = tools_resp.read().decode("utf-8")
        print("Response text:", text[:500])
    except Exception as e:
        print("Error:", e)

    return session_id

def test_speak_async(session_id: str):
    print()
    print("=== 2. Call speak (async) ===")
    body = json.dumps({
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {
            "name": "speak",
            "arguments": {"text": "Hello from HTTP client", "async_mode": True}
        }
    })
    req = urllib.request.Request(MCP_URL, data=body.encode("utf-8"), headers={
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "mcp-session-id": session_id,
    })
    try:
        speak_resp = urllib.request.urlopen(req)
        print("Status:", speak_resp.status)
        text = speak_resp.read().decode("utf-8")
        print("Response text:", text[:500])
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("=== HTTP MCP Client Test ===")
    print(f"Server: {MCP_URL}")
    print()
    session_id = test_list_tools()
    print()
    if session_id:
        test_speak_async(session_id)
    print()
    print("=== Test Complete ===")
