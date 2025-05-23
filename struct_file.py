#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform_generator
@File    : project_generator.py
@Author  : Gemini AI (Generated for Ryan Zhu)
@Date    : 2025/05/22
"""

import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Union, Callable, Awaitable # Added Dict and other potentially used types

# --- Configuration ---
BASE_PROJECT_NAME = "llm_engineering_platform" # 在注释和某些路径中使用
PROJECT_ROOT = Path(".") / "generated_llm_project" # 在子文件夹中创建文件

AUTHOR_NAME = "Ryan Zhu"
# 使用您示例中的特定日期；对于当前日期，请使用：
# GENERATION_DATE = datetime.now().strftime("%Y/%m/%d %H:%M")
GENERATION_DATE = "2025/05/19 01:31" # 根据您的示例


FILE_HEADER_TEMPLATE = """#!/usr/bin/env python
# -*- coding: UTF-8 -*-
\"\"\"
@Project : {project_name}
@File    : {file_path_for_header}
@Author  : {author_name}
@Date    : {generation_date}
\"\"\"
"""

# --- File Definitions ---

# 创建带有头部的Python文件内容的辅助函数
def create_python_file_content(file_path_obj: Path, content: str, project_name: str =BASE_PROJECT_NAME, author_name: str =AUTHOR_NAME, generation_date: str =GENERATION_DATE) -> str:
    # 获取用于头部的代表性路径，例如：app/agents/base_agent.py
    try:
        # 如果在'app'之外，则尝试使其相对于'app'或项目根目录
        if 'app' in file_path_obj.parts:
            idx = file_path_obj.parts.index('app')
            header_path_str = '/'.join(file_path_obj.parts[idx:])
        else:
            header_path_str = file_path_obj.name # 对于根目录下的文件
    except ValueError:
        header_path_str = file_path_obj.name # 回退

    header = FILE_HEADER_TEMPLATE.format(
        project_name=project_name,
        file_path_for_header=header_path_str, # 显示时使用相对路径
        author_name=author_name,
        generation_date=generation_date
    )
    return f"{header}\n{content}"

FILES_TO_CREATE: Dict[str, str] = {
    # --- 根目录文件 ---
    ".gitignore": """
# 字节编译/优化/DLL文件
__pycache__/
*.py[cod]
*$py.class

# C扩展
*.so

# 分发/打包
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# 安装程序日志
pip-log.txt
pip-delete-this-directory.txt

# 单元测试/覆盖率报告
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
pytestdebug.log

# 翻译
*.mo
*.pot

# Django 相关:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask 相关:
instance/
.webassets-cache

# Scrapy 相关:
.scrapy

# Sphinx 文档
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# PEP 582
__pypackages__/

# Celery 相关
celerybeat-schedule
celerybeat.pid

# SageMath 解析文件
*.sage.py

# 环境
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder 项目设置
.spyderproject
.spyderworkspace

# Rope 项目设置
.ropeproject

# mkdocs 文档
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre 类型检查器
.pyre/

# pytype
.type/

# Cython 调试符号
cython_debug/
""",
    "README.md": f"""
# {BASE_PROJECT_NAME}

基于LLM和多Agent系统的开源项目智能评估平台。

## 项目概览

本系统利用大型语言模型（LLM）和动态多Agent系统（MAS）架构，为开源项目提供全面的评估。主要特性包括：

- 用户意图识别与解析。
- 动态任务分解与专业Agent的协作执行。
- Agent注册、发现以及A2A/MCP通信。
- 使用Jinja2模板的复杂提示词工程。
- 集成多样化知识源：
    - 版本控制：GitHub、Gitee API。
    - 漏洞数据库：OSV。
    - 图数据库：Neo4j用于关系分析。
    - 向量存储：FAISS用于语义搜索。
    - Web搜索：实时信息检索。
- 可扩展的评估指标。
- 结构化报告生成与可视化。

## 安装与设置

1. 克隆本仓库。
2. 创建虚拟环境: `python -m venv venv`
3. 激活虚拟环境: `source venv/bin/activate` (Linux/macOS) 或 `venv\\Scripts\\activate` (Windows)
4. 安装依赖: `pip install -r requirements.txt`
5. 在 `app/config.py` 中配置API密钥及其他设置，或通过环境变量配置。
6. 运行应用: `uvicorn app.main:app --reload`

## 项目结构

(请参考生成的文件结构及文件内的注释。)
""",
    "requirements.txt": """
fastapi>=0.100.0
uvicorn[standard]>=0.20.0
pydantic>=2.0.0
pydantic-settings>=2.0.0
httpx>=0.24.0
jinja2>=3.0.0
# langchain # 或您偏好的LLM交互库
# openai # 如果使用OpenAI
python-dotenv>=1.0.0

# 数据分析与可视化
pandas>=2.0.0
matplotlib>=3.0.0
seaborn>=0.12.0

# 向量存储
faiss-cpu # 或 faiss-gpu (如果支持CUDA)

# 图数据库
neo4j>=5.0.0 # Neo4j官方驱动
networkx>=3.0

# Web搜索 (示例，取决于使用的服务)
# google-api-python-client
# beautifulsoup4
# requests

# MAS / 通信 (如果使用特定库)
# asyncio # 内置

# 其他特定依赖
# ...
""",

    # --- app/ ---
    "app/__init__.py": create_python_file_content(PROJECT_ROOT / "app" / "__init__.py",
        "# app/__init__.py\n# 初始化 'app' 包。"
    ),
    "app/main.py": create_python_file_content(PROJECT_ROOT / "app" / "main.py",
        """# app/main.py
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
    \"\"\"应用启动逻辑：
    - 初始化数据库连接（如有）
    - 加载配置
    - 向AgentRegistry注册Agent
    - 启动后台任务
    \"\"\"
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
    \"\"\"应用关闭逻辑：
    - 关闭数据库连接
    - 优雅关闭Agent或后台任务
    \"\"\"
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
"""
    ),
    "app/config.py": create_python_file_content(PROJECT_ROOT / "app" / "config.py",
        """# app/config.py
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
"""
    ),

    # --- app/api/ ---
    "app/api/__init__.py": create_python_file_content(PROJECT_ROOT / "app" / "api" / "__init__.py",
        "# app/api/__init__.py"
    ),
    "app/api/endpoints/__init__.py": create_python_file_content(PROJECT_ROOT / "app" / "api" / "endpoints" / "__init__.py",
        "# app/api/endpoints/__init__.py\nfrom .assessment import router as assessment_router" # 导出路由
    ),
    "app/api/endpoints/assessment.py": create_python_file_content(PROJECT_ROOT / "app" / "api" / "endpoints" / "assessment.py",
        """# app/api/endpoints/assessment.py
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
    \"\"\"
    端点，用于发起新的开源项目评估。
    Orchestrator通常处理请求并协调Agent。
    \"\"\"
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
"""
    ),
    "app/api/schemas.py": create_python_file_content(PROJECT_ROOT / "app" / "api" / "schemas.py",
        """# app/api/schemas.py
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
"""
    ),

    # --- app/core/ ---
    "app/core/__init__.py": create_python_file_content(PROJECT_ROOT / "app" / "core" / "__init__.py",
        "# app/core/__init__.py"
    ),
    "app/core/orchestrator.py": create_python_file_content(PROJECT_ROOT / "app" / "core" / "orchestrator.py",
        """# app/core/orchestrator.py
# 高级任务编排器。接收初始请求，（可能通过TaskPlannerAgent）分解任务，
# 通过AgentRegistry向Agent/Agent群组分派任务/目标，并监控总体进展。

from typing import Dict, Any, Optional, Tuple, List
import uuid
# from .agent_registry import AgentRegistry, agent_registry # 假设全局或注入的注册中心
# from ..communication.protocols.mcp_schemas import Message, Performative, MessageContent # 示例MCP
# from ..agents.base_agent import BaseAgent # 用于类型提示

class Orchestrator:
    def __init__(self, registry): # 传入agent_registry实例
        self.agent_registry = registry # : AgentRegistry
        print("Orchestrator已初始化。")

    async def initiate_assessment_flow(self, user_query: str, project_url: Optional[str] = None) -> Tuple[str, str]:
        \"\"\"
        处理初始用户请求，规划并启动Agent协作流程。
        返回 (assessment_id, status_check_url)
        \"\"\"
        assessment_id = str(uuid.uuid4())
        print(f"Orchestrator: 收到请求 (ID: {assessment_id}) - 查询: '{user_query}', URL: '{project_url}'")

        # 1. 识别意图 (例如：调用IntentAgent)
        intent_agent = await self.agent_registry.find_agent_by_capability("intent_recognition")
        if not intent_agent:
            # 在实际应用中，这里应该记录错误并可能返回一个特定的错误响应
            raise Exception("IntentAgent未找到或不可用。")
        
        # 假设IntentAgent有一个方法叫 `determine_intent`
        # intent_payload = {"query": user_query, "project_url": project_url}
        # structured_intent = await intent_agent.execute_task(task_details=intent_payload) # 使用execute_task
        
        # 目前使用占位符
        structured_intent = {
            "action": "assess_project", 
            "project_identifier": project_url or user_query, # 更通用的标识符
            "requested_aspects": ["activity", "security", "license_compliance", "web_presence"] # 示例方面
        }
        if not structured_intent: # 或者检查structured_intent中是否有错误标记
            raise Exception("未能识别用户意图。")
        print(f"Orchestrator (ID: {assessment_id}): 意图已识别 - {structured_intent}")

        # 2. 规划任务 (例如：调用TaskPlannerAgent)
        task_planner_agent = await self.agent_registry.find_agent_by_capability("task_planning")
        if not task_planner_agent:
            raise Exception("TaskPlannerAgent未找到或不可用。")

        # task_plan_payload = structured_intent
        # planned_tasks_result = await task_planner_agent.execute_task(task_details=task_plan_payload)
        # tasks: List[Dict] = planned_tasks_result.get("tasks", [])
        
        # 目前使用占位符
        tasks: List[Dict] = []
        project_identifier = structured_intent["project_identifier"]
        
        if "activity" in structured_intent["requested_aspects"]:
            tasks.append({"id": str(uuid.uuid4()), "name": "Collect GitHub Commit Data", "type": "data_collection", "details": {"source": "github_commits", "project_identifier": project_identifier}, "assigned_to_capability": "data_retrieval_github"})
            tasks.append({"id": str(uuid.uuid4()), "name": "Assess Developer Activity", "type": "evaluation", "details": {"aspect": "activity", "data_task_ids": [tasks[-1]["id"]]}, "assigned_to_capability": "project_evaluation_activity"})
        
        if "web_presence" in structured_intent["requested_aspects"]:
             tasks.append({"id": str(uuid.uuid4()), "name": "Search Web for Project News", "type": "data_collection", "details": {"query": f"{project_identifier} news and discussions", "source": "web_search"}, "assigned_to_capability": "web_search"})
        
        # ... 可为其他方面添加更多任务 ...

        tasks.append({"id": str(uuid.uuid4()), "name": "Generate Final Report", "type": "report_generation", "details": {"all_task_ids": [t["id"] for t in tasks]}, "assigned_to_capability": "report_generation_service"})
        
        if not tasks:
            raise Exception("未能规划任务。")
        print(f"Orchestrator (ID: {assessment_id}): 任务已规划 - {len(tasks)}个任务: {tasks}")

        # TODO: 实际的任务分发、执行监控、结果聚合逻辑将更复杂
        # - 将assessment_id和tasks存储到持久化存储（例如，数据库）
        # - 异步启动任务执行（例如，通过消息总线或直接Agent调用，考虑任务依赖）
        # - 提供API端点以检查assessment_id的状态和获取结果

        status_url = f"/api/v1/assessment/{assessment_id}/status" # 示例
        print(f"Orchestrator (ID: {assessment_id}): 评估流程已启动。状态检查URL: {status_url}")
        return assessment_id, status_url
