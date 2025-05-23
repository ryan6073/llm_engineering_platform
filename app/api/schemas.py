#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/api/schemas.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/api/schemas.py
# 用于API请求/响应验证和序列化的Pydantic模型。

from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List, Dict, Any
from enum import Enum
import uuid # 确保导入
from datetime import datetime

class HealthCheckResponse(BaseModel):
    status: str = "healthy"

# --- 评估Schema ---
class AssessmentRequestSchema(BaseModel):
    query: str = Field(..., min_length=1, description="用户对评估的自然语言查询。")
    project_url: Optional[HttpUrl] = Field(None, description="开源项目的URL (例如GitHub, Gitee)。")
    # 可选：指定评估方面，例如：evaluation_aspects: List[str] = []

class AssessmentCreationResponseSchema(BaseModel):
    assessment_id: str = Field(description="评估的唯一ID。")
    message: str = Field(description="操作状态消息。")
    status_url: str = Field(description="用于检查此评估状态的URL。")


class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class TaskInfoSchema(BaseModel):
    task_id: str
    task_name: str
    description: Optional[str] = None
    status: TaskStatus
    result: Optional[Any] = None
    error_message: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

class AssessmentStatusResponseSchema(BaseModel):
    assessment_id: str
    overall_status: TaskStatus # 使用TaskStatus枚举
    summary: Optional[str] = None
    tasks: List[TaskInfoSchema] = []
    final_report_url: Optional[HttpUrl] = None # 生成报告的链接

# 可根据 app/models/report.py 中的模型定义更详细的报告Schema
class FinalReportSchema(BaseModel):
    report_id: str
    assessment_id: str
    project_name: str
    generated_at: datetime
    assessment_summary_llm: Optional[str] = None
    key_findings: Dict[str, Any] # 例如：{"activity_score": 0.8, "security_issues": []}
    # ... 更详细的报告结构
