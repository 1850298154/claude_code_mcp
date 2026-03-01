# ============================================================================
# 文件: src/graphrag/builder.py
# 描述: GraphBuilder 类定义，用于知识图谱构建
#
# 上游依赖:
#   - graphrag/types.py                       (Graph, Entity, Relation)
#
# 下游封装:
#   - builder/*                                 (操作函数)
#   - mcp/tools/graphrag.py                     (MCP 工具封装)
#
# Bash 快速定位:
#   find . -name "builder.py" -path "*/graphrag/*"
# ============================================================================

from pathlib import Path
from typing import List, Optional

from graphrag.types import Graph, Entity, Relation, EntityType


class GraphBuilder:
    """Graph Builder - 知识图谱构建

    提供从项目、文档构建知识图谱的能力。
    """

    def __init__(self):
        """初始化 Builder"""
        self._graph: Optional[Graph] = None

    @property
    def graph(self) -> Optional[Graph]:
        """获取当前图谱"""
        return self._graph

    def build_from_project(self, project_path: Path | str) -> Graph:
        """从项目构建图谱

        实现位置: builder/build_from_project.py

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

        # 扫描子目录
        for subdir in project_dir.iterdir():
            if subdir.is_dir():
                subdir_entity = Entity(
                    id=f"directory:{subdir.name}",
                    type=EntityType.PROJECT,
                    name=subdir.name,
                    description=f"Directory: {subdir.name}",
                    source=str(subdir),
                )
                entities.append(subdir_entity)

                relation = Relation(
                    id=f"relation:{project_dir.name}-{subdir.name}",
                    source_id=project_entity.id,
                    target_id=subdir_entity.id,
                    type="contains",
                )
                relations.append(relation)

        self._graph = Graph(entities=entities, relations=relations)
        return self._graph

    def build_from_docs(self, docs: List[Path]) -> Graph:
        """从文档构建图谱

        实现位置: builder/build_from_docs.py

        Args:
            docs: 文档路径列表

        Returns:
            构建的知识图谱
        """
        entities = []
        relations = []

        for doc_path in docs:
            if isinstance(doc_path, str):
                doc_path = Path(doc_path)

            # 添加文档实体
            doc_entity = Entity(
                id=f"doc:{doc_path.name}",
                type=EntityType.FILE,
                name=doc_path.name,
                description=f"Document: {doc_path.name}",
                source=str(doc_path),
            )
            entities.append(doc_entity)

        self._graph = Graph(entities=entities, relations=relations)
        return self._graph

    def add_entity(self, entity: Entity) -> None:
        """添加实体

        实现位置: builder/add_entity.py

        Args:
            entity: 要添加的实体
        """
        if self._graph is None:
            self._graph = Graph(entities=[], relations=[])

        self._graph.entities.append(entity)

    def add_relation(self, relation: Relation) -> None:
        """添加关系

        实现位置: builder/add_relation.py

        Args:
            relation: 要添加的关系
        """
        if self._graph is None:
            self._graph = Graph(entities=[], relations=[])

        self._graph.relations.append(relation)

    def query_graph(self, query: str) -> List[dict]:
        """查询图谱

        实现位置: builder/query_graph.py

        Args:
            query: 查询语句

        Returns:
            查询结果
        """
        if self._graph is None:
            return []

        results = []

        # 简单的实体匹配查询
        for entity in self._graph.entities:
            if query.lower() in entity.name.lower():
                results.append({
                    "type": "entity",
                    "id": entity.id,
                    "name": entity.name,
                    "description": entity.description,
                })

        # 简单的关系匹配查询
        for relation in self._graph.relations:
            if query.lower() in relation.type.lower():
                results.append({
                    "type": "relation",
                    "id": relation.id,
                    "source": relation.source_id,
                    "target": relation.target_id,
                })

        return results

    def clear(self) -> None:
        """清空图谱"""
        self._graph = None