"""
    ),
    "app/core/agent_registry.py": create_python_file_content(PROJECT_ROOT / "app" / "core" / "agent_registry.py",
        """# app/core/agent_registry.py
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
        \"\"\"向注册中心注册Agent。\"\"\"
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
        \"\"\"注销Agent。\"\"\"
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
        \"\"\"通过ID查找Agent。\"\"\"
        agent_info = self._agents.get(agent_id)
        return agent_info["instance"] if agent_info else None # 简化：返回实例

    async def find_agents_by_capability(self, capability: str) -> List[Any]: # 返回Agent实例列表
        \"\"\"查找提供特定能力的所有Agent。\"\"\"
        agent_ids = self._capabilities.get(capability, [])
        return [self._agents[agent_id]["instance"] for agent_id in agent_ids if agent_id in self._agents]

    async def find_agent_by_capability(self, capability: str) -> Optional[Any]: # 返回单个Agent实例
        \"\"\"查找提供特定能力的第一个可用Agent（简单策略）。\"\"\"
        agents = await self.find_agents_by_capability(capability)
        return agents[0] if agents else None
        
    async def list_all_agents_info(self) -> Dict[str, Dict]:
        \"\"\"列出所有已注册Agent及其信息。\"\"\"
        return {
            agent_id: {
                "capabilities": [cap for cap, ids in self._capabilities.items() if agent_id in ids],
                "metadata": agent_data.get("metadata", {})
            }
            for agent_id, agent_data in self._agents.items()
        }

# 全局实例（简单方法，大型应用考虑依赖注入）
agent_registry = AgentRegistry() 
"""
    ),

    # --- app/agents/ ---
    "app/agents/__init__.py": create_python_file_content(PROJECT_ROOT / "app" / "agents" / "__init__.py",
        """# app/agents/__init__.py
# 此包包含所有专门的Agent实现。

# from .base_agent import BaseAgent
# from .intent_agent import IntentAgentImpl
# from .task_planner_agent import TaskPlannerAgentImpl
# from .data_agent import DataAgentImpl
# from .evaluation_agent import EvaluationAgentImpl
# from .report_agent import ReportAgentImpl

# 可能需要一个工厂或一种方法来自动发现和注册此包中定义的Agent。
"""
    ),
    "app/agents/base_agent.py": create_python_file_content(PROJECT_ROOT / "app" / "agents" / "base_agent.py",
        """# app/agents/base_agent.py
# 系统中所有Agent的抽象基类。
# 定义核心Agent行为、生命周期、通信接口(MCP)、能力描述及与AgentRegistry的交互。

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import uuid
from datetime import datetime

# from ..communication.protocols.mcp_schemas import Message, Performative # 示例MCP Schema
# from ..core.agent_registry import AgentRegistry # 用于类型提示

