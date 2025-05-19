# LLM Engineering Platform

A platform for building, deploying, and managing sophisticated LLM-powered agents and applications using LangGraph.

## Overview

This platform provides a structured approach to developing language agents by leveraging:
- **LangGraph:** For defining agent workflows as stateful graphs.
- **LangChain:** For core LLM interactions, tool usage, and component integrations.
- **Jinja2 Prompts:** For flexible and maintainable prompt engineering.
- **FastAPI:** For exposing agent functionalities via a robust API.
- **Docker:** For containerization and reproducible deployments.
- **uv:** For fast Python package installation and virtual environment management.

## Project Structure

- `src/`: Core application source code.
  - `agents/`: Agent definitions, LangGraph agent implementations (e.g., ReAct), and factory functions.
  - `config/`: Python-based configurations (LLM mappings, global settings, Pydantic settings).
  - `llms/`: Abstractions for interacting with different LLM providers (OpenAI, Anthropic, local models).
  - `prompts/`: Jinja2-based prompt templating. `.md` files in this directory are prompt templates.
  - `orchestrator/`: Logic for managing and executing LangGraph graphs.
  - `knowledge_base/`: Modules for Retrieval Augmented Generation (RAG) - retrievers, loaders.
  - `tools/`: Custom tools that agents can use.
  - `models/`: Pydantic data models for internal data structures, API schemas, and agent states.
  - `utils/`: Common utility functions.
- `app/`: FastAPI application for exposing the platform via an API.
  - `main.py`: FastAPI application entry point.
  - `api/`: API versioning and endpoint definitions.
- `tests/`: Unit and integration tests.
- `scripts/`: Helper scripts (e.g., development server startup, data loading).
- `data/`: For local data, knowledge sources (often gitignored in production).
- `logs/`: Application logs.
- `pyproject.toml`: Project metadata, dependencies (can be used by `uv`), and tool configurations.
- `requirements.txt`: Alternative dependency list (can be used by `uv`).
- `Dockerfile`, `docker-compose.yml`: For containerized deployment.
- `.env_template`, `.env`: Environment variable management.

## Getting Started

### Prerequisites

- Python 3.9+ (uv will manage this within its virtual environment if needed)
- **uv:** Install from [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)
- Docker and Docker Compose (recommended for easy setup of services like databases)
- An LLM API key (e.g., OpenAI, Anthropic)

### Setup Instructions with `uv`

1.  **Clone the Repository (if applicable):**
    ```bash
    # git clone <repository_url>
    # cd llm_engineering_platform
    ```

2.  **Create and Activate Virtual Environment using `uv`:**
    `uv` can create and manage virtual environments. It will create a `.venv` directory by default.
    ```bash
    uv venv # Creates a virtual environment
    source .venv/bin/activate # On macOS/Linux
    # .venv\Scriptsctivate # On Windows
    ```
    Alternatively, many `uv` commands can be run without explicitly activating the venv if you prefix them with `uv run -- `.

3.  **Install Dependencies using `uv`:**
    You can install dependencies from `requirements.txt` or `pyproject.toml`.

    Using `requirements.txt`:
    ```bash
    uv pip install -r requirements.txt
    ```
    Or, if your `pyproject.toml` is set up with a PEP 621 `[project]` table (and optionally `[tool.uv.sources]` or `[tool.poetry.dependencies]`), `uv` can install from it:
    ```bash
    uv pip install . # Installs dependencies from pyproject.toml
    # To install dev dependencies as well (if defined in pyproject.toml, e.g., under [project.optional-dependencies] or [tool.poetry.group.dev.dependencies]):
    # uv pip install ".[dev]" 
    ```

4.  **Configure Environment Variables:**
    Copy the `.env_template` file to a new file named `.env` and update it with your actual API keys and configurations:
    ```bash
    cp .env_template .env
    ```
    Edit `.env` with your details (e.g., `OPENAI_API_KEY`).

### Running the Application

#### Option 1: Using Docker Compose (Recommended for Production-like Environment & Services)

This will build the Docker image and start the application along with any defined services (e.g., Redis, Qdrant).
```bash
docker-compose up --build
```
The API will typically be available at `http://localhost:8000` (or the port specified in your `.env` / `docker-compose.yml`). API documentation (Swagger UI) will be at `http://localhost:8000/docs`.

To stop the services:
```bash
docker-compose down
```

#### Option 2: Running Natively with Uvicorn (for FastAPI development, using `uv`)

Ensure your virtual environment (managed by `uv`) is activated or use `uv run`.
The `scripts/run_dev.sh` script can be adapted or you can run Uvicorn directly.

Using `uv run` (activates the environment implicitly for the command):
```bash
uv run uvicorn app.main:app --reload --host $(grep FASTAPI_HOST .env | cut -d '=' -f2 || echo "0.0.0.0") --port $(grep FASTAPI_PORT .env | cut -d '=' -f2 || echo "8000")
```
Or, after activating the venv (`source .venv/bin/activate`):
```bash
uvicorn app.main:app --reload --host $(grep FASTAPI_HOST .env | cut -d '=' -f2 || echo "0.0.0.0") --port $(grep FASTAPI_PORT .env | cut -d '=' -f2 || echo "8000")
```
The `--reload` flag enables auto-reloading on code changes.

## Development

### Prompt Engineering
- Prompt templates are located in `src/prompts/` as `.md` files using Jinja2 syntax.
- The `src/prompts/prompts.py` module provides utilities for loading and rendering these templates.

### Creating New Agents (LangGraph)
1.  Define the agent's state structure (e.g., in `src/models/agent_io.py`).
2.  Implement the agent's nodes (functions that perform actions or LLM calls).
3.  Construct the `StateGraph` in `src/orchestrator/` or a dedicated agent module.
4.  Define edges and conditional edges to control the flow.
5.  Compile the graph into a runnable application.
6.  Use the agent factory (`src/agents/factory.py`) or directly instantiate and use the compiled graph.

### Tools
- Define custom tools by inheriting from LangChain's `BaseTool` or using the `@tool` decorator.
- Place tool definitions in `src/tools/`.
- Make tools available to agents during their initialization.

### Testing
- Write unit tests for individual components in `tests/unit/`.
- Write integration tests for agent flows and API endpoints in `tests/integration/`.
- Run tests using Pytest (can be run with `uv run pytest`):
  ```bash
  uv run pytest
  ```
  Or with coverage:
  ```bash
  uv run pytest --cov=src tests/
  ```

### Linting and Formatting
This project can be configured to use tools like Ruff (which `uv` can also run).
```bash
# Example with Ruff using uv
uv run ruff check .
uv run ruff format .
```

## Contributing
(Add guidelines for contributing to the project if applicable)

## License
(Specify the license for your project, e.g., MIT, Apache 2.0)
This project is licensed under the MIT License - see the LICENSE file for details.
