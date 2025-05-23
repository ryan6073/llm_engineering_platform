#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/api/endpoints/assessment.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/api/endpoints/assessment.py
# 与项目评估相关的API端点。

from fastapi import APIRouter, HTTPException, Body, Depends
from typing import Any, Optional
from ...core.orchestrator import Orchestrator # 示例编排器
from ..schemas import AssessmentRequestSchema, AssessmentCreationResponseSchema, HealthCheckResponse # 示例Schema
from ...core.agent_registry import agent_registry # 假设全局或通过依赖注入

router = APIRouter()

# 依赖注入Orchestrator的简单示例
async def get_orchestrator():
    # 在实际应用中，Orchestrator可能在应用启动时创建并管理
    # 这里我们假设它依赖于agent_registry
    return Orchestrator(registry=agent_registry)


@router.post("/assess", response_model=AssessmentCreationResponseSchema)
async def create_assessment_endpoint(
    request: AssessmentRequestSchema = Body(...),
    orchestrator: Orchestrator = Depends(get_orchestrator) # 注入Orchestrator
):
    """
    端点，用于发起新的开源项目评估。
    Orchestrator通常处理请求并协调Agent。
    """
    try:
        print(f"API: 收到评估请求 - 查询: {request.query}, URL: {request.project_url}")
        
        # 调用Orchestrator处理请求
        # 这应该返回一个任务ID或初始状态
        assessment_id, status_url = await orchestrator.initiate_assessment_flow(
            user_query=str(request.query), # 确保是字符串 
            project_url=str(request.project_url) if request.project_url else None # 确保是字符串或None
        )
        
        return AssessmentCreationResponseSchema(
            assessment_id=assessment_id,
            message="评估已成功启动。",
            status_url=status_url # 例如：/api/v1/assessment/{assessment_id}/status
        )
    except Exception as e:
        # 记录异常 e
        print(f"API错误: {e}")
        raise HTTPException(status_code=500, detail=f"评估启动失败: {str(e)}")

@router.get("/health", response_model=HealthCheckResponse)
async def health_check():
    return HealthCheckResponse(status="healthy")

# 在 app.main.py 中链接:
# from .api.endpoints import assessment_router
# app.include_router(assessment_router, prefix="/api/v1/assessment", tags=["Assessment"])
