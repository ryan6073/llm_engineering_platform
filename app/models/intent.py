#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/models/intent.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""


from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List as PyList, Dict, Any, Union
from enum import Enum
import uuid
from datetime import datetime, timezone
from .common import BaseModelWithTimestamps, Identifier

# --- Specific Model Definition for Intent ---

class IntentModel(BaseModelWithTimestamps, Identifier):
    query: str = Field(description="用户的原始查询。")
    detected_project_url: Optional[HttpUrl] = Field(None, description="检测到的项目URL。")
    evaluation_aspects: PyList[str] = Field(default_factory=list, description="要评估的方面。")
    parsed_parameters: Dict[str, Any] = Field(default_factory=dict, description="从查询中解析的其他参数。")
    status: str = Field(default="pending", description="意图处理状态。")


# Example usage:
# if __name__ == "__main__":
#     if "intent" == "intent": 
#         # Example: test_intent = IntentModel(query="analyze this repo", evaluation_aspects=["activity"])
#         # print(test_intent.model_dump_json(indent=2))
#         pass
