# LLM 工程化平台 (智能评估系统)

[English](./README.md) | [简体中文](./README_zh.md)

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

1.  克隆本仓库。
2.  创建虚拟环境: `python -m venv venv`
3.  激活虚拟环境:
    * Linux/macOS: `source venv/bin/activate`
    * Windows: `venv\Scripts\activate`
4.  安装依赖: `pip install -r requirements.txt`
5.  在 `app/config.py` 中配置API密钥及其他设置，或通过环境变量配置（例如，一个 `.env` 文件）。
6.  运行应用: `uvicorn app.main:app --reload`

## 项目结构

(请参考生成的文件结构及文件内的注释。)

## 贡献指南

欢迎参与贡献！请参考 `CONTRIBUTING.md` 文件了解详细指南。

## 许可证

本项目采用 [MIT 许可证](./LICENSE)授权。