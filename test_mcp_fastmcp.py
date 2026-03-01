#!/usr/bin/env python
"""
MCP FastMCP 服务器测试客户端

测试使用官方 FastMCP 实现的 MCP 服务器。
"""

import json
import requests
import sys
import io

# Fix UTF-8 encoding on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

MCP_URL = "http://0.0.0.0:8000/mcp"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream",
}


def _parse_sse(text: str) -> dict:
    """解析 SSE (Server-Sent Events) 格式响应"""
    for line in text.split('\n'):
        line = line.strip()
        if line.startswith('data:'):
            data_content = line[5:].strip()
            if data_content:
                return json.loads(data_content)
    return {}


def main():
    print("=" * 60)
    print("MCP FastMCP Server Test")
    print("=" * 60)
    print(f"Server: {MCP_URL}")
    print()

    # 1. Initialize and get session ID
    print("=" * 60)
    print("1. Initialize")
    print("=" * 60)
    init_resp = requests.post(
        MCP_URL,
        json={
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "test_client", "version": "1.0"}
            }
        },
        headers=headers,
        timeout=10
    )
    print(f"Status: {init_resp.status_code}")

    # Extract session ID from response header
    session_id = init_resp.headers.get("Mcp-Session-Id")
    print(f"Session ID: {session_id}")

    result = _parse_sse(init_resp.text)
    print(f"Response: {json.dumps(result, indent=2, ensure_ascii=False)[:500]}")
    print()

    # 2. List tools using session ID
    print("=" * 60)
    print("2. List Tools")
    print("=" * 60)
    session_headers = headers.copy()
    if session_id:
        session_headers["Mcp-Session-Id"] = session_id

    tools_resp = requests.post(
        MCP_URL,
        json={"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
        headers=session_headers,
        timeout=10
    )
    print(f"Status: {tools_resp.status_code}")
    result = _parse_sse(tools_resp.text)
    if "result" in result and "tools" in result["result"]:
        tools = result["result"]["tools"]
        print(f"\n找到 {len(tools)} 个工具:\n")
        for i, tool in enumerate(tools, 1):
            print(f"{i}. {tool['name']}")
            if tool.get('description'):
                desc = tool['description'][:60] + "..." if len(tool['description']) > 60 else tool['description']
                print(f"   {desc}")
            print()
    else:
        print(f"Response: {tools_resp.text[:500]}")
    print()

    # 3. Call speak tool
    print("=" * 60)
    print("3. Call speak tool")
    print("=" * 60)
    speak_resp = requests.post(
        MCP_URL,
        json={
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "speak",
                "arguments": {"text": "Hello from FastMCP client", "async_mode": True}
            }
        },
        headers=session_headers,
        timeout=30
    )
    print(f"Status: {speak_resp.status_code}")
    result = _parse_sse(speak_resp.text)
    if "result" in result:
        print(f"Success! {result['result']}")
    else:
        print(f"Response: {speak_resp.text[:500]}")
    print()

    # 4. Call search_papers tool
    print("=" * 60)
    print("4. Call search_papers (Semantic Scholar)")
    print("=" * 60)
    search_resp = requests.post(
        MCP_URL,
        json={
            "jsonrpc": "2.0",
            "id": 4,
            "method": "tools/call",
            "params": {
                "name": "search_papers",
                "arguments": {"query": "attention mechanism", "limit": 2}
            }
        },
        headers=session_headers,
        timeout=60
    )
    print(f"Status: {search_resp.status_code}")
    result = _parse_sse(search_resp.text)
    if "result" in result:
        print(f"Success! Got papers")
        # result 可能是 dict 或 JSON 字符串
        result_data = result["result"]
        if isinstance(result_data, str):
            papers_data = json.loads(result_data)
        else:
            papers_data = result_data
        count = len(papers_data.get("papers", []))
        print(f"Found {count} papers")
        if count > 0:
            print(f"Sample: {json.dumps(papers_data['papers'][0], indent=2, ensure_ascii=False)[:500]}")
    else:
        print(f"Response: {search_resp.text[:500]}")

    print("\n" + "=" * 60)
    print("测试完成!")
    print("=" * 60)


if __name__ == "__main__":
    main()
