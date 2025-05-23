#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/main.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/main.py
# FastAPI应用入口，全局配置，以及MAS初始化。

from fastapi import FastAPI
from typing import Optional
# from .api.endpoints.assessment import router as assessment_router # 示例路由
from .core.agent_registry import agent_registry # 示例Agent注册中心
# from .agents.intent_agent import IntentAgentImpl # 示例Agent导入以供注册
# from .agents.data_agent import DataAgentImpl   # 示例Agent导入以供注册
from .config import settings # 导入配置

app = FastAPI(
    title=settings.APP_NAME,
    description="基于LLM和多Agent系统的开源项目智能评估平台",
    version="0.1.0"
)

@app.on_event("startup")
async def startup_event():
    """应用启动逻辑：
    - 初始化数据库连接（如有）
    - 加载配置
    - 向AgentRegistry注册Agent
    - 启动后台任务
    """
    print(f"应用 '{settings.APP_NAME}' 启动中...")
    # 示例：
    # intent_ag = IntentAgentImpl()
    # await intent_ag.register_self(agent_registry) # Agent 自注册
    # data_ag = DataAgentImpl()
    # await data_ag.register_self(agent_registry)
    print("Agent注册完成 (示例)。")
    # 可以在这里初始化其他服务，例如Neo4j客户端的连接池等

@app.on_event("shutdown")
async def shutdown_event():
    """应用关闭逻辑：
    - 关闭数据库连接
    - 优雅关闭Agent或后台任务
    """
    print("应用关闭中...")
    # 示例：
    # await agent_registry.deregister_all_agents() # 或Agent自行注销
    # if neo4j_client: await neo4j_client.close_async()

# app.include_router(assessment_router, prefix="/api/v1", tags=["Assessment"]) # 调整了prefix

@app.get("/")
async def read_root():
    return {"message": f"欢迎来到 {settings.APP_NAME}!"}

# if __name__ == "__main__":
#     import uvicorn
#     # 通常由Uvicorn运行 app:app
#     uvicorn.run(app, host="0.0.0.0", port=8000)