class BaseAgent(ABC):
    def __init__(self, agent_id: Optional[str] = None, agent_name: Optional[str] = None):
        self.agent_id: str = agent_id or f"{self.__class__.__name__}-{str(uuid.uuid4())[:8]}"
        self.agent_name: str = agent_name or self.__class__.__name__
        self.capabilities: List[str] = self._define_capabilities()
        # self.message_bus = None # 或其他通信处理器
        print(f"Agent {self.agent_id} ({self.agent_name}) 已初始化，能力：{self.capabilities}")

    @abstractmethod
    def _define_capabilities(self) -> List[str]:
        \"\"\"每个Agent必须定义其能力。\"\"\"
        pass

    async def register_self(self, registry): # 传入AgentRegistry实例
        \"\"\"向AgentRegistry注册Agent。\"\"\"
        # 在实际场景中，'self'可能是端点或代理对象
        metadata = {"name": self.agent_name, "registered_at": datetime.utcnow().isoformat()}
        await registry.register_agent(self.agent_id, self, self.capabilities, metadata)

    async def deregister_self(self, registry): # 传入AgentRegistry实例
        \"\"\"从AgentRegistry注销Agent。\"\"\"
        await registry.deregister_agent(self.agent_id)

    @abstractmethod
    async def handle_message(self, message: Any) -> Optional[Any]: # 'Message' 类型来自mcp_schemas
        \"\"\"
        根据MCP处理传入消息。
        这是A2A通信的主要入口点。
        \"\"\"
        pass

    async def send_message(self, recipient_agent_id: str, message_content: Any, performative: Any, # Performative类型
                           message_bus: Optional[Any] = None, registry: Optional[Any] = None, # MessageBus, AgentRegistry类型
                           conversation_id: Optional[str] = None, in_reply_to: Optional[str] = None):
        \"\"\"
        向另一个Agent发送消息，可能通过消息总线或直接调用。
        \"\"\"
        # from ..communication.protocols.mcp_schemas import Message # 延迟导入以避免循环
        # msg = Message(
        #     sender_id=self.agent_id,
        #     receiver_id=recipient_agent_id,
        #     performative=performative,
        #     content=message_content,
        #     conversation_id=conversation_id,
        #     in_reply_to=in_reply_to
        # )
        # print(f"Agent {self.agent_id} 尝试向 {recipient_agent_id} 发送消息: {msg.model_dump(exclude_none=True)}")
        # if message_bus:
        #     await message_bus.route_message_to_agent(recipient_agent_id, msg, registry)
        # elif registry: # 简单直接调用（仅限本地测试）
        #     recipient_agent = await registry.find_agent_by_id(recipient_agent_id)
        #     if recipient_agent:
        #         return await recipient_agent.handle_message(msg)
        #     else:
        #         print(f"错误：接收方Agent {recipient_agent_id} 未找到。")
        #         return None
        # else:
        #     print("错误：未提供MessageBus或AgentRegistry用于发送消息。")
        #     return None
        print(f"Agent {self.agent_id} 模拟向 {recipient_agent_id} 发送消息内容: {message_content}")
        return {"status": "message_sent_simulation_placeholder"}


    @abstractmethod
    async def execute_task(self, task_details: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        \"\"\"
        Agent执行其专业任务的核心逻辑。
        可能由Orchestrator或其他Agent调用。
        \"\"\"
        pass

    async def startup(self, registry): # 传入AgentRegistry实例
        \"\"\"Agent启动时调用（例如，在应用启动期间）。\"\"\"
        print(f"Agent {self.agent_id} 启动中...")
        await self.register_self(registry)

    async def shutdown(self, registry): # 传入AgentRegistry实例
        \"\"\"Agent关闭时调用。\"\"\"
        print(f"Agent {self.agent_id} 关闭中...")
        await self.deregister_self(registry)
"""
    ),
    # --- app/communication/ ---
    "app/communication/__init__.py": create_python_file_content(PROJECT_ROOT / "app" / "communication" / "__init__.py",
        "# app/communication/__init__.py\n# 处理Agent间通信协议和机制。"
    ),
    "app/communication/message_bus.py": create_python_file_content(PROJECT_ROOT / "app" / "communication" / "message_bus.py",
        """# app/communication/message_bus.py
# (可选) 实现用于异步Agent间通信的消息总线。
# 可使用Redis Pub/Sub, RabbitMQ, Kafka等技术，或用于本地开发的简单内存队列。

from typing import Dict, List, Callable, Any, Awaitable
# from ..core.agent_registry import AgentRegistry # 用于查找接收方Agent

class MessageBus: # 概念性占位符
    def __init__(self):
        # 初始化到总线技术的连接（如有）
        print("MessageBus已初始化 (内存概念占位符)。")
        # topic -> list of async handlers
        self._subscriptions: Dict[str, List[Callable[[Any], Awaitable[None]]]] = {} 

    async def publish(self, topic: str, message: Any): # Message类型来自mcp_schemas
        \"\"\"向主题发布消息。\"\"\"
        print(f"MessageBus: 向主题 '{topic}' 发布: {message}")
        if topic in self._subscriptions:
            for handler in self._subscriptions[topic]:
                await handler(message) # 假设handler是异步的

    async def subscribe(self, topic: str, handler: Callable[[Any], Awaitable[None]]): # Message类型
        \"\"\"将Agent的处理程序订阅到主题。\"\"\"
        self._subscriptions.setdefault(topic, [])
        if handler not in self._subscriptions[topic]: # 避免重复订阅
            self._subscriptions[topic].append(handler)
            print(f"MessageBus: 处理程序已订阅主题 '{topic}'。")

    async def route_message_to_agent(self, agent_id: str, message: Any, registry: Any): # Message类型, AgentRegistry类型
        \"\"\"将直接消息路由到特定Agent，可能通过其已知主题或直接收件箱。\"\"\"
        print(f"MessageBus: 尝试将消息路由到Agent '{agent_id}': {message}")
        target_agent = await registry.find_agent_by_id(agent_id)
        if target_agent and hasattr(target_agent, 'handle_message'):
            await target_agent.handle_message(message) # 直接调用Agent的处理方法
        else:
            print(f"MessageBus: Agent '{agent_id}' 未找到或没有handle_message方法。")

# 全局实例或注入
# message_bus = MessageBus()
"""
    ),
    "app/communication/protocols/__init__.py": create_python_file_content(PROJECT_ROOT / "app" / "communication" / "protocols" / "__init__.py",
        "# app/communication/protocols/__init__.py"
    ),
    "app/communication/protocols/mcp_schemas.py": create_python_file_content(PROJECT_ROOT / "app" / "communication" / "protocols" / "mcp_schemas.py",
        """# app/communication/protocols/mcp_schemas.py
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
"""
    ),

    # --- app/prompts/ ---
    "app/prompts/__init__.py": create_python_file_content(PROJECT_ROOT / "app" / "prompts" / "__init__.py",
        "# app/prompts/__init__.py"
    ),
    "app/prompts/prompt_manager.py": create_python_file_content(PROJECT_ROOT / "app" / "prompts" / "prompt_manager.py",
        """# app/prompts/prompt_manager.py
# 管理Jinja2提示词模板的加载和渲染，用于LLM交互。

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
from typing import Dict, Any
from ..config import settings # 导入配置以获取模板目录

class PromptManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(PromptManager, cls).__new__(cls)
            # 初始化只执行一次
            template_folder_path = Path(settings.PROMPT_TEMPLATE_DIR)
            if not template_folder_path.is_dir():
                # 尝试相对于当前文件创建（如果配置路径无效）
                # 这更像是一个回退，理想情况下配置路径应该是正确的
                alt_path = Path(__file__).resolve().parent / "templates"
                if alt_path.is_dir():
                    template_folder_path = alt_path
                    print(f"警告：配置的模板目录 '{settings.PROMPT_TEMPLATE_DIR}' 未找到。回退到 '{alt_path}'。")
                else:
                    # 如果回退路径也不存在，则创建它
                    alt_path.mkdir(parents=True, exist_ok=True)
                    template_folder_path = alt_path
                    print(f"警告：模板目录 '{settings.PROMPT_TEMPLATE_DIR}' 和 '{alt_path}' 均未找到。已创建 '{alt_path}'。请添加模板。")
            
            cls._instance.env = Environment(
                loader=FileSystemLoader(template_folder_path),
                autoescape=select_autoescape(['html', 'xml', 'md']), # 如果不需要，请小心使用自动转义
                trim_blocks=True,
                lstrip_blocks=True
            )
            print(f"PromptManager已初始化，模板文件夹：{template_folder_path}")
        return cls._instance

    def load_and_render(self, template_name: str, context: Dict[str, Any]) -> str:
        \"\"\"加载指定的提示词模板并使用给定的上下文进行渲染。\"\"\"
        try:
            template = self.env.get_template(template_name)
            return template.render(context)
        except Exception as e:
            print(f"加载/渲染模板 {template_name} 时出错：{e}")
            # 回退或引发错误
            return f"错误：无法渲染提示词模板 '{template_name}'。详情：{e}"

# 单例实例
prompt_manager = PromptManager()

# 示例用法：
# if __name__ == "__main__":
#     # 确保settings.PROMPT_TEMPLATE_DIR指向一个有效的、包含模板的目录
#     # 例如，手动创建 app/prompts/templates/intent_agent.md
#     # Path(settings.PROMPT_TEMPLATE_DIR).mkdir(parents=True, exist_ok=True)
#     # with open(Path(settings.PROMPT_TEMPLATE_DIR) / "intent_agent.md", "w") as f:
#     #     f.write("User query: {{ user_query }}")
#
#     rendered_prompt = prompt_manager.load_and_render(
#         "intent_agent.md", 
#         {"user_query": "分析此项目。", "project_url": "http://..."}
#     )
#     print(rendered_prompt)
"""
    ),
    "app/prompts/templates/__init__.py": "", # 通常为空或对于非代码目录不需要
    "app/prompts/templates/evaluation_agent/__init__.py": "",
    "app/prompts/templates/evaluation_agent/developer_activity.md": """
### 开发者活动评估提示词模板

**目标**: 基于提供的项目数据，评估开发者的活动水平。

**上下文变量 (Jinja2示例)**:
- 项目名称: `{{ project_name }}`
- Commit历史摘要 (例如，近3个月): 
  `{{ commit_summary }}` 
- Issue跟踪统计 (例如，新增、已关闭、未解决):
  `{{ issue_stats }}`
- 贡献者数量: `{{ contributor_count }}`

**指令**:
1. 分析提供的关于项目 '{{ project_name }}' 的数据。
2. 综合考虑Commit频率、活跃贡献者数量、Issue解决率以及近期的活动趋势。
3. 给出一个定性的活动水平评估 (例如：高、中、低、停滞)。
4. 提供简要的评估理由，并引用具体数据点。
5. 您的输出应严格遵循以下JSON格式。

**输出格式 (JSON)**:
```json
{% raw %}
{
  "project_name": "{{ project_name }}",
  "evaluation_aspect": "developer_activity",
  "activity_level": "评估结果 (例如：中)",
  "justification": "基于数据的简要理由。",
  "supporting_data_points": {
    "commit_frequency_assessment": "...",
    "contributor_engagement": "...",
    "issue_resolution_rate_assessment": "..."
  }
}
{% endraw %}
```
""",

    # --- app/knowledge_base/ ---
    "app/knowledge_base/__init__.py": create_python_file_content(PROJECT_ROOT / "app" / "knowledge_base" / "__init__.py", "# app/knowledge_base/__init__.py"),
    "app/knowledge_base/retriever.py": create_python_file_content(PROJECT_ROOT / "app" / "knowledge_base" / "retriever.py",
        """# app/knowledge_base/retriever.py
# 统一的检索接口，用于访问各种知识源。
# 将请求分派给特定的连接器、向量存储、图存储或Web搜索。

from typing import Any, Dict, List, Optional
# from .connectors.base_connector import BaseConnector
# from .vector_store.faiss_client import FaissClient # 示例
# from .graph_store.neo4j_client import Neo4jClient # 示例
# from .connectors.web_search_connector import WebSearchConnectorImpl # 示例

class KnowledgeBaseRetriever:
    def __init__(self, 
                 connectors: Optional[Dict[str, Any]] = None, 
                 vector_store: Optional[Any] = None, 
                 graph_store: Optional[Any] = None, 
                 web_search_connector: Optional[Any] = None):
        self.connectors = connectors or {} # 例如：{"github": GithubConnectorImpl(), "osv": OSVConnectorImpl()}
        self.vector_store = vector_store
        self.graph_store = graph_store
        self.web_search_connector = web_search_connector
        print("KnowledgeBaseRetriever已初始化。")

    async def retrieve_data(self, source_type: str, query: Any, params: Optional[Dict] = None) -> Any:
        \"\"\"
        从指定的源类型检索数据。
        'source_type' 可以是 'github_api', 'vector_search', 'graph_query', 'web_search'等。
        'query' 是主要的查询字符串或对象。
        'params' 是检索的附加参数。
        \"\"\"
        params = params or {}
        print(f"Retriever: 收到对源 '{source_type}' 的请求，查询 '{str(query)[:100]}...'")

        if source_type == "web_search" and self.web_search_connector:
            return await self.web_search_connector.fetch_data(query, params=params)
        elif source_type == "vector_search" and self.vector_store:
            # query 应该是嵌入向量或待嵌入的文本
            # return await self.vector_store.search(query_embedding=query, top_k=params.get("top_k", 5))
             return f"模拟向量搜索结果：{query}"
        elif source_type == "graph_query" and self.graph_store:
            # query 应该是Cypher查询字符串
            return await self.graph_store.execute_query(query, parameters=params)
        elif source_type in self.connectors:
            connector = self.connectors[source_type]
            # 假设连接器有 'fetch_data' 或类似方法
            return await connector.fetch_data(query, params=params) 
        else:
            print(f"错误：未知的源类型 '{source_type}' 或连接器未配置。")
            return {"error": f"未知源类型 '{source_type}' 或连接器未配置。"}

# 示例实例化 (通常在DataAgent或中央服务设置中)
# from .connectors.github_connector import GithubConnectorImpl
# from .connectors.web_search_connector import WebSearchConnectorImpl
# from .vector_store.faiss_client import FaissClient
# from .graph_store.neo4j_client import Neo4jClient
# from ...config import settings
#
# gh_connector = GithubConnectorImpl(api_key=settings.GITHUB_TOKEN)
# web_searcher = WebSearchConnectorImpl(api_key=settings.SEARCH_ENGINE_API_KEY, cx=settings.SEARCH_ENGINE_CX)
# faiss_db = FaissClient(index_path=settings.FAISS_INDEX_PATH, embedding_model_name=settings.EMBEDDING_MODEL_NAME)
# neo4j_db = Neo4jClient(uri=settings.NEO4J_URI, user=settings.NEO4J_USER, password=settings.NEO4J_PASSWORD)
#
# knowledge_retriever = KnowledgeBaseRetriever(
#     connectors={"github": gh_connector, /* ...其他连接器... */},
#     vector_store=faiss_db,
#     graph_store=neo4j_db,
#     web_search_connector=web_searcher
# )
"""
    ),
    "app/knowledge_base/connectors/__init__.py": create_python_file_content(PROJECT_ROOT / "app" / "knowledge_base" / "connectors" / "__init__.py",
        """# app/knowledge_base/connectors/__init__.py
# from .base_connector import BaseConnector
# from .github_connector import GithubConnectorImpl
# from .gitee_connector import GiteeConnectorImpl
# from .osv_connector import OsvConnectorImpl
# from .web_search_connector import WebSearchConnectorImpl
"""
    ),
    "app/knowledge_base/connectors/base_connector.py": create_python_file_content(PROJECT_ROOT / "app" / "knowledge_base" / "connectors" / "base_connector.py",
        """# app/knowledge_base/connectors/base_connector.py
# 所有数据源连接器的抽象基类。

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class BaseConnector(ABC):
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        print(f"{self.__class__.__name__} 已初始化。")

    @abstractmethod
    async def connect(self):
        \"\"\"如果需要，建立到数据源的连接。\"\"\"
        pass

    @abstractmethod
    async def disconnect(self):
        \"\"\"如果需要，关闭到数据源的连接。\"\"\"
        pass

    @abstractmethod
    async def fetch_data(self, query: Any, params: Optional[Dict] = None) -> Any:
        \"\"\"根据查询和参数从源获取数据。\"\"\"
        pass

    async def test_connection(self) -> bool:
        \"\"\"测试到数据源的连接是否正常。\"\"\"
        # 默认实现，如果需要特定测试则覆盖
        try:
            await self.connect()
            # 如果可能，执行简单的读取或状态检查
            await self.disconnect()
            return True
        except Exception as e:
            print(f"{self.__class__.__name__} 的连接测试失败：{e}")
            return False
"""
    ),
    "app/knowledge_base/vector_store/__init__.py": create_python_file_content(PROJECT_ROOT / "app" / "knowledge_base" / "vector_store" / "__init__.py",
        "# app/knowledge_base/vector_store/__init__.py\n# from .faiss_client import FaissClient"
    ),
    "app/knowledge_base/vector_store/faiss_client.py": create_python_file_content(PROJECT_ROOT / "app" / "knowledge_base" / "vector_store" / "faiss_client.py",
        """# app/knowledge_base/vector_store/faiss_client.py
# 与FAISS向量索引交互的客户端。
# 处理嵌入生成（或假设预计算的嵌入）、索引加载和相似性搜索。

import faiss # type: ignore
import numpy as np
from typing import List, Tuple, Optional, Union
from pathlib import Path
# from sentence_transformers import SentenceTransformer # 嵌入生成示例
# from ...config import settings # 用于配置

class FaissClient:
    def __init__(self, index_path: str, embedding_model_name: Optional[str] = None, dimension: Optional[int] = None):
        self.index_file_path = Path(index_path)
        self.index: Optional[faiss.Index] = None
        self.embedding_model = None
        self._dimension = dimension

        if embedding_model_name:
            # try:
            #     self.embedding_model = SentenceTransformer(embedding_model_name)
            #     self._dimension = self.embedding_model.get_sentence_embedding_dimension()
            #     print(f"SentenceTransformer模型 '{embedding_model_name}' 已加载，维度：{self._dimension}")
            # except Exception as e:
            #     print(f"加载SentenceTransformer模型 '{embedding_model_name}' 失败：{e}。请确保模型已安装。")
            #     # 如果模型加载失败但维度已提供，则继续；否则可能无法创建索引。
            #     if not self._dimension:
            #         print("错误：嵌入模型加载失败且未提供维度。FaissClient可能无法正常工作。")
            pass # 占位：实际应加载模型或确保维度已知

        if not self._dimension: # 如果模型未加载且未提供维度，则设置一个默认值或引发错误
            self._dimension = 384 # 示例：all-MiniLM-L6-v2的维度
            print(f"警告：未指定嵌入维度，使用默认值：{self._dimension}。这可能与您的数据不匹配。")

        self._load_or_create_index()
        print(f"FaissClient已初始化。索引路径：{self.index_file_path}, 维度：{self._dimension}")

    def _load_or_create_index(self):
        if self.index_file_path.exists():
            try:
                self.index = faiss.read_index(str(self.index_file_path))
                print(f"FAISS索引已从 {self.index_file_path} 加载。索引大小：{self.index.ntotal if self.index else 0}")
                if self.index and self._dimension and self.index.d != self._dimension:
                    print(f"警告：索引维度 ({self.index.d}) 与模型/配置维度 ({self._dimension}) 不同。可能导致问题。")
                    # 可以选择重建索引或引发错误
            except Exception as e:
                print(f"加载FAISS索引时出错：{e}。如果维度已知，将在首次添加时创建新索引。")
                self.index = None # 确保如果加载失败，索引为None
        else:
            print(f"在 {self.index_file_path} 未找到FAISS索引文件。如果维度已知，将在首次添加时创建。")
        
        if not self.index and self._dimension:
            # 如果无法加载但维度已知，则创建新索引
            self.index = faiss.IndexFlatL2(self._dimension) # 示例：L2距离索引
            print(f"已创建新的空FAISS IndexFlatL2，维度 {self._dimension}。")

    async def get_embedding(self, text: Union[str, List[str]]) -> Optional[np.ndarray]:
        if not self.embedding_model:
            print("错误：嵌入模型未加载。无法生成嵌入。")
            return None
        # try:
        #     # SentenceTransformer的encode方法是同步的，如果用于异步代码，应考虑在线程池中运行
        #     # import asyncio
        #     # loop = asyncio.get_running_loop()
        #     # embeddings = await loop.run_in_executor(None, self.embedding_model.encode, text)
        #     # return np.array(embeddings)
        #     return np.array(self.embedding_model.encode(text)) # 简单同步调用
        # except Exception as e:
        #     print(f"生成嵌入时出错：{e}")
        #     return None
        print(f"模拟为 '{text}' 生成嵌入。") # 占位
        return np.random.rand(1 if isinstance(text, str) else len(text), self._dimension).astype(np.float32)


    async def add_texts(self, texts: List[str], text_ids: Optional[List[Any]] = None): # text_ids用于元数据存储
        if not self.embedding_model:
            print("无法添加文本：嵌入模型未加载。")
            return
        embeddings = await self.get_embedding(texts)
        if embeddings is not None:
            # TODO: 实现元数据存储以将text_ids与FAISS内部索引关联起来
            # 对于IndexFlatL2，FAISS索引是连续的。需要外部映射。
            self.add_embeddings(embeddings) # 简单添加，不处理ID映射
            print(f"已为 {len(texts)} 个文本添加嵌入。元数据ID（如果提供）需要外部管理。")

    def add_embeddings(self, embeddings: np.ndarray):
        if not self.index:
            if self._dimension and embeddings.shape[1] == self._dimension:
                self.index = faiss.IndexFlatL2(self._dimension)
                print("在add_embeddings期间因缺少索引而初始化了新的FAISS索引。")
            else:
                raise ValueError("FAISS索引未初始化且维度不匹配或嵌入形状不正确。")

        if embeddings.shape[1] != self.index.d:
            raise ValueError(f"嵌入维度 ({embeddings.shape[1]}) 与索引维度 ({self.index.d}) 不匹配。")
        
        self.index.add(embeddings.astype(np.float32))
        print(f"已向FAISS索引添加 {embeddings.shape[0]} 个嵌入。总数：{self.index.ntotal}")

    async def search_by_text(self, query_text: str, top_k: int = 5) -> Tuple[Optional[np.ndarray], Optional[np.ndarray]]:
        if not self.embedding_model:
            print("无法按文本搜索：嵌入模型未加载。")
            return None, None
        query_embedding = await self.get_embedding(query_text)
        if query_embedding is not None:
            return self.search_by_embedding(query_embedding, top_k)
        return None, None

    def search_by_embedding(self, query_embedding: np.ndarray, top_k: int = 5) -> Tuple[Optional[np.ndarray], Optional[np.ndarray]]:
        if not self.index or self.index.ntotal == 0:
            print("FAISS索引未加载或为空。")
            return np.array([]), np.array([])
        if query_embedding.ndim == 1:
            query_embedding = np.expand_dims(query_embedding, axis=0).astype(np.float32)
        elif query_embedding.ndim == 2:
            query_embedding = query_embedding.astype(np.float32)
        else:
            raise ValueError("查询嵌入必须是1D或2D NumPy数组。")

        if query_embedding.shape[1] != self.index.d:
            raise ValueError(f"查询嵌入维度 ({query_embedding.shape[1]}) 与索引维度 ({self.index.d}) 不匹配。")
        
        distances, indices = self.index.search(query_embedding, top_k)
        return distances, indices # 最近邻的距离和索引

    def save_index(self):
        if self.index:
            self.index_file_path.parent.mkdir(parents=True, exist_ok=True)
            faiss.write_index(self.index, str(self.index_file_path))
            print(f"FAISS索引已保存到 {self.index_file_path}")
        else:
            print("无法保存：FAISS索引未初始化。")
"""
    ),
    "app/knowledge_base/graph_store/__init__.py": create_python_file_content(PROJECT_ROOT / "app" / "knowledge_base" / "graph_store" / "__init__.py",
        "# app/knowledge_base/graph_store/__init__.py\n# from .neo4j_client import Neo4jClient\n# from .graph_utils import ..."
    ),
    "app/knowledge_base/graph_store/neo4j_client.py": create_python_file_content(PROJECT_ROOT / "app" / "knowledge_base" / "graph_store" / "neo4j_client.py",
        """# app/knowledge_base/graph_store/neo4j_client.py
# 与Neo4j图数据库交互的客户端。

from neo4j import AsyncGraphDatabase # FastAPI使用AsyncGraphDatabase
from typing import Dict, List, Any, Optional
# from ...config import settings # 用于配置

class Neo4jClient:
    _driver: Optional[AsyncGraphDatabase.driver] = None # 类级别驱动程序以实现共享

    def __init__(self, uri: str, user: str, password: str):
        self._uri = uri
        self._auth = (user, password)
        # 驱动程序将在首次需要时惰性初始化
        print(f"Neo4jClient已为URI配置：{uri}")

    async def _get_driver(self) -> AsyncGraphDatabase.driver:
        if Neo4jClient._driver is None or Neo4jClient._driver.closed():
            try:
                Neo4jClient._driver = AsyncGraphDatabase.driver(self._uri, auth=self._auth)
                await Neo4jClient._driver.verify_connectivity() # 确保连接有效
                print("Neo4j异步驱动程序已连接并验证。")
            except Exception as e:
                print(f"连接到Neo4j异步驱动程序失败：{e}")
                Neo4jClient._driver = None # 连接失败时重置驱动程序
                raise # 重新引发异常以表示连接失败
        return Neo4jClient._driver

    async def close_driver(self): # 类方法，在应用关闭时调用
        if Neo4jClient._driver and not Neo4jClient._driver.closed():
            await Neo4jClient._driver.close()
            Neo4jClient._driver = None
            print("Neo4j异步驱动程序已关闭。")

    async def execute_query(self, query: str, parameters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        \"\"\"执行Cypher查询并返回结果。\"\"\"
        driver = await self._get_driver()
        if not driver:
            return [{"error": "Neo4j连接不可用。"}]
            
        records_data: List[Dict[str, Any]] = []
        query_summary = None
        try:
            # Neo4j建议对异步操作使用异步会话
            async with driver.session() as session:
                results = await session.run(query, parameters)
                # 异步处理记录
                records_data = [record.data() async for record in results] 
                query_summary = await results.consume() # 消耗流的其余部分并获取摘要
        except Exception as e:
            print(f"执行Neo4j查询时出错：{query} | 参数：{parameters} | 错误：{e}")
            return [{"error": str(e)}] # 返回错误信息
        
        print(f"查询已执行。Cypher：'{query[:70]}...', 参数：{parameters}。"
              f"返回 {len(records_data)} 条记录。摘要计数器：{query_summary.counters if query_summary else 'N/A'}")
        return records_data

    async def execute_write_query(self, query: str, parameters: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, int]]:
        \"\"\"执行写查询并返回操作计数器。\"\"\"
        driver = await self._get_driver()
        if not driver:
            return {"error": "Neo4j连接不可用。"}

        try:
            async with driver.session() as session:
                # 使用事务函数执行写操作
                summary = await session.write_transaction(self._run_write_transaction_fn, query, parameters)
            print(f"写查询已执行。摘要计数器：{summary.counters if summary else 'N/A'}")
            return summary.counters if summary else None # 例如：nodes_created, relationships_created
        except Exception as e:
            print(f"执行Neo4j写查询时出错：{e}")
            return {"error": str(e)}

    @staticmethod
    async def _run_write_transaction_fn(tx, query, parameters): # 事务函数必须是静态的或在类外部
        result = await tx.run(query, parameters)
        summary = await result.consume() # 在事务中消耗结果很重要
        return summary

# 示例用法 (通常在应用启动/关闭时管理驱动程序生命周期)
# from ...config import settings
# neo4j_client_instance = Neo4jClient(uri=settings.NEO4J_URI, user=settings.NEO4J_USER, password=settings.NEO4J_PASSWORD)
#
# async def example_neo4j_usage():
#     try:
#         results = await neo4j_client_instance.execute_query("MATCH (n) RETURN count(n) AS node_count")
#         print("节点计数:", results)
#     finally:
#         # 通常在应用关闭时调用
#         # await neo4j_client_instance.close_driver() 
#         pass 
"""
    ),
    "app/knowledge_base/graph_store/graph_utils.py": create_python_file_content(PROJECT_ROOT / "app" / "knowledge_base" / "graph_store" / "graph_utils.py",
        """# app/knowledge_base/graph_store/graph_utils.py
# 主要使用NetworkX处理图数据的实用程序。
# 包括图创建、操作、分析和序列化/反序列化功能。

import networkx as nx
from typing import List, Dict, Any, Tuple, Optional, Union
from pathlib import Path

def create_graph_from_edges(edges: List[Tuple[Any, Any, Optional[Dict]]], directed: bool = False) -> Union[nx.Graph, nx.DiGraph]:
    \"\"\"从边列表创建NetworkX图。边可以具有属性。\"\"\"
    G = nx.DiGraph() if directed else nx.Graph()
    for edge in edges:
        u, v, *attrs = edge
        attr_dict = attrs[0] if attrs else {}
        G.add_edge(u, v, **attr_dict)
    print(f"已创建图，包含 {G.number_of_nodes()} 个节点和 {G.number_of_edges()} 条边。")
    return G

def add_nodes_with_attributes(G: Union[nx.Graph, nx.DiGraph], nodes_data: List[Tuple[Any, Dict]]):
    \"\"\"向图中的节点添加节点及其属性。\"\"\"
    for node, attrs in nodes_data:
        G.add_node(node, **attrs)
    print(f"已添加/更新 {len(nodes_data)} 个节点的属性。")


def graph_to_graphml(G: Union[nx.Graph, nx.DiGraph], filepath: Union[str, Path]) -> None:
    \"\"\"将NetworkX图序列化为GraphML格式。\"\"\"
    path_obj = Path(filepath)
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    nx.write_graphml(G, str(path_obj)) # write_graphml需要字符串路径
    print(f"图已保存到GraphML：{path_obj}")

def graphml_to_graph(filepath: Union[str, Path]) -> Optional[Union[nx.Graph, nx.DiGraph]]:
    \"\"\"从GraphML格式反序列化NetworkX图。\"\"\"
    path_obj = Path(filepath)
    if path_obj.exists():
        G = nx.read_graphml(str(path_obj))
        print(f"图已从GraphML加载：{path_obj}。节点：{G.number_of_nodes()}，边：{G.number_of_edges()}")
        return G
    else:
        print(f"GraphML文件未找到：{path_obj}")
        return None

def get_basic_graph_metrics(G: Union[nx.Graph, nx.DiGraph]) -> Dict[str, Any]:
    \"\"\"计算图的一些基本指标。\"\"\"
    if not G: return {}
    num_nodes = G.number_of_nodes()
    metrics = {
        "num_nodes": num_nodes,
        "num_edges": G.number_of_edges(),
        "density": nx.density(G)
    }
    if num_nodes > 0:
        if isinstance(G, nx.Graph): # 无向图指标
            metrics["is_connected"] = nx.is_connected(G)
            # metrics["average_clustering_coefficient"] = nx.average_clustering(G)
        elif isinstance(G, nx.DiGraph): # 有向图指标
            metrics["is_strongly_connected"] = nx.is_strongly_connected(G)
            metrics["is_weakly_connected"] = nx.is_weakly_connected(G)
        
        # degrees = [val for (node, val) in G.degree()]
        # metrics["average_degree"] = sum(degrees) / num_nodes if num_nodes > 0 else 0
    print(f"已计算基本图指标：{metrics}")
    return metrics
"""
    ),

    # --- app/evaluation/ ---
    "app/evaluation/__init__.py": create_python_file_content(PROJECT_ROOT / "app" / "evaluation" / "__init__.py",
        "# app/evaluation/__init__.py\n# from .metrics import ..."
    ),
    "app/evaluation/metrics.py": create_python_file_content(PROJECT_ROOT / "app" / "evaluation" / "metrics.py",
        """# app/evaluation/metrics.py
# 定义特定的评估指标及其计算逻辑。
# 这些函数通常由EvaluationAgent调用。

from typing import Dict, Any, List, Optional

def calculate_developer_activity(commit_data: Optional[List[Dict]], issue_data: Optional[List[Dict]]) -> Dict[str, Any]:
    \"\"\"
    计算开发者活动指标。
    示例：提交频率、活跃贡献者、Issue解决率。
    \"\"\"
    commit_data = commit_data or []
    issue_data = issue_data or []
    
    num_commits = len(commit_data)
    active_developers = len(set(c.get('author_login', c.get('author', {}).get('login')) 
                                for c in commit_data if c.get('author_login') or c.get('author')))
    
    # 占位符逻辑
    score = 0.0
    if num_commits > 100 and active_developers > 5: score = 0.9
    elif num_commits > 50 or active_developers > 2: score = 0.6
    elif num_commits > 10: score = 0.3
    
    return {
        "metric_name": "developer_activity",
        "score": round(score, 2), # 标准化分数 (0.0 到 1.0)
        "details": {
            "total_commits_analyzed": num_commits,
            "active_contributors_identified": active_developers,
            "comment": "基于近期提交历史和贡献者数量的初步评估。"
        }
    }

def check_license_compliance(license_info: Optional[Dict], project_type: str = "generic") -> Dict[str, Any]:
    \"\"\"
    根据检测到的许可证和项目上下文检查许可证合规性。
    可能涉及对照批准/有问题的许可证列表进行检查。
    \"\"\"
    license_info = license_info or {}
    license_name = license_info.get("name", "Unknown")
    spdx_id = license_info.get("spdx_id", "N/A")
    is_compliant = True # 默认合规
    compliance_notes = "许可证信息初步评估。"

    if license_name == "Unknown" or spdx_id == "N/A":
        is_compliant = False # 或标记为 " undetermined "
        compliance_notes = "未能确定许可证或不是标准的OSI批准许可证。"
    elif "GPL" in license_name and project_type == "proprietary_linking_critical": # 示例特定上下文
        is_compliant = False
        compliance_notes = f"{license_name} 许可证可能具有严格的copyleft影响，与项目类型不兼容。"
    # 此处可添加更多特定许可证规则

    return {
        "metric_name": "license_compliance",
        "is_compliant": is_compliant, # True, False, 或 "undetermined"
        "details": {
            "detected_license_name": license_name,
            "spdx_id": spdx_id,
            "notes": compliance_notes
        }
    }

def score_vulnerability_assessment(vulnerabilities: Optional[List[Dict]]) -> Dict[str, Any]:
    \"\"\"
    根据已识别的漏洞（例如，来自OSV）对项目进行评分。
    考虑漏洞的严重性和数量。
    \"\"\"
    vulnerabilities = vulnerabilities or []
    severity_counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0, "UNKNOWN": 0}

    for vuln in vulnerabilities:
        severity = str(vuln.get("severity", "UNKNOWN")).upper() # 确保是大写且为字符串
        if severity in severity_counts:
            severity_counts[severity] += 1
        else: # 处理不在预期列表中的严重性级别
            severity_counts["UNKNOWN"] += 1
            
    # 简单评分：分数越低越好（这里我们返回风险等级或计数）
    risk_score = 0.0 # 0-1, 1表示风险高
    if severity_counts["CRITICAL"] > 0: risk_score = 1.0
    elif severity_counts["HIGH"] > 0: risk_score = 0.8 - (0.05 * min(severity_counts["HIGH"], 4)) # 递减影响
    elif severity_counts["MEDIUM"] > 0: risk_score = 0.5 - (0.05 * min(severity_counts["MEDIUM"], 6))
    elif severity_counts["LOW"] > 0: risk_score = 0.2
    
    risk_score = round(max(0.0, min(1.0, risk_score)), 2)


    return {
        "metric_name": "vulnerability_risk",
        "risk_score": risk_score, # 0.0 (低风险) 到 1.0 (高风险)
        "details": {
            "severity_counts": severity_counts,
            "total_vulnerabilities_found": len(vulnerabilities)
        }
    }
