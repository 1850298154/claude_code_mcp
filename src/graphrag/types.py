# ============================================================================
# 文件: src/graphrag/types.py
# 描述: GraphRAG 模块类型定义
#
# 上游依赖: 无
# 下游封装: builder.py, qa/*
#
# Bash 快速定位:
#   find . -name "types.py" -path "*/graphrag/*"
# ============================================================================

from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from pathlib import Path
from datetime import datetime
from enum import Enum


class EntityType(Enum):
    """实体类型枚举"""

    PROJECT = "project"
    FILE = "file"
    FUNCTION = "function"
    CLASS = "class"
    VARIABLE = "variable"
    CONCEPT = "concept"


@dataclass
class Entity:
    """图谱实体数据结构

    Attributes:
        id: 实体唯一标识符
        type: 实体类型
        name: 实体名称
        description: 实体描述
        properties: 额外属性
        source: 来源文件
    """

    id: str
    type: EntityType
    name: str
    description: Optional[str] = None
    properties: Optional[Dict[str, Any]] = None
    source: Optional[str] = None


@dataclass
class Relation:
    """图谱关系数据结构

    Attributes:
        id: 关系唯一标识符
        source_id: 源实体 ID
        target_id: 目标实体 ID
        type: 关系类型
        properties: 额外属性
    """

    id: str
    source_id: str
    target_id: str
    type: str
    properties: Optional[Dict[str, Any]] = None


@dataclass
class Graph:
    """知识图谱数据结构

    Attributes:
        entities: 实体列表
        relations: 关系列表
        metadata: 图谱元数据
    """

    entities: List[Entity]
    relations: List[Relation]
    metadata: Optional[Dict[str, Any]] = None


@dataclass
class QAContext:
    """问答上下文

    Attributes:
        graph: 知识图谱
        question: 用户问题
        relevant_entities: 相关实体
    """

    graph: Graph
    question: str
    relevant_entities: List[Entity]


@dataclass
class Answer:
    """问答答案

    Attributes:
        answer: 答案内容
        confidence: 置信度
        sources: 来源引用
        entities: 涉及的实体
    """

    answer: str
    confidence: float
    sources: List[str]
    entities: List[str]
