#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/communication/message_bus.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/communication/message_bus.py
# (可选) 实现用于异步Agent间通信的消息总线。
# 可使用Redis Pub/Sub, RabbitMQ, Kafka等技术，或用于本地开发的简单内存队列。

from typing import Dict, List, Callable, Any, Awaitable
# from ..core.agent_registry import AgentRegistry # 用于查找接收方Agent

class MessageBus: # 概念性占位符
    def __init__(self):
        # 初始化到总线技术的连接（如有）
        print("MessageBus已初始化 (内存概念占位符)。")
        # topic -> list of async handlers
        self._subscriptions: Dict[str, List[Callable[[Any], Awaitable[None]]]] = {} 

    async def publish(self, topic: str, message: Any): # Message类型来自mcp_schemas
        """向主题发布消息。"""
        print(f"MessageBus: 向主题 '{topic}' 发布: {message}")
        if topic in self._subscriptions:
            for handler in self._subscriptions[topic]:
                await handler(message) # 假设handler是异步的

    async def subscribe(self, topic: str, handler: Callable[[Any], Awaitable[None]]): # Message类型
        """将Agent的处理程序订阅到主题。"""
        self._subscriptions.setdefault(topic, [])
        if handler not in self._subscriptions[topic]: # 避免重复订阅
            self._subscriptions[topic].append(handler)
            print(f"MessageBus: 处理程序已订阅主题 '{topic}'。")

    async def route_message_to_agent(self, agent_id: str, message: Any, registry: Any): # Message类型, AgentRegistry类型
        """将直接消息路由到特定Agent，可能通过其已知主题或直接收件箱。"""
        print(f"MessageBus: 尝试将消息路由到Agent '{agent_id}': {message}")
        target_agent = await registry.find_agent_by_id(agent_id)
        if target_agent and hasattr(target_agent, 'handle_message'):
            await target_agent.handle_message(message) # 直接调用Agent的处理方法
        else:
            print(f"MessageBus: Agent '{agent_id}' 未找到或没有handle_message方法。")

# 全局实例或注入
# message_bus = MessageBus()
