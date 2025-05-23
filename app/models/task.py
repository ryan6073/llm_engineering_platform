#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/models/task.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""


from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List as PyList, Dict, Any, Union
from enum import Enum
import uuid
from datetime import datetime, timezone
from .common import BaseModelWithTimestamps, Identifier

# --- Specific Model Definition for Task ---

class TaskStatusEnum(str, Enum):
    PENDING = "pending"
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class TaskModel(BaseModelWithTimestamps, Identifier):
    name: str = Field(description="任务的可读名称。")
    task_type: str = Field(description="任务的类型，例如：data_collection, evaluation, llm_call。")
    status: TaskStatusEnum = Field(default=TaskStatusEnum.PENDING)
    parameters: Dict[str, Any] = Field(default_factory=dict, description="任务执行所需的参数。")
    dependencies: PyList[str] = Field(default_factory=list, description="此任务依赖的其他任务ID列表。")
    assigned_agent_id: Optional[str] = Field(None, description="分配执行此任务的Agent ID。")
    result: Optional[Any] = Field(None, description="任务执行的结果。")
    error_message: Optional[str] = Field(None, description="如果任务失败，则为错误消息。")
    assessment_id: Optional[str] = Field(None, description="此任务所属的评估ID。")


# Example usage:
# if __name__ == "__main__":
#     if "task" == "intent": 
#         # Example: test_intent = IntentModel(query="analyze this repo", evaluation_aspects=["activity"])
#         # print(test_intent.model_dump_json(indent=2))
#         pass
