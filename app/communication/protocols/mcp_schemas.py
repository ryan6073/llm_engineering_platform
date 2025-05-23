#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/communication/protocols/mcp_schemas.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/communication/protocols/mcp_schemas.py
# 定义多Agent通信协议(MCP)消息结构的Pydantic模型。
# 标准化Agent交换信息的方式。

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, Union, List as PyList # PyList以避免与Message.List冲突
from enum import Enum
import uuid
from datetime import datetime, timezone

class Performative(str, Enum):
    REQUEST = "request"         # 请求执行动作
    INFORM = "inform"           #告知事实或结果
    QUERY_REF = "query_ref"     # 查询引用/资源信息
    PROPOSE = "propose"         # 提出建议
    ACCEPT_PROPOSAL = "accept_proposal" # 接受建议
    REJECT_PROPOSAL = "reject_proposal" # 拒绝建议
    FAILURE = "failure"         #告知动作执行失败
    CONFIRM = "confirm"         # 确认收到消息或动作完成
    CANCEL = "cancel"           # 取消先前的请求
    SUBSCRIBE = "subscribe"     # 订阅信息流
    NOT_UNDERSTOOD = "not_understood" # 无法理解消息
    # 根据需要添加更多FIPA类或自定义的Performative

class Message(BaseModel):
    message_id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="消息的唯一ID。")
    sender_id: str = Field(description="发送方Agent的ID。")
    # 接收方可以是单个Agent ID，ID列表，或用于通过总线广播的特殊值（如"ALL"）
    receiver_id: Union[str, PyList[str]] = Field(description="接收方Agent的ID或ID列表。")
    performative: Performative = Field(description="消息的意图或类型。")
    content: Any = Field(description="实际的有效载荷，可以是另一个Pydantic模型。")
    ontology: Optional[str] = Field(None, description="描述内容领域的本体。")
    language: str = Field(default="JSON", description="内容的语言/格式（例如JSON, XML）。")
    protocol: str = Field(default="CustomMCP_v1.0", description="遵循的通信协议版本。")
    conversation_id: Optional[str] = Field(None, description="用于对对话中的相关消息进行分组。")
    in_reply_to: Optional[str] = Field(None, description="此消息回复的消息的ID。")
    reply_with: Optional[str] = Field(None, description="期望回复匹配的标识符。") # 用于关联回复
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="消息创建的时间戳(UTC)。")

    # 示例内容模型 (可以在Agent特定逻辑中定义更具体的模型)
    # class RequestContent(BaseModel):
    #     action_name: str
    #     parameters: Dict[str, Any]

    # class InformContent(BaseModel):
    #     status_code: int
    #     data: Any
    #     message_text: Optional[str] = None

# 示例用法：
# if __name__ == "__main__":
#     msg = Message(
#         sender_id="agent1_analyzer",
#         receiver_id="agent2_dataprovider",
#         performative=Performative.REQUEST,
#         content={"action_name": "get_project_commits", "parameters": {"project_url": "http://example.com/repo"}},
#         ontology="ProjectAssessmentOntology_v1",
#         conversation_id=str(uuid.uuid4())
#     )
#     print(msg.model_dump_json(indent=2))
