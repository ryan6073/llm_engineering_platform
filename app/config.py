#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/config.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/config.py
# 应用配置设置。
# 使用Pydantic BaseSettings进行环境变量加载和类型验证。

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional, List
from pathlib import Path # 确保导入Path

class Settings(BaseSettings):
    # --- 通用设置 ---
    APP_NAME: str = "LLM Engineering Platform"
    DEBUG_MODE: bool = False
    PROJECT_BASE_PATH: str = str(Path(__file__).resolve().parent.parent) # app目录的父目录

    # --- LLM配置 ---
    LLM_PROVIDER: str = "openai" # 例如："openai", "azure", "local_qwen"
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_MODEL_NAME: str = "gpt-4o" # 默认模型
    AZURE_OPENAI_ENDPOINT: Optional[str] = None
    AZURE_OPENAI_KEY: Optional[str] = None
    AZURE_OPENAI_DEPLOYMENT_NAME: Optional[str] = None
    # 本地模型，如Qwen
    LOCAL_LLM_MODEL_PATH: Optional[str] = None 
    LOCAL_LLM_API_BASE: Optional[str] = "http://localhost:8000/v1" # 本地服务器示例

    # --- 知识库配置 ---
    # 向量存储 (FAISS示例 - 路径通常由faiss_client管理)
    FAISS_INDEX_PATH: str = "data/vector_store/index.faiss"
    EMBEDDING_MODEL_NAME: str = 'all-MiniLM-L6-v2' # 用于FAISS的嵌入模型

    # 图数据库 (Neo4j)
    NEO4J_URI: str = "bolt://localhost:7687"
    NEO4J_USER: str = "neo4j"
    NEO4J_PASSWORD: str = "password"

    # Web搜索 (通用API密钥示例)
    SEARCH_ENGINE_API_KEY: Optional[str] = None
    SEARCH_ENGINE_CX: Optional[str] = None # Google自定义搜索

    # --- Agent系统配置 ---
    AGENT_REGISTRY_HOST: str = "localhost" # 如果AgentRegistry是独立服务
    AGENT_REGISTRY_PORT: int = 50051 # gRPC或其他服务示例端口
    MESSAGE_BUS_URL: Optional[str] = None # 例如："redis://localhost:6379/0" (Celery/Redis)

    # --- 数据连接器API密钥 ---
    GITHUB_TOKEN: Optional[str] = None
    GITEE_TOKEN: Optional[str] = None
    
    # --- 模板目录 ---
    PROMPT_TEMPLATE_DIR: str = "app/prompts/templates" # 相对项目根目录

    # --- 数据存储目录 ---
    DATA_DIR: str = "data" # 顶级数据目录
    REPORTS_DIR: str = "data/reports"
    PLOTS_DIR: str = "data/reports/plots"


    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8', extra='ignore')

settings = Settings()

# 确保路径是绝对的或相对于项目根目录
# from pathlib import Path # 已在类定义之上导入
settings.FAISS_INDEX_PATH = str(Path(settings.PROJECT_BASE_PATH) / settings.FAISS_INDEX_PATH)
settings.PROMPT_TEMPLATE_DIR = str(Path(settings.PROJECT_BASE_PATH) / settings.PROMPT_TEMPLATE_DIR)
settings.DATA_DIR = str(Path(settings.PROJECT_BASE_PATH) / settings.DATA_DIR)
settings.REPORTS_DIR = str(Path(settings.PROJECT_BASE_PATH) / settings.REPORTS_DIR)
settings.PLOTS_DIR = str(Path(settings.PROJECT_BASE_PATH) / settings.PLOTS_DIR)

# 示例用法: print(settings.APP_NAME)
