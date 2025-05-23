# LLM Engineering Platform

[简体中文](./README_zh.md) | [English](./README.md)

An intelligent open-source project assessment platform based on LLMs and Multi-Agent Systems.

## Project Overview

This system utilizes Large Language Models (LLMs) and a dynamic Multi-Agent System (MAS) architecture to provide comprehensive evaluations of open-source projects. Key features include:

- User intent recognition and parsing.
- Dynamic task decomposition and collaborative execution by specialized agents.
- Agent registration, discovery, and A2A/MCP communication.
- Sophisticated prompt engineering using Jinja2 templates.
- Integration with diverse knowledge sources:
    - Version Control: GitHub, Gitee APIs.
    - Vulnerability Databases: OSV.
    - Graph Databases: Neo4j for relationship analysis.
    - Vector Stores: FAISS for semantic search.
    - Web Search: Real-time information retrieval.
- Extensible evaluation metrics.
- Structured report generation with visualizations.

## Setup and Installation

1.  Clone this repository.
2.  Create a virtual environment: `python -m venv venv`
3.  Activate the virtual environment:
    * Linux/macOS: `source venv/bin/activate`
    * Windows: `venv\Scripts\activate`
4.  Install dependencies: `pip install -r requirements.txt`
5.  Configure API keys and other settings in `app/config.py` or via environment variables (e.g., a `.env` file).
6.  Run the application: `uvicorn app.main:app --reload`

## Project Structure

(Please refer to the generated file structure and comments within the files for details.)

## Contributing

Contributions are welcome! Please refer to `CONTRIBUTING.md` for guidelines.

## License

This project is licensed under the [MIT License](./LICENSE).