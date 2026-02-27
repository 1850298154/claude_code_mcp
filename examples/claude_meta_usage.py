# ============================================================================
# 文件: examples/claude_meta_usage.py
# 描述: ClaudeMeta 使用示例
#
# Bash 快速定位: find . -name "claude_meta_usage.py"
# ============================================================================

"""
ClaudeMeta 使用示例

展示如何使用 ClaudeMetaReader 读取 ~/.claude 元信息。
"""

from pathlib import Path
from claude_meta.reader import ClaudeMetaReader


def main():
    """主函数"""
    # 初始化 Reader
    reader = ClaudeMetaReader()

    # 1. 获取所有会话
    print("=== 获取所有会话 ===")
    sessions = reader.get_sessions()
    print(f"找到 {len(sessions)} 个会话")

    for session in sessions[:5]:  # 只显示前 5 个
        print(f"  - {session.id}: {session.title} ({session.project})")

    # 2. 检测中断的会话
    print("\n=== 检测中断的会话 ===")
    interrupted = reader.detect_interrupted()
    print(f"找到 {len(interrupted)} 个中断的会话")

    # 3. 恢复会话
    if sessions:
        print(f"\n=== 恢复会话 {sessions[0].id} ===")
        session = reader.restore_session(
            session_id=sessions[0].id,
            project=sessions[0].project
        )
        print(f"  标题: {session.title}")
        print(f"  项目: {session.project}")
        print(f"  消息数: {len(session.messages)}")

    # 4. 获取项目上下文
    if sessions:
        print(f"\n=== 项目上下文 ({sessions[0].project}) ===")
        context = reader.get_project_context(sessions[0].project)
        print(f"  会话数: {context['total_sessions']}")
        print(f"  消息数: {context['total_messages']}")

    # 5. 获取记忆
    print("\n=== 记忆 ===")
    memory = reader.get_memory()
    if memory:
        print(f"  记忆长度: {len(memory)} 字符")
        print(f"  预览: {memory[:100]}...")
    else:
        print("  无记忆内容")


if __name__ == "__main__":
    main()
