# ============================================================================
# 文件: test_listener.py
# 描述: 测试语音识别功能
# ============================================================================

"""测试 Listener 语音识别功能"""

import sys
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent / "src"))

from audio import Listener, RecognitionResult


def test_listen_once():
    """测试单次录音识别"""
    print("=" * 50)
    print("测试: 单次录音并识别")
    print("=" * 50)

    listener = Listener()
    print(f"语音识别可用: {listener.is_available}")

    if not listener.is_available:
        print("请先安装依赖: uv add SpeechRecognition pocketsphinx pyaudio")
        return

    print("\n请在 5 秒内开始说话，最长录音 10 秒...")
    result = listener.listen_once(timeout=5, phrase_time_limit=10)

    if result.success:
        print(f"\n识别成功: {result.text}")
    else:
        print(f"\n识别失败: {result.error}")


def test_key_listener():
    """测试按键监听录音"""
    print("=" * 50)
    print("测试: 按键监听录音识别")
    print("=" * 50)

    listener = Listener(trigger_key="f12")
    print(f"语音识别可用: {listener.is_available}")

    if not listener.is_available:
        print("请先安装依赖: uv add SpeechRecognition pocketsphinx pyaudio pynput")
        return

    def on_result(result: RecognitionResult):
        if result.success:
            print(f"\n识别结果: {result.text}")
        else:
            print(f"\n识别失败: {result.error}")

    print("\n按住 F12 开始录音，松开停止...")
    listener.start_key_listener(on_result=on_result)

    try:
        # 保持运行
        while listener._keyboard_listener and listener._keyboard_listener.is_alive():
            import time
            time.sleep(0.1)
    except KeyboardInterrupt:
        listener.stop_key_listener()
        print("\n已停止")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "key":
        test_key_listener()
    else:
        test_listen_once()
