# ============================================================================
# 文件: claude_meta/analyzer/extract_context.py
# 描述: 提取会话的上下文关键信息
#
# 上游依赖: core/types/claude/conversation.py
# 下游封装: 无
# Bash 快速定位: find . -name "extract_context.py"
# ============================================================================

from typing import List, Dict, Any
from core.types.claude.conversation import Conversation


def extract_context(conversation: Conversation) -> Dict[str, Any]:
    """提取会话的上下文关键信息

    Args:
        conversation: Conversation 对象

    Returns:
        上下文字典，包含主题、任务、文件等关键信息
    """
    # 提取用户消息
    user_messages = [m for m in conversation.messages if m.role.value == "user"]

    # 提取助手消息
    assistant_messages = [
        m for m in conversation.messages if m.role.value == "assistant"
    ]

    # 提取工具调用信息（从 metadata 中）
    tool_calls = []
    for msg in assistant_messages:
        if msg.metadata and "tool_calls" in msg.metadata:
            tool_calls.extend(msg.metadata["tool_calls"])

    # 提取文件引用（简单匹配模式）
    file_references = []
    for msg in conversation.messages:
        import re
        files = re.findall(r'[\w/\\]+\.(py|js|ts|md|txt|json|yaml|yml)', msg.content)
        file_references.extend(files)

    # 提取任务关键词
    task_keywords = []
    keywords = ["实现", "优化", "修复", "添加", "删除", "重构", "测试"]
    for msg in user_messages:
        for keyword in keywords:
            if keyword in msg.content:
                task_keywords.append(keyword)

    return {
        "session_id": conversation.id,
        "project": conversation.project,
        "title": conversation.title,
        "started_at": conversation.created_at,
        "total_messages": len(conversation.messages),
        "user_messages": len(user_messages),
        "assistant_messages": len(assistant_messages),
        "tool_calls": tool_calls,
        "file_references": list(set(file_references)),
        "task_keywords": list(set(task_keywords)),
        "last_user_query": user_messages[-1].content if user_messages else "",
    }
