# ============================================================================
# 文件: src/graphrag/builder/add_entity.py
# 描述: 添加实体函数
#
# 上游依赖:
#   - graphrag/types.py                       (Entity)
#
# 下游封装:
#   - graphrag/builder.py                     (GraphBuilder.add_entity)
#
# Bash 快速定位:
#   find . -name "add_entity.py" -path "*/builder/*"
# ============================================================================

from graphrag.types import Entity


def add_entity(entities: List[Entity], entity: Entity) -> None:
    """添加实体到图谱

    Args:
        entities: 实体列表
        entity: 要添加的实体
    """
    entities.append(entity)
