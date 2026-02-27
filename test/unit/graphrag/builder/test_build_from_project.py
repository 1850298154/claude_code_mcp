# ============================================================================
# 文件: test/unit/graphrag/builder/test_build_from_project.py
# 描述: 测试 build_from_project 函数
#
# 测试对象: src/graphrag/builder/build_from_project.py
#
# Bash 快速定位:
#   find test -name "test_build_from_project.py"
# ============================================================================

import pytest
from pathlib import Path

from graphrag.types import Entity, Relation, EntityType
from graphrag.builder.build_from_project import build_from_project


class TestBuildFromProject:
    """测试 build_from_project 函数"""

    def test_build_from_project_empty(self, tmp_dir):
        """测试空目录构建图谱"""
        # Given: 空目录
        empty_dir = tmp_dir / "empty"
        empty_dir.mkdir()

        # When: 构建图谱
        graph = build_from_project(empty_dir)

        # Then: 图谱只有项目实体
        assert len(graph.entities) == 1
        assert graph.entities[0].type == EntityType.PROJECT

    def test_build_from_project_with_files(self, tmp_dir):
        """测试带文件的目录构建图谱"""
        # Given: 带文件的目录
        project_dir = tmp_dir / "test_project"
        project_dir.mkdir()
        (project_dir / "file1.py").write_text("content")
        (project_dir / "file2.py").write_text("content")

        # When: 构建图谱
        graph = build_from_project(project_dir)

        # Then: 图谱包含项目和文件实体
        assert len(graph.entities) == 3
        assert any(e.type == EntityType.PROJECT for e in graph.entities)
        assert any(e.type == EntityType.FILE for e in graph.entities)
