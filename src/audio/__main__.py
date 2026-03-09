# ============================================================================
# 文件: src/audio/__main__.py
# 描述: 音频模块命令行入口
# ============================================================================

"""音频模块命令行入口

提供命令行接口用于测试音频功能。
"""

import sys
from .speaker import Speaker
from .listener import Listener


def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("Usage: python -m audio <command> [args]")
        print("\nCommands:")
        print("  speak <text>     - 播放语音")
        print("  listen           - 启动语音识别（按F12录音）")
        print("  listen-once      - 单次录音并识别")
        return

    command = sys.argv[1]

    if command == "speak":
        if len(sys.argv) < 3:
            print("Usage: python -m audio speak <text>")
            return
        text = " ".join(sys.argv[2:])
        speaker = Speaker()
        speaker.speak(text)

    elif command == "listen":
        print("启动语音识别监听器...")
        listener = Listener()
        listener.start_key_listener()
        # 保持运行
        try:
            listener._keyboard_listener.join()
        except KeyboardInterrupt:
            listener.stop_key_listener()
            print("\n已停止")

    elif command == "listen-once":
        print("开始录音（说话后自动停止）...")
        listener = Listener()
        result = listener.listen_once(timeout=5, phrase_time_limit=10)
        if result.success:
            print(f"识别结果: {result.text}")
        else:
            print(f"识别失败: {result.error}")

    else:
        print(f"未知命令: {command}")


if __name__ == "__main__":
    main()
