# ============================================================================
# 文件: src/cc_mcp/transport/websocket.py
# 描述: WebSocket 传输层
#
# 上游依赖: 无
# 下游封装: cc_mcp/server.py, cc_mcp/cli.py
#
# Bash 快速定位:
#   find . -name "websocket.py" -path "*/transport/*"
# ============================================================================

"""WebSocket 传输层

通过 WebSocket 进行 MCP 通信，支持持久连接和状态共享。
"""

import asyncio
import json
import logging
from typing import Optional

import websockets

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class WebSocketTransport:
    """WebSocket 传输层

    通过 WebSocket 进行持久通信，解决 stdio 每次启动的问题。
    """

    def __init__(self, host: str = "127.0.0.1", port: int = 8765):
        """初始化传输层

        Args:
            host: 监听主机地址
            port: 监听端口
        """
        self._host = host
        self._port = port
        self._websocket = None
        self._server = None
        self._running = False

    async def handle_connection(self, websocket):
        """处理客户端连接

        Args:
            websocket: WebSocket 连接
        """
        self._websocket = websocket
        logger.info(f"Client connected from {websocket.remote_address}")

        try:
            async for message in websocket:
                try:
                    request = json.loads(message)
                    logger.debug(f"Received request: {request}")

                    # 委托给外部处理器
                    if hasattr(self, '_request_handler'):
                        response = await self._request_handler(request)
                        response_json = json.dumps(response)
                        await websocket.send(response_json)
                        logger.debug(f"Sent response: {response_json}")
                    else:
                        logger.warning("No request handler set")

                except json.JSONDecodeError as e:
                    logger.error(f"Invalid JSON: {e}")
                    error_response = {
                        "jsonrpc": "2.0",
                        "id": request.get("id"),
                        "error": {
                            "code": -32700,
                            "message": "Parse error"
                        }
                    }
                    await websocket.send(json.dumps(error_response))
                except Exception as e:
                    logger.error(f"Error handling request: {e}")
                    error_response = {
                        "jsonrpc": "2.0",
                        "id": request.get("id"),
                        "error": {
                            "code": -32603,
                            "message": str(e)
                        }
                    }
                    await websocket.send(json.dumps(error_response))

        except websockets.exceptions.ConnectionClosed:
            logger.info("Client disconnected")
        except Exception as e:
            logger.error(f"Connection error: {e}")
        finally:
            self._websocket = None

    async def read_line(self) -> Optional[str]:
        """WebSocket 不使用此方法

        Returns:
            None
        """
        return None

    async def write_line(self, line: str):
        """WebSocket 不使用此方法

        Args:
            line: 要写入的内容
        """
        # WebSocket 使用 send 方法
        pass

    async def send_to_client(self, data: dict):
        """主动向客户端发送数据

        Args:
            data: 要发送的数据
        """
        if self._websocket:
            try:
                await self._websocket.send(json.dumps(data))
                logger.debug(f"Sent to client: {data}")
            except Exception as e:
                logger.error(f"Failed to send to client: {e}")

    async def start_server(self, init_callback=None):
        """启动 WebSocket 服务器

        Args:
            init_callback: 初始化回调函数
        """
        self._running = True

        uri = f"ws://{self._host}:{self._port}"
        logger.info(f"Starting WebSocket server on {uri}")

        # 调用初始化回调
        if init_callback:
            init_callback()

        self._server = await websockets.serve(
            self.handle_connection,
            self._host,
            self._port
        )

        logger.info(f"WebSocket server listening on {self._host}:{self._port}")

        # 服务器会一直运行，直到被停止
        while self._running:
            await asyncio.sleep(1)

    async def stop(self):
        """停止服务器"""
        self._running = False
        if self._server:
            self._server.close()
            logger.info("WebSocket server stopped")


async def start_websocket_server(host: str = "127.0.0.1", port: int = 8765):
    """启动 WebSocket 服务器

    Args:
        host: 监听主机
        port: 监听端口
    """
    from ..cli import main
    from .websocket import WebSocketTransport

    transport = WebSocketTransport(host, port)
    server = await transport._create_server()

    try:
        await server.serve_forever()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
    finally:
        server.close()


__all__ = ["WebSocketTransport", "start_websocket_server"]
