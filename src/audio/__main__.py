# ============================================================================
# 文件: src/audio/__main__.py
# 描述: 音频模块命令行入口
# ============================================================================

"""音频模块命令行入口

提供命令行接口用于测试音频功能。
"""

import sys
from .speaker import Speaker


def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("Usage: python -m audio <text>")
        return

    text = " ".join(sys.argv[1:])
    speaker = Speaker()
    speaker.speak(text)


if __name__ == "__main__":
    main()
