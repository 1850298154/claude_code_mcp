# ============================================================================
# 文件: claude_meta/analyzer/summarize_progress.py
# 描述: 总结会话的进度
#
# 上游依赖: core/types/claude/conversation.py, claude_meta/analyzer/extract_context.py
# 下游封装: 无
# Bash 快速定位: find . -name "summarize_progress.py"
# ============================================================================

from typing import Dict, Any

from core.types.claude.conversation import Conversation
from claude_meta.analyzer.extract_context import extract_context


def summarize_progress(conversation: Conversation) -> Dict[str, Any]:
    """总结会话的进度

    Args:
        conversation: Conversation 对象

    Returns:
        进度总结字典，包含状态、完成度、下一步等
    """
    context = extract_context(conversation)

    # 判断会话状态
    is_interrupted = context["total_messages"] > 0 and (
        context["last_user_query"]
        and "?" in context["last_user_query"]
    )

    # 估算完成度（基于消息数量和工具调用）
    completion_score = 0.0
    if context["total_messages"] > 0:
        completion_score = min(1.0, context["assistant_messages"] / max(1, context["user_messages"]) * 0.7 + len(context["tool_calls"]) * 0.1)

    # 提取下一步建议
    next_steps = []
    if is_interrupted:
        next_steps.append("恢复中断的工作")
    if "实现" in context["task_keywords"]:
        next_steps.append("继续实现功能")
    if "测试" in context["task_keywords"]:
        next_steps.append("添加或运行测试")
    if len(context["file_references"]) > 0:
        next_steps.append(f"检查相关文件: {', '.join(context['file_references'][:3])}")

    return {
        "session_id": context["session_id"],
        "project": context["project"],
        "status": "interrupted" if is_interrupted else "completed",
        "completion_score": completion_score,
        "total_progress": f"{completion_score * 100:.1f}%",
        "task_summary": f"{' '.join(context['task_keywords'])} {context['project']}" if context['task_keywords'] else f"与 {context['project']} 相关的对话",
        "files_modified": len(context["file_references"]),
        "next_steps": next_steps,
        "last_activity": conversation.updated_at,
    }
