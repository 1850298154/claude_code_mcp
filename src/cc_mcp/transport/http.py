# ============================================================================
# 文件: src/cc_mcp/transport/http.py
# 描述: HTTP 传输层
#
# 上游依赖: 无
# 下游封装: cc_mcp/server.py, cc_mcp/cli.py
#
# Bash 快速定位:
#   find . -name "http.py" -path "*/transport/*"
# ============================================================================

"""HTTP 传输层

通过 HTTP 进行 MCP 通信，支持 RESTful API 风格。
"""

import asyncio
import json
import logging
from typing import Optional, Callable, Any, Dict

from aiohttp import web

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HTTPTransport:
    """HTTP 传输层

    通过 HTTP 进行 MCP 通信，支持 `/mcp` 端点。
    """

    def __init__(self, host: str = "127.0.0.1", port: int = 8000):
        """初始化传输层

        Args:
            host: 监听主机地址
            port: 监听端口
        """
        self._host = host
        self._port = port
        self._app: Optional[web.Application] = None
        self._runner: Optional[web.AppRunner] = None
        self._site: Optional[web.TCPSite] = None
        self._running: bool = False
        self._request_handler: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]] = None

    def set_request_handler(self, handler: Callable[[Dict[str, Any]], Dict[str, Any]]):
        """设置请求处理器

        Args:
            handler: 请求处理函数
        """
        self._request_handler = handler

    async def _handle_mcp_request(self, request: web.Request) -> web.Response:
        """处理 MCP HTTP 请求

        Args:
            request: aiohttp 请求对象

        Returns:
            aiohttp 响应对象
        """
        try:
            # 读取请求体
            body = await request.text()
            if not body:
                return web.json_response(
                    {"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid Request"}},
                    status=400
                )

            # 解析 JSON
            mcp_request = json.loads(body)
            logger.debug(f"Received HTTP request: {mcp_request}")

            # 处理请求
            if self._request_handler:
                # 对于 HTTP，我们需要用 asyncio 处理异步 handler
                if asyncio.iscoroutinefunction(self._request_handler):
                    mcp_response = await self._request_handler(mcp_request)
                else:
                    mcp_response = self._request_handler(mcp_request)
            else:
                mcp_response = {
                    "jsonrpc": "2.0",
                    "id": mcp_request.get("id"),
                    "error": {"code": -32601, "message": "No handler set"}
                }

            logger.debug(f"Sending HTTP response: {mcp_response}")

            # 返回 JSON 响应
            return web.json_response(mcp_response)

        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON: {e}")
            return web.json_response(
                {"jsonrpc": "2.0", "error": {"code": -32700, "message": "Parse error"}},
                status=400
            )
        except Exception as e:
            logger.error(f"Error handling request: {e}")
            return web.json_response(
                {"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}},
                status=500
            )

    async def _handle_health(self, request: web.Request) -> web.Response:
        """健康检查端点

        Args:
            request: aiohttp 请求对象

        Returns:
            aiohttp 响应对象
        """
        return web.json_response({"status": "ok", "service": "claude-code-mcp"})

    def _create_app(self) -> web.Application:
        """创建 aiohttp 应用

        Returns:
            aiohttp 应用对象
        """
        app = web.Application()
        app.router.add_post("/mcp", self._handle_mcp_request)
        app.router.add_get("/health", self._handle_health)
        app.router.add_get("/mcp", self._handle_mcp_request)  # 支持 GET 请求
        return app

    async def start_server(self, init_callback=None):
        """启动 HTTP 服务器

        Args:
            init_callback: 初始化回调函数
        """
        self._running = True

        # 调用初始化回调
        if init_callback:
            init_callback()

        # 创建应用
        self._app = self._create_app()

        # 创建 Runner
        self._runner = web.AppRunner(self._app)

        # 启动
        await self._runner.setup()

        # 创建 Site
        self._site = web.TCPSite(self._runner, self._host, self._port)

        # 启动服务
        await self._site.start()

        uri = f"http://{self._host}:{self._port}/mcp"
        logger.info(f"HTTP server started on {uri}")
        logger.info(f"Health check: http://{self._host}:{self._port}/health")

        # 服务器会一直运行，直到被停止
        while self._running:
            await asyncio.sleep(1)

    async def stop(self):
        """停止服务器"""
        self._running = False
        if self._site:
            await self._site.stop()
        if self._runner:
            await self._runner.cleanup()
        logger.info("HTTP server stopped")

    async def read_line(self) -> Optional[str]:
        """HTTP 不使用此方法

        Returns:
            None
        """
        return None

    async def write_line(self, line: str):
        """HTTP 不使用此方法

        Args:
            line: 要写入的内容
        """
        pass


async def start_http_server(host: str = "127.0.0.1", port: int = 8000):
    """启动 HTTP 服务器

    Args:
        host: 监听主机
        port: 监听端口
    """
    transport = HTTPTransport(host, port)
    await transport.start_server()


__all__ = ["HTTPTransport", "start_http_server"]
