
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
