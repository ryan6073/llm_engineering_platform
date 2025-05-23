#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/knowledge_base/graph_store/neo4j_client.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/knowledge_base/graph_store/neo4j_client.py
# 与Neo4j图数据库交互的客户端。

from neo4j import AsyncGraphDatabase # FastAPI使用AsyncGraphDatabase
from typing import Dict, List, Any, Optional
# from ...config import settings # 用于配置

class Neo4jClient:
    _driver: Optional[AsyncGraphDatabase.driver] = None # 类级别驱动程序以实现共享

    def __init__(self, uri: str, user: str, password: str):
        self._uri = uri
        self._auth = (user, password)
        # 驱动程序将在首次需要时惰性初始化
        print(f"Neo4jClient已为URI配置：{uri}")

    async def _get_driver(self) -> AsyncGraphDatabase.driver:
        if Neo4jClient._driver is None or Neo4jClient._driver.closed():
            try:
                Neo4jClient._driver = AsyncGraphDatabase.driver(self._uri, auth=self._auth)
                await Neo4jClient._driver.verify_connectivity() # 确保连接有效
                print("Neo4j异步驱动程序已连接并验证。")
            except Exception as e:
                print(f"连接到Neo4j异步驱动程序失败：{e}")
                Neo4jClient._driver = None # 连接失败时重置驱动程序
                raise # 重新引发异常以表示连接失败
        return Neo4jClient._driver

    async def close_driver(self): # 类方法，在应用关闭时调用
        if Neo4jClient._driver and not Neo4jClient._driver.closed():
            await Neo4jClient._driver.close()
            Neo4jClient._driver = None
            print("Neo4j异步驱动程序已关闭。")

    async def execute_query(self, query: str, parameters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """执行Cypher查询并返回结果。"""
        driver = await self._get_driver()
        if not driver:
            return [{"error": "Neo4j连接不可用。"}]
            
        records_data: List[Dict[str, Any]] = []
        query_summary = None
        try:
            # Neo4j建议对异步操作使用异步会话
            async with driver.session() as session:
                results = await session.run(query, parameters)
                # 异步处理记录
                records_data = [record.data() async for record in results] 
                query_summary = await results.consume() # 消耗流的其余部分并获取摘要
        except Exception as e:
            print(f"执行Neo4j查询时出错：{query} | 参数：{parameters} | 错误：{e}")
            return [{"error": str(e)}] # 返回错误信息
        
        print(f"查询已执行。Cypher：'{query[:70]}...', 参数：{parameters}。"
              f"返回 {len(records_data)} 条记录。摘要计数器：{query_summary.counters if query_summary else 'N/A'}")
        return records_data

    async def execute_write_query(self, query: str, parameters: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, int]]:
        """执行写查询并返回操作计数器。"""
        driver = await self._get_driver()
        if not driver:
            return {"error": "Neo4j连接不可用。"}

        try:
            async with driver.session() as session:
                # 使用事务函数执行写操作
                summary = await session.write_transaction(self._run_write_transaction_fn, query, parameters)
            print(f"写查询已执行。摘要计数器：{summary.counters if summary else 'N/A'}")
            return summary.counters if summary else None # 例如：nodes_created, relationships_created
        except Exception as e:
            print(f"执行Neo4j写查询时出错：{e}")
            return {"error": str(e)}

    @staticmethod
    async def _run_write_transaction_fn(tx, query, parameters): # 事务函数必须是静态的或在类外部
        result = await tx.run(query, parameters)
        summary = await result.consume() # 在事务中消耗结果很重要
        return summary

# 示例用法 (通常在应用启动/关闭时管理驱动程序生命周期)
# from ...config import settings
# neo4j_client_instance = Neo4jClient(uri=settings.NEO4J_URI, user=settings.NEO4J_USER, password=settings.NEO4J_PASSWORD)
#
# async def example_neo4j_usage():
#     try:
#         results = await neo4j_client_instance.execute_query("MATCH (n) RETURN count(n) AS node_count")
#         print("节点计数:", results)
#     finally:
#         # 通常在应用关闭时调用
#         # await neo4j_client_instance.close_driver() 
#         pass 
