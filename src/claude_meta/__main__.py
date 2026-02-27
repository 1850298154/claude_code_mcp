# ============================================================================
# 文件: src/claude_meta/__main__.py
# 描述: Claude Meta 模块主入口
#
# Bash 快速定位:
#   find src -name "__main__.py" -path "*/claude_meta/*"
# ============================================================================

"""Claude Meta 模块主入口"""

from claude_meta.config.paths import ClaudeMetaPaths
from claude_meta.reader import ClaudeMetaReader


def main():
    """主函数"""
    paths = ClaudeMetaPaths()
    reader = ClaudeMetaReader(paths)

    # 打印会话列表
    sessions = reader.get_sessions()
    print(f"Found {len(sessions)} sessions:")
    for session in sessions:
        print(f"  - {session.id}: {session.title}")


if __name__ == "__main__":
    main()
