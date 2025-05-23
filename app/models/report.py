#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/models/report.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""


from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List as PyList, Dict, Any, Union
from enum import Enum
import uuid
from datetime import datetime, timezone
from .common import BaseModelWithTimestamps, Identifier

# --- Specific Model Definition for Report ---

class ReportModel(BaseModelWithTimestamps, Identifier):
    assessment_id: str = Field(description="此报告关联的评估ID。")
    project_name: str
    project_url: HttpUrl
    llm_generated_summary: Optional[str] = None
    evaluation_metrics_summary: Dict[str, Any] = Field(default_factory=dict)
    detailed_findings: PyList[Dict[str, Any]] = Field(default_factory=list)
    visualization_paths: Dict[str, str] = Field(default_factory=dict)


# Example usage:
# if __name__ == "__main__":
#     if "report" == "intent": 
#         # Example: test_intent = IntentModel(query="analyze this repo", evaluation_aspects=["activity"])
#         # print(test_intent.model_dump_json(indent=2))
#         pass
