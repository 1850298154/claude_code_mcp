# ============================================================================
# 文件: src/graphrag/builder/build_from_project.py
# 描述: 从项目构建图谱函数
#
# 上游依赖:
#   - graphrag/types.py                       (Graph, Entity, Relation)
#   - graphrag/builder.py                     (GraphBuilder)
#
# 下游封装:
#   - mcp/tools/graphrag.py                     (MCP 工具封装)
#
# Bash 快速定位:
#   find . -name "build_from_project.py" -path "*/builder/*"
# ============================================================================

from pathlib import Path
from typing import List

from graphrag.types import Graph, Entity, Relation, EntityType


def build_from_project(project_path: Path | str) -> Graph:
    """从项目构建图谱

    Args:
        project_path: 项目路径

    Returns:
        构建的知识图谱
    """
    if isinstance(project_path, Path):
        project_path = str(project_path)

    # 扫描项目目录
    project_dir = Path(project_path)
    entities = []
    relations = []

    # 添加项目实体
    project_entity = Entity(
        id=f"project:{project_dir.name}",
        type=EntityType.PROJECT,
        name=project_dir.name,
        description=f"Project at {project_path}",
        source=str(project_dir),
        properties={"path": str(project_dir)},
    )
    entities.append(project_entity)

    # 扫描 Python 文件
    for file_path in project_dir.rglob("*.py"):
        file_entity = Entity(
            id=f"file:{file_path}",
            type=EntityType.FILE,
            name=file_path.name,
            description=f"Python file: {file_path.name}",
            source=str(file_path),
            properties={"path": str(file_path)},
        )
        entities.append(file_entity)

        # 添加文件到项目的关系
        relation = Relation(
            id=f"relation:{project_dir.name}-{file_path.name}",
            source_id=project_entity.id,
            target_id=file_entity.id,
            type="contains",
        )
        relations.append(relation)

    return Graph(entities=entities, relations=relations)
