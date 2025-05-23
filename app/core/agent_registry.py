#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/core/agent_registry.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/core/agent_registry.py
# Agent注册中心：管理Agent的动态注册、注销和发现。
# Agent注册其能力、地址和其他元数据。

from typing import Dict, List, Any, Optional
# from ..agents.base_agent import BaseAgent # 用于BaseAgent类型提示

class AgentRegistry:
    def __init__(self):
        # agent_id -> agent_instance 或 agent_metadata (如地址、能力列表)
        self._agents: Dict[str, Any] = {} 
        # capability_name -> list of agent_ids
        self._capabilities: Dict[str, List[str]] = {} 
        print("AgentRegistry已初始化。")

    async def register_agent(self, agent_id: str, agent_instance: Any, capabilities: List[str], metadata: Optional[Dict] = None):
        """向注册中心注册Agent。"""
        if agent_id in self._agents:
            print(f"警告：Agent {agent_id} 已注册。将重新注册。")
        
        # 目前直接存储实例；在分布式系统中可能是地址/端点等元数据
        self._agents[agent_id] = {"instance": agent_instance, "metadata": metadata or {}}
        
        for capability in capabilities:
            self._capabilities.setdefault(capability, [])
            if agent_id not in self._capabilities[capability]:
                self._capabilities[capability].append(agent_id)
        
        print(f"Agent {agent_id} 已注册，能力：{capabilities}, 元数据：{metadata}")

    async def deregister_agent(self, agent_id: str):
        """注销Agent。"""
        if agent_id in self._agents:
            del self._agents[agent_id]
            for capability in list(self._capabilities.keys()): # 迭代键的副本
                if agent_id in self._capabilities[capability]:
                    self._capabilities[capability].remove(agent_id)
                    if not self._capabilities[capability]: # 如果没有Agent提供此能力，则移除该能力
                        del self._capabilities[capability]
            print(f"Agent {agent_id} 已注销。")
        else:
            print(f"警告：尝试注销未找到的Agent {agent_id}。")

    async def find_agent_by_id(self, agent_id: str) -> Optional[Any]: # 返回Agent实例或元数据
        """通过ID查找Agent。"""
        agent_info = self._agents.get(agent_id)
        return agent_info["instance"] if agent_info else None # 简化：返回实例

    async def find_agents_by_capability(self, capability: str) -> List[Any]: # 返回Agent实例列表
        """查找提供特定能力的所有Agent。"""
        agent_ids = self._capabilities.get(capability, [])
        return [self._agents[agent_id]["instance"] for agent_id in agent_ids if agent_id in self._agents]

    async def find_agent_by_capability(self, capability: str) -> Optional[Any]: # 返回单个Agent实例
        """查找提供特定能力的第一个可用Agent（简单策略）。"""
        agents = await self.find_agents_by_capability(capability)
        return agents[0] if agents else None
        
    async def list_all_agents_info(self) -> Dict[str, Dict]:
        """列出所有已注册Agent及其信息。"""
        return {
            agent_id: {
                "capabilities": [cap for cap, ids in self._capabilities.items() if agent_id in ids],
                "metadata": agent_data.get("metadata", {})
            }
            for agent_id, agent_data in self._agents.items()
        }

# 全局实例（简单方法，大型应用考虑依赖注入）
agent_registry = AgentRegistry() 
