### Report Agent 提示词模板

**目标**: (描述此提示词的目标)

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
