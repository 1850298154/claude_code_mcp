# ============================================================================
# 文件: claude_meta/parser/parse_history.py
# 描述: 解析历史文件，返回用户查询列表
#
# 上游依赖: 无
# 下游封装: reader/get_sessions.py, analyzer/extract_context.py
# Bash 快速定位: find . -name "parse_history.py"
# ============================================================================

import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any


@dataclass
class HistoryEntry:
    """历史记录条目

    Attributes:
        query: 用户查询内容
        timestamp: 查询时间戳
        project: 关联的项目名称
    """

    query: str
    timestamp: datetime
    project: str


def parse_history(data: List[Dict[str, Any]]) -> List[HistoryEntry]:
    """解析历史数据为 HistoryEntry 列表

    Args:
        data: 历史 JSON 数据

    Returns:
        HistoryEntry 列表
    """
    entries = []

    for entry in data:
        history_entry = HistoryEntry(
            query=entry["query"],
            timestamp=datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00")),
            project=entry.get("project", ""),
        )
        entries.append(history_entry)

    return entries


def parse_history_from_file(file_path: Path) -> List[HistoryEntry]:
    """从文件解析历史记录

    Args:
        file_path: 历史文件路径

    Returns:
        HistoryEntry 列表
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return parse_history(data)