"""
    ),

    # --- app/reporting/ ---
    "app/reporting/__init__.py": create_python_file_content(PROJECT_ROOT / "app" / "reporting" / "__init__.py",
        "# app/reporting/__init__.py\n# from .generator import ReportGenerator\n# from .visualizations import ..."
    ),
    "app/reporting/generator.py": create_python_file_content(PROJECT_ROOT / "app" / "reporting" / "generator.py",
        """# app/reporting/generator.py
# 从评估结果和可视化生成结构化报告（JSON、Markdown，未来可能支持PDF/HTML）。

import json
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone
import uuid # 确保导入uuid
# from .visualizations import generate_activity_plot # 示例
# from ..config import settings # 用于报告路径

class ReportGenerator:
    def __init__(self):
        print("ReportGenerator已初始化。")

    def generate_json_report_data(self, assessment_id: str, project_name: str, 
                                  evaluation_metrics: Dict[str, Any], 
                                  detailed_findings: Optional[List[Dict]] = None,
                                  llm_summary: Optional[str] = None,
                                  plot_paths: Optional[Dict[str, str]] = None
                                 ) -> Dict[str, Any]:
        \"\"\"生成JSON报告数据结构。\"\"\"
        report_data = {
            "report_id": str(uuid.uuid4()), # 为报告本身生成ID
            "assessment_id": assessment_id,
            "project_name": project_name,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "overall_summary_llm": llm_summary,
            "evaluation_metrics": evaluation_metrics,
            "detailed_findings": detailed_findings or [],
            "visualization_paths": plot_paths or {} # 存储已保存绘图的路径
        }
        return report_data

    def render_markdown_report(self, report_data: Dict[str, Any]) -> str:
        \"\"\"从JSON数据渲染Markdown报告。\"\"\"
        md_report = f"# {report_data.get('project_name', 'N/A')} 项目评估报告\\n\\n"
        md_report += f"**报告ID:** {report_data.get('report_id')}\\n"
        md_report += f"**评估ID:** {report_data.get('assessment_id')}\\n"
        md_report += f"**生成日期:** {report_data.get('generated_at')}\\n\\n"

        if report_data.get('overall_summary_llm'):
            md_report += f"## 总体摘要 (由LLM生成)\\n"
            md_report += f"{report_data['overall_summary_llm']}\\n\\n"

        md_report += f"## 评估指标\\n"
        metrics = report_data.get('evaluation_metrics', {})
        if metrics:
            for metric_name, metric_value_obj in metrics.items():
                md_report += f"### {metric_name.replace('_', ' ').title()}\\n"
                if isinstance(metric_value_obj, dict):
                    for key, val in metric_value_obj.items():
                        if key == "metric_name": continue # 已在标题中
                        md_report += f"- **{key.replace('_', ' ').title()}**: {val}\\n"
                else: # 直接值
                    md_report += f"- {metric_value_obj}\\n"
                md_report += "\\n"
        else:
            md_report += "无可用指标。\\n"
        md_report += "\\n"
        
        findings = report_data.get('detailed_findings', [])
        if findings:
            md_report += f"## 详细发现\\n"
            for finding in findings:
                md_report += f"- {finding.get('description', '无描述')}"
                if finding.get('severity'): md_report += f" (严重性: {finding['severity']})"
                md_report += "\\n"
            md_report += "\\n"

        plot_paths = report_data.get('visualization_paths', {})
        if plot_paths:
            md_report += f"## 可视化\\n"
            for viz_name, viz_path in plot_paths.items():
                md_report += f"### {viz_name.replace('_', ' ').title()}\\n"
                # 假设路径是相对的或Web可访问的
                md_report += f"![{viz_name}]({viz_path})\\n\\n" 
        return md_report

