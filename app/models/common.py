#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/models/common.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""


from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List as PyList, Dict, Any, Union
from enum import Enum
import uuid
from datetime import datetime, timezone


# --- Specific Model Definition for Common ---

class BaseModelWithTimestamps(BaseModel):
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Identifier(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="唯一标识符。")


# Example usage:
# if __name__ == "__main__":
#     if "common" == "intent": 
#         # Example: test_intent = IntentModel(query="analyze this repo", evaluation_aspects=["activity"])
#         # print(test_intent.model_dump_json(indent=2))
#         pass
