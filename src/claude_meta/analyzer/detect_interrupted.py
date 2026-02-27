# ============================================================================
# 文件: claude_meta/analyzer/detect_interrupted.py
# 描述: 检测中断的会话
#
# 上游依赖: claude_meta/config/paths.py, claude_meta/reader/get_sessions.py
# 下游封装: 无
# Bash 快速定位: find . -name "detect_interrupted.py"
# ============================================================================

from typing import List

from claude_meta.config.paths import ClaudeMetaPaths
from claude_meta.reader.get_sessions import get_sessions


def detect_interrupted(paths: ClaudeMetaPaths) -> List:
    """检测中断的会话

    中断的会话是指 ended_at 为 null 的会话。

    Args:
        paths: ClaudeMetaPaths 路径配置

    Returns:
        中断的会话列表
    """
    sessions = get_sessions(paths)

    # 检测 ended_at == updated_at 或 ended_at 为 None 的会话
    interrupted = [
        s for s in sessions if s.ended_at == s.created_at
    ]

    return interrupted