# 示例用法：
# if __name__ == "__main__":
#     import uuid # 需要导入
#     generator = ReportGenerator()
#     dummy_metrics = {
#         "developer_activity": {"metric_name":"developer_activity", "score": 0.7, "details": {"commits": 150}},
#         "license_compliance": {"metric_name":"license_compliance", "is_compliant": True, "details": {"detected_license_name": "MIT"}}
#     }
#     dummy_plot_paths = {"activity_trend": "plots/activity_trend_sample.png"} # 确保此路径存在或可访问
#     llm_summary_text = "此项目显示出良好的开发者活动，并且许可证合规。"
#
#     report_content = generator.generate_json_report_data(
#         assessment_id="test_assessment_123",
#         project_name="SampleProjectX",
#         evaluation_metrics=dummy_metrics,
#         llm_summary=llm_summary_text,
#         plot_paths=dummy_plot_paths
#     )
#     print("--- JSON Report Data ---")
#     print(json.dumps(report_content, indent=2))
#
#     md_output = generator.render_markdown_report(report_content)
#     print("\\n--- Markdown Report ---")
#     print(md_output)
#
#     # 保存到文件
#     # report_file_path = Path(settings.REPORTS_DIR) / f"{report_content['report_id']}.md"
#     # report_file_path.parent.mkdir(parents=True, exist_ok=True)
#     # with open(report_file_path, "w", encoding="utf-8") as f:
#     #    f.write(md_output)
#     # print(f"\\nMarkdown报告已保存到：{report_file_path}")
"""
    ),
    "app/reporting/visualizations.py": create_python_file_content(PROJECT_ROOT / "app" / "reporting" / "visualizations.py",
        """# app/reporting/visualizations.py
