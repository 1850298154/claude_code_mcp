# ============================================================================
# 文件: claude_meta/reader/get_memory.py
# 描述: 获取记忆内容
#
# 上游依赖: claude_meta/config/paths.py, claude_meta/parser/parse_memory.py
# 下游封装: 无
# Bash 快速定位: find . -name "get_memory.py"
# ============================================================================

from pathlib import Path

from claude_meta.config.paths import ClaudeMetaPaths
from claude_meta.parser.parse_memory import parse_memory


def get_memory(paths: ClaudeMetaPaths) -> str:
    """获取记忆内容

    Args:
        paths: ClaudeMetaPaths 路径配置

    Returns:
        记忆内容字符串，如果文件不存在则返回空字符串
    """
    memory_file = paths.get_memory_file()
    if not memory_file.exists():
        return ""
    return parse_memory(memory_file)
