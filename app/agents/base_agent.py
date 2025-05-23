#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/agents/base_agent.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/agents/base_agent.py
# 系统中所有Agent的抽象基类。
# 定义核心Agent行为、生命周期、通信接口(MCP)、能力描述及与AgentRegistry的交互。

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import uuid
from datetime import datetime

# from ..communication.protocols.mcp_schemas import Message, Performative # 示例MCP Schema
# from ..core.agent_registry import AgentRegistry # 用于类型提示

class BaseAgent(ABC):
    def __init__(self, agent_id: Optional[str] = None, agent_name: Optional[str] = None):
        self.agent_id: str = agent_id or f"{self.__class__.__name__}-{str(uuid.uuid4())[:8]}"
        self.agent_name: str = agent_name or self.__class__.__name__
        self.capabilities: List[str] = self._define_capabilities()
        # self.message_bus = None # 或其他通信处理器
        print(f"Agent {self.agent_id} ({self.agent_name}) 已初始化，能力：{self.capabilities}")

    @abstractmethod
    def _define_capabilities(self) -> List[str]:
        """每个Agent必须定义其能力。"""
        pass

    async def register_self(self, registry): # 传入AgentRegistry实例
        """向AgentRegistry注册Agent。"""
        # 在实际场景中，'self'可能是端点或代理对象
        metadata = {"name": self.agent_name, "registered_at": datetime.utcnow().isoformat()}
        await registry.register_agent(self.agent_id, self, self.capabilities, metadata)

    async def deregister_self(self, registry): # 传入AgentRegistry实例
        """从AgentRegistry注销Agent。"""
        await registry.deregister_agent(self.agent_id)

    @abstractmethod
    async def handle_message(self, message: Any) -> Optional[Any]: # 'Message' 类型来自mcp_schemas
        """
        根据MCP处理传入消息。
        这是A2A通信的主要入口点。
        """
        pass

    async def send_message(self, recipient_agent_id: str, message_content: Any, performative: Any, # Performative类型
                           message_bus: Optional[Any] = None, registry: Optional[Any] = None, # MessageBus, AgentRegistry类型
                           conversation_id: Optional[str] = None, in_reply_to: Optional[str] = None):
        """
        向另一个Agent发送消息，可能通过消息总线或直接调用。
        """
        # from ..communication.protocols.mcp_schemas import Message # 延迟导入以避免循环
        # msg = Message(
        #     sender_id=self.agent_id,
        #     receiver_id=recipient_agent_id,
        #     performative=performative,
        #     content=message_content,
        #     conversation_id=conversation_id,
        #     in_reply_to=in_reply_to
        # )
        # print(f"Agent {self.agent_id} 尝试向 {recipient_agent_id} 发送消息: {msg.model_dump(exclude_none=True)}")
        # if message_bus:
        #     await message_bus.route_message_to_agent(recipient_agent_id, msg, registry)
        # elif registry: # 简单直接调用（仅限本地测试）
        #     recipient_agent = await registry.find_agent_by_id(recipient_agent_id)
        #     if recipient_agent:
        #         return await recipient_agent.handle_message(msg)
        #     else:
        #         print(f"错误：接收方Agent {recipient_agent_id} 未找到。")
        #         return None
        # else:
        #     print("错误：未提供MessageBus或AgentRegistry用于发送消息。")
        #     return None
        print(f"Agent {self.agent_id} 模拟向 {recipient_agent_id} 发送消息内容: {message_content}")
        return {"status": "message_sent_simulation_placeholder"}


    @abstractmethod
    async def execute_task(self, task_details: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Agent执行其专业任务的核心逻辑。
        可能由Orchestrator或其他Agent调用。
        """
        pass

    async def startup(self, registry): # 传入AgentRegistry实例
        """Agent启动时调用（例如，在应用启动期间）。"""
        print(f"Agent {self.agent_id} 启动中...")
        await self.register_self(registry)

    async def shutdown(self, registry): # 传入AgentRegistry实例
        """Agent关闭时调用。"""
        print(f"Agent {self.agent_id} 关闭中...")
        await self.deregister_self(registry)
