#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/knowledge_base/connectors/base_connector.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/knowledge_base/connectors/base_connector.py
# 所有数据源连接器的抽象基类。

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class BaseConnector(ABC):
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        print(f"{self.__class__.__name__} 已初始化。")

    @abstractmethod
    async def connect(self):
        """如果需要，建立到数据源的连接。"""
        pass

    @abstractmethod
    async def disconnect(self):
        """如果需要，关闭到数据源的连接。"""
        pass

    @abstractmethod
    async def fetch_data(self, query: Any, params: Optional[Dict] = None) -> Any:
        """根据查询和参数从源获取数据。"""
        pass

    async def test_connection(self) -> bool:
        """测试到数据源的连接是否正常。"""
        # 默认实现，如果需要特定测试则覆盖
        try:
            await self.connect()
            # 如果可能，执行简单的读取或状态检查
            await self.disconnect()
            return True
        except Exception as e:
            print(f"{self.__class__.__name__} 的连接测试失败：{e}")
            return False