# 用于使用Matplotlib/Seaborn为报告生成绘图和图表的函数。
# 这些函数通常将pandas DataFrame或结构化数据作为输入。

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path
from typing import Dict, List, Any, Optional
from ..config import settings # 用于绘图目录
from datetime import datetime # 确保导入datetime

# 确保绘图保存到目录
PLOTS_OUTPUT_DIR = Path(settings.PLOTS_DIR) # 从配置获取

def generate_activity_plot(activity_data: List[Dict[str, Any]], filename_prefix: str = "activity") -> Optional[str]:
    \"\"\"
    为开发者活动趋势（例如，随时间变化的提交）生成绘图。
    保存绘图并返回其路径。
    'activity_data' 应为字典列表，例如：[{'date': '2023-01-01', 'commits': 10}, ...]
    \"\"\"
    if not activity_data:
        print("未提供用于绘图的活动数据。")
        return None

    try:
        df = pd.DataFrame(activity_data)
        if 'date' not in df.columns or ('commits' not in df.columns and 'count' not in df.columns) : # 允许 'count' 作为备用
            print("绘图的活动数据必须包含 'date' 和 'commits' (或 'count') 列。")
            return None
            
        value_col = 'commits' if 'commits' in df.columns else 'count'
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')

        plt.figure(figsize=(10, 6))
        sns.lineplot(x='date', y=value_col, data=df, marker='o', estimator=sum) # 如果日期有重复，则求和
        plt.title('开发者提交随时间变化趋势')
        plt.xlabel('日期')
        plt.ylabel(f'{value_col.title()}数量')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        PLOTS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True) # 确保目录存在
        output_filename = f"{filename_prefix}_trend_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        output_path = PLOTS_OUTPUT_DIR / output_filename
        plt.savefig(output_path)
        plt.close() # 关闭绘图以释放内存
        print(f"活动绘图已保存到：{output_path}")
        return str(output_path) # 返回相对或绝对路径，取决于如何使用
    except Exception as e:
        print(f"生成活动绘图时出错：{e}")
        return None

def generate_vulnerability_distribution_plot(vuln_summary: Dict[str, int], filename_prefix: str = "vuln") -> Optional[str]:
    \"\"\"
    为按严重性划分的漏洞分布生成条形图。
    'vuln_summary' 例如：{"CRITICAL": 2, "HIGH": 5, "MEDIUM": 10, "LOW": 3}
    \"\"\"
    if not vuln_summary:
        print("未提供用于绘图的漏洞摘要。")
        return None
    
    try:
        # 确保我们只绘制有计数的严重性级别
        filtered_summary = {k: v for k, v in vuln_summary.items() if v > 0}
        if not filtered_summary:
            print("无漏洞可绘制。")
            return None

        labels = list(filtered_summary.keys())
        counts = list(filtered_summary.values())
        
        # 定义严重性顺序以便更好地可视化
        severity_order = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNKNOWN"]
        ordered_labels = [s for s in severity_order if s in labels] + [s for s in labels if s not in severity_order]
        ordered_counts = [filtered_summary[s] for s in ordered_labels]


        plt.figure(figsize=(8, 6))
        sns.barplot(x=ordered_labels, y=ordered_counts, palette="viridis", order=ordered_labels) # 使用seaborn调色板
        plt.title('按严重性划分的漏洞分布')
        plt.xlabel('严重性')
        plt.ylabel('漏洞数量')
        plt.tight_layout()

        PLOTS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        output_filename = f"{filename_prefix}_distribution_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        output_path = PLOTS_OUTPUT_DIR / output_filename
        plt.savefig(output_path)
        plt.close()
        print(f"漏洞分布绘图已保存到：{output_path}")
        return str(output_path)
    except Exception as e:
        print(f"生成漏洞分布绘图时出错：{e}")
        return None
"""
    ),

    # --- app/models/ ---
    "app/models/__init__.py": create_python_file_content(PROJECT_ROOT / "app" / "models" / "__init__.py",
        """# app/models/__init__.py
# Pydantic模型，用于内部数据结构。
# from .common import BaseModelWithTimestamps # 示例
# from .intent import IntentModel
# from .task import TaskModel, TaskStatusEnum
# from .project_data import ProjectDataModel, CommitData, IssueData # 示例
# from .report import ReportModel
"""
    ),
    # --- app/utils/ ---
    "app/utils/__init__.py": create_python_file_content(PROJECT_ROOT / "app" / "utils" / "__init__.py",
        "# app/utils/__init__.py\n# 通用工具函数和辅助类。\n# from .http_client import AsyncHttpClient\n# from .llm_clients import get_llm_client, BaseLLMClient"
    ),
    "app/utils/http_client.py": create_python_file_content(PROJECT_ROOT / "app" / "utils" / "http_client.py",
        """# app/utils/http_client.py
# 异步HTTP客户端包装器 (例如，使用httpx)。
# 供连接器或其他需要发出外部HTTP请求的服务使用。

import httpx
from typing import Optional, Dict, Any, Union

class AsyncHttpClientSingleton:
    _client: Optional[httpx.AsyncClient] = None

    @classmethod
    def get_client(cls, timeout: float = 20.0, retries: int = 2) -> httpx.AsyncClient:
        if cls._client is None or cls._client.is_closed:
            # 为重试配置传输
            transport = httpx.AsyncHTTPTransport(retries=retries)
            cls._client = httpx.AsyncClient(timeout=timeout, transport=transport, follow_redirects=True)
            print("AsyncHttpClient (单例) 已初始化/重新初始化。")
        return cls._client

    @classmethod
    async def request(
        cls, 
        method: str, 
        url: str, 
        params: Optional[Dict] = None,
        data: Optional[Union[Dict, str]] = None, # 允许字符串数据 (例如，用于表单编码)
        json_payload: Optional[Any] = None, # 重命名以避免与json模块冲突
        headers: Optional[Dict] = None,
        # 请求特定超时/重试可以更细致地处理，但通常客户端级别设置已足够
    ) -> httpx.Response:
        client = cls.get_client() # 获取共享客户端实例
        try:
            effective_headers = headers or {}
            # 确保内容类型正确设置 (如果发送JSON)
            if json_payload is not None and 'Content-Type' not in effective_headers:
                effective_headers['Content-Type'] = 'application/json'

            response = await client.request(
                method=method.upper(),
                url=url,
                params=params,
                data=data, # 用于x-www-form-urlencoded
                json=json_payload, # 用于application/json
                headers=effective_headers
            )
            response.raise_for_status() # 对4XX/5XX响应引发异常
            return response
        except httpx.HTTPStatusError as e:
            print(f"HTTP错误：{e.response.status_code}，URL：{e.request.url}。响应：{e.response.text[:200]}")
            raise
        except httpx.RequestError as e: # 包括超时、连接错误等
            print(f"请求错误，URL：{e.request.url}：{e}")
            raise
        # 不在此处关闭客户端，它作为单例进行重用

    @classmethod
    async def close_client(cls): # 应用关闭时调用
        if cls._client and not cls._client.is_closed:
            await cls._client.aclose()
            cls._client = None
            print("AsyncHttpClient (单例) 已关闭。")

# 简化用法别名
async_http_client = AsyncHttpClientSingleton
"""
    ),
    "app/utils/llm_clients.py": create_python_file_content(PROJECT_ROOT / "app" / "utils" / "llm_clients.py",
        """# app/utils/llm_clients.py
# 与各种LLM服务（本地和基于云）交互的统一客户端。
# 使用app.config中的配置来选择和设置适当的客户端。

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
# from openai import AsyncOpenAI # 示例
# from anthropic import AsyncAnthropic # 示例
# from .http_client import async_http_client # 用于本地LLM服务器通信
from ..config import settings # 导入配置

