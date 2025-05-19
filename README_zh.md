# LLM 工程平台

[English](./README.md) | [简体中文](./README_zh.md)

一个用于构建、部署和管理复杂 LLM 驱动的代理和应用的平台，基于 LangGraph。

## 概述

本平台通过以下技术提供结构化的语言代理开发方法：
- **LangGraph**：用于定义代理工作流的状态图。
- **LangChain**：用于核心 LLM 交互、工具使用和组件集成。
- **Jinja2 模板**：用于灵活且可维护的提示工程。
- **FastAPI**：通过强大的 API 暴露代理功能。
- **Docker**：用于容器化和可重复的部署。
- **uv**：用于快速的 Python 包安装和虚拟环境管理。

## 项目结构

- `src/`：核心应用源代码。
  - `agents/`：代理定义、LangGraph 代理实现（如 ReAct）和工厂函数。
  - `config/`：基于 Python 的配置（LLM 映射、全局设置、Pydantic 设置）。
  - `llms/`：与不同 LLM 提供商（OpenAI、Anthropic、本地模型）交互的抽象层。
  - `prompts/`：基于 Jinja2 的提示模板，目录中的 `.md` 文件为提示模板。
  - `orchestrator/`：管理并执行 LangGraph 图的逻辑。
  - `knowledge_base/`：检索增强生成（RAG）模块 - 检索器、加载器。
  - `tools/`：代理可使用的自定义工具。
  - `models/`：Pydantic 数据模型，用于内部数据结构、API 模式和代理状态。
  - `utils/`：通用工具函数。
- `app/`：用于通过 API 暴露平台的 FastAPI 应用。
  - `main.py`：FastAPI 应用入口点。
  - `api/`：API 版本管理和端点定义。
- `tests/`：单元测试和集成测试。
- `scripts/`：辅助脚本（如开发服务器启动、数据加载）。
- `data/`：本地数据、知识源（生产环境中通常被 gitignore）。
- `logs/`：应用日志。
- `pyproject.toml`：项目元数据、依赖（可由 `uv` 使用）和工具配置。
- `requirements.txt`：备用的依赖列表（可由 `uv` 使用）。
- `Dockerfile`, `docker-compose.yml`：用于容器化部署。
- `.env_template`, `.env`：环境变量管理。

## 开始使用

### 前置条件

- Python 3.9+（`uv` 会在虚拟环境中管理此依赖）
- **uv**：从 [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv) 安装
- Docker 和 Docker Compose（推荐用于快速设置数据库等服务）
- LLM API 密钥（如 OpenAI、Anthropic）

### 使用 `uv` 进行设置

1. **克隆仓库（如果适用）：**
   ```bash
   # git clone <repository_url>
   # cd llm_engineering_platform
   ```

2. **使用 `uv` 创建并激活虚拟环境：**
   `uv` 可以创建并管理虚拟环境，默认创建 `.venv` 目录。
   ```bash
   uv venv # 创建虚拟环境
   source .venv/bin/activate # 在 macOS/Linux 上
   # .venv\Scripts\activate # 在 Windows 上
   ```
   或者，许多 `uv` 命令无需显式激活虚拟环境，可通过前缀 `uv run --` 运行。

3. **使用 `uv` 安装依赖：**
   可从 `requirements.txt` 或 `pyproject.toml` 安装依赖。

   使用 `requirements.txt`：
   ```bash
   uv pip install -r requirements.txt
   ```
   或者，如果 `pyproject.toml` 配置了 PEP 621 `[project]` 表（以及可选的 `[tool.uv.sources]` 或 `[tool.poetry.dependencies]`），`uv` 可直接从中安装：
   ```bash
   uv pip install . # 从 pyproject.toml 安装依赖
   # 若需同时安装开发依赖（若在 pyproject.toml 中定义，如 [project.optional-dependencies] 或 [tool.poetry.group.dev.dependencies]）：
   # uv pip install ".[dev]"
   ```

4. **配置环境变量：**
   复制 `.env_template` 文件为 `.env`，并更新其中的 API 密钥和配置：
   ```bash
   constitutionally .env_template .env
   ```
   编辑 `.env` 文件，填入实际信息（如 `OPENAI_API_KEY`）。

### 运行应用

#### 选项 1：使用 Docker Compose（推荐用于类生产环境和服务）

此命令将构建 Docker 镜像并启动应用及定义的服务（如 Redis、Qdrant）。
```bash
docker-compose up --build
```
API 通常可在 `http://localhost:8000` 访问（或 `.env` / `docker-compose.yml` 中指定的端口）。API 文档（Swagger UI）位于 `http://localhost:8000/docs`。

停止服务：
```bash
docker-compose down
```

#### 选项 2：使用 Uvicorn 本地运行（用于 FastAPI 开发，使用 `uv`）

确保虚拟环境（由 `uv` 管理）已激活，或使用 `uv run`。
可调整 `scripts/run_dev.sh` 脚本，或直接运行 Uvicorn。

使用 `uv run`（隐式激活环境）：
```bash
uv run uvicorn app.main:app --reload --host $(grep FASTAPI_HOST .env | cut -d '=' -f2 || echo "0.0.0.0") --port $(grep FASTAPI_PORT .env | cut -d '=' -f2 || echo "8000")
```
或在激活虚拟环境后（`source .venv/bin/activate`）：
```bash
uvicorn app.main:app --reload --host $(grep FASTAPI_HOST .env | cut -d '=' -f2 || echo "0.0.0.0") --port $(grep FASTAPI_PORT .env | cut -d '=' -f2 || echo "8000")
```
`--reload` 标志启用代码更改时的自动重载。

## 开发

### 提示工程
- 提示模板位于 `src/prompts/`，为使用 Jinja2 语法的 `.md` 文件。
- `src/prompts/prompts.py` 模块提供加载和渲染这些模板的工具。

### 创建新代理（LangGraph）
1. 定义代理的状态结构（如在 `src/models/agent_io.py` 中）。
2. 实现代理的节点（执行动作或 LLM 调用的函数）。
3. 在 `src/orchestrator/` 或专用代理模块中构建 `StateGraph`。
4. 定义边和条件边以控制流程。
5. 将图编译为可运行的应用。
6. 使用代理工厂（`src/agents/factory.py`）或直接实例化和使用编译后的图。

### 工具
- 通过继承 LangChain 的 `BaseTool` 或使用 `@tool` 装饰器定义自定义工具。
- 将工具定义置于 `src/tools/`。
- 在代理初始化时使工具对代理可用。

### 测试
- 在 `tests/unit/` 中为单个组件编写单元测试。
- 在 `tests/integration/` 中为代理流程和 API 端点编写集成测试。
- 使用 Pytest 运行测试（可通过 `uv run pytest` 执行）：
  ```bash
  uv run pytest
  ```
  或带覆盖率：
  ```bash
  uv run pytest --cov=src tests/
  ```

### 代码检查与格式化
项目可配置使用 Ruff 等工具（可通过 `uv` 运行）。
```bash
# 使用 Ruff 的示例
uv run ruff check .
uv run ruff format .
```

## 贡献
（添加适用于项目的贡献指南）

## 许可证
本项目采用 MIT 许可证 - 详情见 LICENSE 文件。