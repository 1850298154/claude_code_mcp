# ============================================================================
# 文件: src/graphrag/builder/add_relation.py
# 描述: 添加关系函数
#
# 上游依赖:
#   - graphrag/types.py                       (Relation)
#
# 下游封装:
#   - graphrag/builder.py                     (GraphBuilder.add_relation)
#
# Bash 快速定位:
#   find . -name "add_relation.py" -path "*/builder/*"
# ============================================================================

from graphrag.types import Relation


def add_relation(relations: List[Relation], relation: Relation) -> None:
    """添加关系到图谱

    Args:
        relations: 关系列表
        relation: 要添加的关系
    """
    relations.append(relation)