class BaseLLMClient(ABC):
    def __init__(self, model_name: str):
        self.model_name = model_name

    @abstractmethod
    async def generate_completion(self, prompt: str, max_tokens: int = 2048, temperature: float = 0.7, 
                                  system_prompt: Optional[str] = None, stop_sequences: Optional[List[str]] = None) -> str:
        pass

    @abstractmethod
    async def generate_chat_completion(self, messages: List[Dict[str, str]], max_tokens: int = 2048, 
                                       temperature: float = 0.7, stop_sequences: Optional[List[str]] = None) -> str:
        pass

class OpenAIClientImpl(BaseLLMClient): # 示例实现
    def __init__(self, api_key: str, model_name: str = settings.OPENAI_MODEL_NAME):
        super().__init__(model_name)
        # self.client = AsyncOpenAI(api_key=api_key)
        print(f"OpenAIClientImpl已初始化，模型：{self.model_name}。")
        if not api_key:
            print("警告：未为OpenAIClientImpl提供OpenAI API密钥。")

    async def generate_completion(self, prompt: str, max_tokens: int = 2048, temperature: float = 0.7,
                                  system_prompt: Optional[str] = None, stop_sequences: Optional[List[str]] = None) -> str:
        # messages = []
        # if system_prompt: messages.append({"role": "system", "content": system_prompt})
        # messages.append({"role": "user", "content": prompt})
        # return await self.generate_chat_completion(messages, max_tokens, temperature, stop_sequences)
        print(f"OpenAIClientImpl: 模拟为提示词生成补全：'{prompt[:50]}...'")
        return f"来自OpenAI模型的模拟补全：{prompt[:50]}..."

    async def generate_chat_completion(self, messages: List[Dict[str, str]], max_tokens: int = 2048,
                                       temperature: float = 0.7, stop_sequences: Optional[List[str]] = None) -> str:
        # try:
        #     response = await self.client.chat.completions.create(
        #         model=self.model_name,
        #         messages=messages,
        #         max_tokens=max_tokens,
        #         temperature=temperature,
        #         stop=stop_sequences
        #     )
        #     return response.choices[0].message.content or ""
        # except Exception as e:
        #     print(f"OpenAI聊天补全出错：{e}")
        #     return f"错误：{e}"
        print(f"OpenAIClientImpl: 模拟为消息生成聊天补全：{messages}")
        return f"来自OpenAI模型的模拟聊天补全。"

class LocalLLMClientImpl(BaseLLMClient): # 本地模型示例（通过HTTP提供，如Ollama/vLLM中的Qwen）
    def __init__(self, api_base: str, model_name: str = "qwen_local"): # model_name可能在payload中指定
        super().__init__(model_name)
        self.api_base = api_base.rstrip('/')
        # self.http_client = async_http_client # 使用共享的HTTP客户端
        print(f"LocalLLMClientImpl已初始化，模型：{self.model_name}，API基地址：{self.api_base}。")

    async def generate_chat_completion(self, messages: List[Dict[str, str]], max_tokens: int = 2048,
                                       temperature: float = 0.7, stop_sequences: Optional[List[str]] = None) -> str:
        # 遵循本地服务器的API规范 (例如，OpenAI兼容端点)
        # endpoint = f"{self.api_base}/v1/chat/completions" # 示例
        # payload = {
        #     "model": self.model_name, # 服务器可能忽略此项，如果端点已绑定模型
        #     "messages": messages,
        #     "max_tokens": max_tokens,
        #     "temperature": temperature,
        #     "stop": stop_sequences,
        #     "stream": False # 通常用于非流式API
        # }
        # try:
        #     response = await self.http_client.request("POST", endpoint, json_payload=payload)
        #     response_data = response.json()
        #     return response_data["choices"][0]["message"]["content"]
        # except Exception as e:
        #     print(f"本地LLM聊天补全出错：{e}")
        #     return f"错误：{e}"
        print(f"LocalLLMClientImpl: 模拟为消息生成聊天补全：{messages}")
        return f"来自本地模型 '{self.model_name}' 的模拟聊天补全。"
    
    async def generate_completion(self, prompt: str, max_tokens: int = 2048, temperature: float = 0.7,
                                  system_prompt: Optional[str] = None, stop_sequences: Optional[List[str]] = None) -> str:
        # messages = []
        # if system_prompt: messages.append({"role": "system", "content": system_prompt})
        # messages.append({"role": "user", "content": prompt})
        # return await self.generate_chat_completion(messages, max_tokens, temperature, stop_sequences)
        print(f"LocalLLMClientImpl: 模拟为提示词生成补全：'{prompt[:50]}...'")
        return f"来自本地模型 '{self.model_name}' 的模拟补全。"


_llm_client_instance: Optional[BaseLLMClient] = None

def get_llm_client() -> BaseLLMClient:
    \"\"\"工厂函数，用于获取配置的LLM客户端（单例模式）。\"\"\"
    global _llm_client_instance
    if _llm_client_instance is None:
        if settings.LLM_PROVIDER == "openai" and settings.OPENAI_API_KEY:
            _llm_client_instance = OpenAIClientImpl(api_key=settings.OPENAI_API_KEY, model_name=settings.OPENAI_MODEL_NAME)
        elif settings.LLM_PROVIDER == "local_qwen" and settings.LOCAL_LLM_API_BASE:
            _llm_client_instance = LocalLLMClientImpl(api_base=settings.LOCAL_LLM_API_BASE, model_name="qwen_local_model") # 替换为实际模型名
        # 添加其他提供商，如Azure, Anthropic等
        # elif settings.LLM_PROVIDER == "azure" and settings.AZURE_OPENAI_KEY and settings.AZURE_OPENAI_ENDPOINT:
        #     _llm_client_instance = AzureOpenAIClientImpl(...)
        else:
            print(f"警告：LLM提供商 '{settings.LLM_PROVIDER}' 不支持或配置错误。将使用占位符客户端。")
            # 返回一个无法工作的占位符或引发配置错误
            class PlaceholderLLMClient(BaseLLMClient): # 占位符
                def __init__(self): super().__init__("placeholder_model")
                async def generate_completion(self, prompt, **kwargs): return "错误：LLM客户端未正确配置。"
                async def generate_chat_completion(self, messages, **kwargs): return "错误：LLM客户端未正确配置。"
            _llm_client_instance = PlaceholderLLMClient()
            # raise ValueError(f"不支持或配置错误的LLM提供商：{settings.LLM_PROVIDER}")
    return _llm_client_instance

# 全局LLM客户端实例 (或根据需要在各处注入)
llm_client = get_llm_client()
"""
    ),
}

def create_project_structure(root_dir: Path, structure: Dict[str, str]):
    """
    创建目录结构和文件。
    """
    for file_path_str, content in structure.items():
        full_file_path = root_dir / file_path_str
        
        # 如果父目录不存在，则创建它们
        full_file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 创建文件并写入内容
        with open(full_file_path, "w", encoding="utf-8") as f:
            # 如果内容不为空且不以换行符结尾，则添加换行符，以使文件更整洁
            if content and not content.endswith('\n'):
                content += '\n'
            f.write(content)
        print(f"已创建: {full_file_path}")

    # 如果模板子目录存在且是实际目录，则在其中创建空的__init__.py
    # (如果FILES_TO_CREATE中未定义带内容的文件)
    template_subdirs_to_check = [
        "app/prompts/templates/evaluation_agent",
        "app/prompts/templates" # 顶级模板目录也检查一下
    ]
    for subdir_str in template_subdirs_to_check:
        dir_path = root_dir / subdir_str
        if dir_path.exists() and dir_path.is_dir():
            init_py = dir_path / "__init__.py"
            if not init_py.exists() and not (subdir_str + "/__init__.py" in structure and structure[subdir_str + "/__init__.py"]):
                init_py.touch()
                print(f"已创建空文件: {init_py}")


if __name__ == "__main__":
    print(f"开始在以下位置生成项目：{PROJECT_ROOT.resolve()}")
    PROJECT_ROOT.mkdir(parents=True, exist_ok=True) # 确保根目录存在
    
    # Correctly handle looped template file creation
    looped_template_files = {}
    for template_file_name_loop_var in ["intent_agent", "task_planner_agent", "report_agent"]:
        file_key = f"app/prompts/templates/{template_file_name_loop_var}.md"
        
        # Python f-string part for the title
        title_part = f"### {template_file_name_loop_var.replace('_', ' ').title()} 提示词模板\n\n"
        
        # Raw string part for the Jinja2 body (Jinja2 braces should be single)
        # This is the critical fix: use r"""...""" for the body to avoid f-string parsing issues
        # with Jinja2's {{...}} and {%...%}
        body_part = r"""**目标**: (描述此提示词的目标)

**上下文变量 (Jinja2示例)**:
- 用户查询: `{{ user_query }}`
- 项目URL: `{{ project_url }}`
- 先前步骤的结果: `{{ previous_results | tojson(indent=2) }}`
- 当前任务详情: `{{ current_task_details }} `

**指令**:
1. 根据提供的上下文，(具体指令)。
2. (更多指令)。
3. 您的输出应严格遵循以下JSON格式。不要包含任何解释性文本或Markdown标记在JSON结构之外。

**输出格式 (JSON)**:
```json
{% raw %}
{
  "key1": "value1",
  "analysis_summary": "...",
  "next_actions_suggestion": [
    {
      "action_type": "...",
      "parameters": {}
    }
  ]
}
{% endraw %}
```

**约束**:
- 简洁明了。
- 仅输出JSON。
- (其他约束)。
"""
        looped_template_files[file_key] = title_part + body_part
    
    FILES_TO_CREATE.update(looped_template_files)

    # Agent file generation
    agent_files_dict = {}
    for agent_name_loop_var in ["intent_agent", "task_planner_agent", "data_agent", "evaluation_agent", "report_agent"]:
        agent_class_name_val = agent_name_loop_var.replace('_', ' ').title().replace(' ', '') + "Impl"
        agent_title_val = agent_name_loop_var.replace('_', ' ').title()

        capabilities_list_str = ""
        if agent_name_loop_var == "intent_agent": capabilities_list_str = 'return ["intent_recognition"]'
        elif agent_name_loop_var == "task_planner_agent": capabilities_list_str = 'return ["task_planning"]'
        elif agent_name_loop_var == "data_agent": capabilities_list_str = 'return ["data_retrieval_github", "data_retrieval_gitee", "data_retrieval_osv", "web_search", "graph_data_access"]'
        elif agent_name_loop_var == "evaluation_agent": capabilities_list_str = 'return ["project_evaluation_activity", "project_evaluation_security"]'
        elif agent_name_loop_var == "report_agent": capabilities_list_str = 'return ["report_generation_service"]'
        else: capabilities_list_str = f'return ["{agent_name_loop_var.lower()}_service_placeholder"]'

        print_handle_msg_literal = r'print(f"{self.agent_id} ({self.agent_name}) 收到消息: {message.model_dump_json(indent=2) if hasattr(message, \'model_dump_json\') else message}")'
        print_exec_task_literal = r'print(f"{self.agent_id} ({self.agent_name}) 执行任务: {task_details}，上下文: {context}")'
        
        content = f"""# app/agents/{agent_name_loop_var}.py
