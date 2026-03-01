#!/usr/bin/env python
# 简单的语音播放HTTP服务器

import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import sys

# 简单的语音播放
def speak_text(text: str):
    """使用Windows语音播放文本"""
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        return True
    except Exception as e:
        print(f"播放失败: {e}")
        return False


class SpeakHandler(BaseHTTPRequestHandler):
    """简单的HTTP请求处理器"""

    def do_POST(self):
        """处理POST请求"""
        if self.path == "/speak":
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                # 尝试多种编码
                body = self.rfile.read(content_length)
                try:
                    data = json.loads(body.decode('utf-8'))
                except:
                    data = json.loads(body.decode('gbk'))

                text = data.get('text', '')
                if not text:
                    self.send_error(400, "Missing 'text' parameter")
                    return

                text = data.get('text', '')
                if not text:
                    self.send_error(400, "Missing 'text' parameter")
                    return

                # 在新线程中播放（不阻塞HTTP响应）
                thread = threading.Thread(target=speak_text, args=(text,))
                thread.daemon = False
                thread.start()

                # 立即返回响应
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "playing", "text": text}).encode('utf-8'))
            except Exception as e:
                self.send_error(500, str(e))
        else:
            self.send_error(404, "Not Found")

    def log_message(self, format, *args):
        """禁止默认日志输出"""
        pass


def main():
    """启动服务器"""
    HOST = "0.0.0.0"
    PORT = 9001

    server = HTTPServer((HOST, PORT), SpeakHandler)
    print(f"简单语音服务器运行在 http://{HOST}:{PORT}")
    print(f"用法: curl -X POST http://127.0.0.1:{PORT}/speak -H 'Content-Type: application/json' -d '{{\"text\":\"你好\"}}'")
    print()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
        server.shutdown()


if __name__ == "__main__":
    main()
