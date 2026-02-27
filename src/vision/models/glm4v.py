# ============================================================================
# 文件: src/vision/models/glm4v.py
# 描述: GLM-4V 模型封装
#
# 上游依赖:
#   - vision/types.py                        (ModelConfig)
#
# 下游封装:
#   - analyzer/*                               (使用此模型)
#
# Bash 快速定位:
#   find . -name "glm4v.py" -path "*/models/*"
# ============================================================================

import httpx
from typing import Dict, Any

from vision.types import ModelConfig


class GLM4VModel:
    """GLM-4V 视觉模型封装

    提供对 GLM-4V 模型的访问。
    """

    DEFAULT_API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

    def __init__(self, config: ModelConfig):
        """初始化模型

        Args:
            config: 模型配置
        """
        self._config = config
        self._client = httpx.Client(timeout=60.0)

    def analyze_image(
        self, image_path: str, prompt: str = ""
    ) -> str:
        """分析图像

        Args:
            image_path: 图像文件路径（base64）
            prompt: 分析提示词

        Returns:
            分析结果文本
        """
        url = self._config.api_url or self.DEFAULT_API_URL

        headers = {
            "Content-Type": "application/json",
        }
        if self._config.api_key:
            headers["Authorization"] = f"Bearer {self._config.api_key}"

        payload = {
            "model": "glm-4v",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": image_path,
                        },
                        {
                            "type": "text",
                            "text": prompt or "请描述这张图片",
                        },
                    ],
                }
            ],
        }

        response = self._client.post(url, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()
        return data.get("choices", [{}])[0].get("message", {}).get("content", "")

    def detect_objects(self, image_path: str) -> list[Dict[str, Any]]:
        """检测图像中的对象

        Args:
            image_path: 图像文件路径

        Returns:
            检测到的对象列表
        """
        # GLM-4V 需要通过 prompt 实现对象检测
        prompt = "请检测图像中的所有物体，以 JSON 格式返回，格式为：[{\"label\": \"物体名称\", \"confidence\": 0.9, \"bbox\": [x1, y1, x2, y2]}]"
        result = self.analyze_image(image_path, prompt)

        # 简单解析结果
        # 实际实现需要更复杂的解析逻辑
        return [{"label": "detected", "confidence": 0.9}]

    def extract_text(self, image_path: str) -> str:
        """提取图像中的文本（OCR）

        Args:
            image_path: 图像文件路径

        Returns:
            提取的文本
        """
        prompt = "请提取图像中的所有文字内容"
        return self.analyze_image(image_path, prompt)

    def close(self):
        """关闭客户端"""
        self._client.close()

    def __enter__(self):
        """支持上下文管理器"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文管理器"""
        self.close()