# 实现 {agent_title_val}。

from .base_agent import BaseAgent
from typing import List, Dict, Any, Optional
# from ..prompts.prompt_manager import prompt_manager
# from ..utils.llm_clients import llm_client
# from ..knowledge_base.retriever import knowledge_retriever
# from ..communication.protocols.mcp_schemas import Message, Performative

class {agent_class_name_val}(BaseAgent):
    def __init__(self, agent_id: Optional[str] = None):
        super().__init__(agent_id=agent_id, agent_name=self.__class__.__name__)

    def _define_capabilities(self) -> List[str]:
        {capabilities_list_str}

    async def handle_message(self, message: Any) -> Optional[Any]: # Message类型
        {print_handle_msg_literal}
        return {{"status": "message_acknowledged_by_{agent_name_loop_var}", "original_message_id": getattr(message, 'message_id', None)}}

    async def execute_task(self, task_details: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        \"\"\"
        {agent_title_val}的核心逻辑。
        示例任务详情: {{{{task_details}}}} 
        \"\"\"
        {print_exec_task_literal}
        
        # --- Agent特定逻辑占位符 ---
        # if self.agent_name == "{agent_class_name_val}": # Example check
        #    pass
        # --- 结束占位符 ---

        return {{"task_id": task_details.get("id", "N/A"), "status": "completed_by_{agent_name_loop_var}", "result": "dummy_result_from_{agent_name_loop_var}"}}

# 在app.main.py或专门的Agent管理模块中实例化并注册此Agent。
# 示例 (在app.main.py的startup事件中):
# from .agents.{agent_name_loop_var} import {agent_class_name_val}
# {agent_name_loop_var}_instance = {agent_class_name_val}()
# await {agent_name_loop_var}_instance.startup(agent_registry) # startup现在包含注册
"""
        agent_files_dict[f"app/agents/{agent_name_loop_var}.py"] = create_python_file_content(
            PROJECT_ROOT / "app" / "agents" / f"{agent_name_loop_var}.py",
            content
        )
    FILES_TO_CREATE.update(agent_files_dict)

    # Connector file generation
    connector_files_dict = {}
    for connector_name_loop_var in ["github_connector", "gitee_connector", "osv_connector", "web_search_connector"]:
        connector_class_name_val = connector_name_loop_var.replace('_', ' ').title().replace(' ', '') + "Impl"
        connector_service_name_val = connector_name_loop_var.split('_')[0].upper()

        print_init_literal_conn = r'print(f"{self.__class__.__name__} 已配置。")'
        print_connect_warn_literal_conn = r'print(f"警告：{self.__class__.__name__} 的API密钥未设置。")'
        print_connect_noop_literal_conn = r'print(f"{self.__class__.__name__} connect方法已调用（对于无状态API通常为空操作）。")'
        print_disconnect_literal_conn = r'print(f"{self.__class__.__name__} disconnect方法已调用。")'
        # Corrected template string for fetch_data print statement
        print_fetch_data_literal_conn_template = 'print(f"{self.__class__.__name__}: 正在为查询 \'{query_placeholder}\' 获取数据，参数 {{params_placeholder}}")'


        content = f"""# app/knowledge_base/connectors/{connector_name_loop_var}.py
# {connector_service_name_val} 服务的连接器。

from .base_connector import BaseConnector
from typing import Any, Dict, Optional, List
# from ...utils.http_client import async_http_client
# from ...config import settings

class {connector_class_name_val}(BaseConnector):
    def __init__(self, api_key: Optional[str] = None, api_base_url: Optional[str] = None, **kwargs):
        super().__init__(config=kwargs)
        self.api_key = api_key
        self.api_base_url = api_base_url
        {print_init_literal_conn}

    async def connect(self):
        if "{connector_name_loop_var.upper()}" not in ["WEB_SEARCH_CONNECTOR"] and not self.api_key:
             {print_connect_warn_literal_conn}
        {print_connect_noop_literal_conn}

    async def disconnect(self):
        {print_disconnect_literal_conn}

    async def fetch_data(self, query: Any, params: Optional[Dict] = None) -> Any:
        \"\"\"
        从{connector_service_name_val}获取数据。
        'query' 可能是项目路径、用户ID、搜索词等。
        'params' 可以指定页面限制、特定端点等。
        \"\"\"
        params = params or {{}}
        # This line is now carefully constructed to avoid premature f-string evaluation by the generator
        # It will be evaluated when the generated connector's fetch_data method is called.
        {print_fetch_data_literal_conn_template.replace('{query_placeholder}', '{str(query)[:100]}').replace('{params_placeholder}', '{params}')}
        
        # --- 示例特定连接器逻辑 ---
        # if self.__class__.__name__ == "{connector_class_name_val}":
        #    pass
        # --- 结束示例逻辑 ---
        
        return {{"source": "{connector_name_loop_var}", "query": str(query), "simulated_data": "来自{connector_name_loop_var}的示例数据"}}

# 示例：
# from ...config import settings
# if __name__ == "__main__":
#     import asyncio
#     async def test_connector():
#         if "{connector_name_loop_var}" == "github_connector":
#             # connector = {connector_class_name_val}(api_key=settings.GITHUB_TOKEN)
#             # data = await connector.fetch_data("octocat/Spoon-Knife")
#             # print(data)
#             pass
#     # asyncio.run(test_connector())
"""
        connector_files_dict[f"app/knowledge_base/connectors/{connector_name_loop_var}.py"] = create_python_file_content(
            PROJECT_ROOT / "app" / "knowledge_base" / "connectors" / f"{connector_name_loop_var}.py",
            content
        )
    FILES_TO_CREATE.update(connector_files_dict)
    
    # Model file generation (Refactored)
    model_files_dict = {}
    MODEL_FILE_BASE_CONTENT = """
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List as PyList, Dict, Any, Union
from enum import Enum
import uuid
from datetime import datetime, timezone
{common_imports_placeholder}

# --- Specific Model Definition for {model_title} ---
{class_definitions_placeholder}

# Example usage:
# if __name__ == "__main__":
#     if "{model_name_placeholder}" == "intent": 
#         # Example: test_intent = IntentModel(query="analyze this repo", evaluation_aspects=["activity"])
#         # print(test_intent.model_dump_json(indent=2))
#         pass
"""

    MODEL_CLASS_DEFINITIONS = {
        "common": """
class BaseModelWithTimestamps(BaseModel):
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Identifier(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="唯一标识符。")
""",
        "intent": """
class IntentModel(BaseModelWithTimestamps, Identifier):
    query: str = Field(description="用户的原始查询。")
    detected_project_url: Optional[HttpUrl] = Field(None, description="检测到的项目URL。")
    evaluation_aspects: PyList[str] = Field(default_factory=list, description="要评估的方面。")
    parsed_parameters: Dict[str, Any] = Field(default_factory=dict, description="从查询中解析的其他参数。")
    status: str = Field(default="pending", description="意图处理状态。")
""",
        "task": """
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
""",
        "project_data": """
class CommitData(BaseModel):
    sha: str
    author_name: Optional[str] = None
    author_login: Optional[str] = None
    date: datetime
    message: str

class IssueData(BaseModel):
    id: Union[int, str]
    title: str
    state: str
    created_at: datetime
    closed_at: Optional[datetime] = None
    assignee_login: Optional[str] = None
    labels: PyList[str] = Field(default_factory=list)

class ProjectSourceCodeInfo(BaseModel):
    main_language: Optional[str] = None
    languages_distribution: Optional[Dict[str, float]] = None
    lines_of_code: Optional[int] = None

class ProjectDataModel(BaseModelWithTimestamps, Identifier):
    project_url: HttpUrl
    project_name: Optional[str] = None
    description: Optional[str] = None
    last_fetched_at: Optional[datetime] = None
    commits: PyList[CommitData] = Field(default_factory=list)
    issues: PyList[IssueData] = Field(default_factory=list)
    license_info: Optional[Dict[str, Any]] = None
    vulnerabilities: PyList[Dict[str, Any]] = Field(default_factory=list)
    web_search_results: PyList[Dict[str, Any]] = Field(default_factory=list)
    graph_data_summary: Optional[Dict[str, Any]] = None
    source_code_info: Optional[ProjectSourceCodeInfo] = None
""",
        "report": """
class ReportModel(BaseModelWithTimestamps, Identifier):
    assessment_id: str = Field(description="此报告关联的评估ID。")
    project_name: str
    project_url: HttpUrl
    llm_generated_summary: Optional[str] = None
    evaluation_metrics_summary: Dict[str, Any] = Field(default_factory=dict)
    detailed_findings: PyList[Dict[str, Any]] = Field(default_factory=list)
    visualization_paths: Dict[str, str] = Field(default_factory=dict)
"""
    }

    for model_name_key_part in ["common", "intent", "task", "project_data", "report"]:
        model_title = model_name_key_part.replace('_', ' ').title()
        class_definitions = MODEL_CLASS_DEFINITIONS.get(model_name_key_part, f"# No specific class definition for {model_name_key_part}\\nclass GenericPlaceholder(BaseModel): pass")
        
        common_imports_str = ""
        if model_name_key_part != "common":
            common_imports_str = "from .common import BaseModelWithTimestamps, Identifier"

        # Use .format() for placeholders in the base template
        file_content_for_model = MODEL_FILE_BASE_CONTENT.format(
            common_imports_placeholder=common_imports_str,
            model_title=model_title,
            class_definitions_placeholder=class_definitions,
            model_name_placeholder=model_name_key_part # For the example usage comment
        )
        
        file_key = f"app/models/{model_name_key_part}.py"
        # We use create_python_file_content to add the standard header
        # The main content is already fully formed by MODEL_FILE_BASE_CONTENT.format(...)
        FILES_TO_CREATE[file_key] = create_python_file_content(
            PROJECT_ROOT / "app" / "models" / f"{model_name_key_part}.py", # Path object for header generation
            file_content_for_model # Pass the already formatted content for the body
        )


    create_project_structure(PROJECT_ROOT, FILES_TO_CREATE)
    print("项目结构和初始文件已成功创建！")
    print(f"后续步骤：")
    print(f"1. cd {PROJECT_ROOT.resolve()}")
    print(f"2. (可选) 创建并激活虚拟环境：python -m venv venv && source venv/bin/activate  (或 venv\\Scripts\\activate on Windows)")
    print(f"3. 安装依赖：pip install -r requirements.txt")
    print(f"4. 在 app/config.py 中配置API密钥和设置，或通过 .env 文件。")
    print(f"5. 开始开发您的Agent和应用逻辑！")


