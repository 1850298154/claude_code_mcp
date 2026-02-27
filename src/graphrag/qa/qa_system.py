# ============================================================================
# 文件: src/graphrag/qa/qa_system.py
# 描述: QASystem 类定义
#
# 上游依赖:
#   - graphrag/types.py                        (QAContext, Answer)
#   - graphrag/builder.py                    (GraphBuilder)
#
# 下游封装:
#   - qa/ask.py                                (ask 函数)
#   - qa/retrieve.py                           (retrieve 函数)
#   - qa/generate_answer.py                      (generate_answer 函数)
#   - mcp/tools/graphrag.py                     (MCP 工具封装)
#
# Bash 快速定位:
#   find . -name "qa_system.py" -path "*/qa/*"
# ============================================================================

from typing import List

from graphrag.types import QAContext, Answer
from graphrag.builder.query_graph import query_graph


class QASystem:
    """QA System - 问答系统

    提供基于知识图谱的问答能力。
    """

    def __init__(self, builder):
        """初始化 QA 系统

        Args:
            builder: GraphBuilder 实例
        """
        self._builder = builder

    def ask(self, question: str, top_k: int = 5) -> Answer:
        """提问

        Args:
            question: 用户问题
            top_k: 返回 top k 个结果

        Returns:
            答案对象
        """
        # 查询图谱获取相关实体
        results = self._builder.query_graph(question)

        # 简单实现：使用查询结果构建答案
        answer_text = f"找到 {len(results)} 个与 '{question}' 相关的结果。"
        for i, result in enumerate(results[:top_k]):
            answer_text += f"\n{i+1}. {result.get('name', result.get('id', 'N/A'))}"

        return Answer(
            answer=answer_text,
            confidence=min(0.9, 1.0 / max(len(results), 1)),
            sources=[r.get("id", "") for r in results],
            entities=[r.get("id", "") for r in results],
        )

    def retrieve(self, question: str, top_k: int = 5) -> List[dict]:
        """检索相关内容

        Args:
            question: 用户问题
            top_k: 返回 top k 个结果

        Returns:
            检索结果列表
        """
        return self._builder.query_graph(question)[:top_k]

    def generate_answer(self, question: str, context: str) -> Answer:
        """生成答案

        Args:
            question: 用户问题
            context: 上下文信息

        Returns:
            答案对象
        """
        # 简单实现：组合上下文和问题
        answer = f"基于上下文: {question} 的回答"
        return Answer(
            answer=answer,
            confidence=0.7,
            sources=["context"],
            entities=[],
        )
