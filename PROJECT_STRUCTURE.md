app/                                    // 核心应用程序代码
├── main.py                             // FastAPI应用入口：初始化、配置及Agent运行时引导
├── api/                                // API接口层
│   ├── endpoints/assessment.py         // API端点：定义项目评估等路由及处理
│   └── schemas.py                      // Pydantic模型：API请求/响应的数据结构与校验
├── core/                               // 核心业务逻辑、编排与Agent管理
│   ├── orchestrator.py                 // 高级任务编排器：顶层任务分解、分派给Agent群组、监控总体进展，与AgentRegistry交互
│   └── agent_registry.py               // Agent注册与发现中心：Agent动态注册、注销、能力查询与服务发现
├── agents/                             // Agent实现：各类可动态注册和交互的智能代理
│   ├── base_agent.py                   // Agent基类：定义Agent核心行为、生命周期、通信接口(MCP)、能力描述及注册协议
│   ├── intent_agent.py                 // 意图识别Agent：独立Agent，解析用户输入，提取结构化意图
│   ├── task_planner_agent.py           // 任务规划Agent：独立Agent，分解复杂任务为子任务或协作计划，可与其他Agent协商
│   ├── data_agent.py                   // 数据收集与管理Agent：数据服务提供者，响应数据请求(A2A/MCP)，与KnowledgeBase交互，执行多源数据获取、图构建等
│   ├── evaluation_agent.py             // 项目评估Agent：独立Agent，接收评估任务与数据，执行评估逻辑
│   └── report_agent.py                 // 报告生成Agent：独立Agent，接收评估结果，生成报告，可协作获取摘要或可视化
├── communication/                      // Agent间通信与协议实现
│   ├── message_bus.py                  // (可选) Agent消息总线：提供异步消息传递、路由，简化Agent间通信
│   └── protocols/                      // 通信协议定义
│       └── mcp_schemas.py              // MCP模式定义：Pydantic定义Agent间通信消息结构、标准动作及内容格式
├── prompts/                            // 提示词工程 (各Agent可使用)
│   ├── prompt_manager.py               // 提示词管理器：为Agent提供提示词加载与渲染服务
│   └── templates/                      // 提示词模板：各Agent使用的Markdown格式Jinja2提示词
├── knowledge_base/                     // 知识库集成与检索 (DataAgent封装或授权Agent访问)
│   ├── retriever.py                    // 统一检索接口：实现关键词、向量、图谱、Web搜索及混合检索
│   ├── connectors/                     // 数据源连接器
│   │   ├── base_connector.py           // 连接器基类
│   │   ├── github_connector.py         // GitHub API连接器
│   │   ├── gitee_connector.py          // Gitee API连接器
│   │   ├── osv_connector.py            // OSV API连接器
│   │   └── web_search_connector.py     // Web搜索连接器：对接搜索引擎API
│   ├── vector_store/                   // 向量存储与检索
│   │   └── faiss_client.py             // FAISS客户端封装
│   └── graph_store/                    // 图数据库与图文件处理
│       ├── neo4j_client.py             // Neo4j图数据库客户端封装
│       └── graph_utils.py              // 图处理工具 (NetworkX)
├── evaluation/                         // 评估指标与模型定义
│   └── metrics.py                      // 评估指标实现：供EvaluationAgent调用
├── reporting/                          // 报告生成与可视化
│   ├── generator.py                    // 报告内容组装器：供ReportAgent调用
│   └── visualizations.py               // 数据可视化组件
├── models/                             // Pydantic内部数据模型 (除MCP外，也用于API等)
│   ├── common.py                       // 通用基础数据结构
│   ├── intent.py                       // 意图对象模型
│   ├── task.py                         // 任务对象模型 (或通用目标/行动描述)
│   └── report.py                       // 评估报告结构模型
├── utils/                              // 通用工具类与辅助函数
│   ├── http_client.py                  // 异步HTTP客户端
│   └── llm_clients.py                  // LLM客户端封装：支持本地与云端LLM
└── config.py                           // 应用配置管理：AgentRegistry地址、MessageBus配置、LLM配置、知识库配置等
