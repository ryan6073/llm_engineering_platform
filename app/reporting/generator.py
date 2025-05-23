#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/reporting/generator.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/reporting/generator.py
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
        """生成JSON报告数据结构。"""
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
        """从JSON数据渲染Markdown报告。"""
        md_report = f"# {report_data.get('project_name', 'N/A')} 项目评估报告\n\n"
        md_report += f"**报告ID:** {report_data.get('report_id')}\n"
        md_report += f"**评估ID:** {report_data.get('assessment_id')}\n"
        md_report += f"**生成日期:** {report_data.get('generated_at')}\n\n"

        if report_data.get('overall_summary_llm'):
            md_report += f"## 总体摘要 (由LLM生成)\n"
            md_report += f"{report_data['overall_summary_llm']}\n\n"

        md_report += f"## 评估指标\n"
        metrics = report_data.get('evaluation_metrics', {})
        if metrics:
            for metric_name, metric_value_obj in metrics.items():
                md_report += f"### {metric_name.replace('_', ' ').title()}\n"
                if isinstance(metric_value_obj, dict):
                    for key, val in metric_value_obj.items():
                        if key == "metric_name": continue # 已在标题中
                        md_report += f"- **{key.replace('_', ' ').title()}**: {val}\n"
                else: # 直接值
                    md_report += f"- {metric_value_obj}\n"
                md_report += "\n"
        else:
            md_report += "无可用指标。\n"
        md_report += "\n"
        
        findings = report_data.get('detailed_findings', [])
        if findings:
            md_report += f"## 详细发现\n"
            for finding in findings:
                md_report += f"- {finding.get('description', '无描述')}"
                if finding.get('severity'): md_report += f" (严重性: {finding['severity']})"
                md_report += "\n"
            md_report += "\n"

        plot_paths = report_data.get('visualization_paths', {})
        if plot_paths:
            md_report += f"## 可视化\n"
            for viz_name, viz_path in plot_paths.items():
                md_report += f"### {viz_name.replace('_', ' ').title()}\n"
                # 假设路径是相对的或Web可访问的
                md_report += f"![{viz_name}]({viz_path})\n\n" 
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
#     print("\n--- Markdown Report ---")
#     print(md_output)
#
#     # 保存到文件
#     # report_file_path = Path(settings.REPORTS_DIR) / f"{report_content['report_id']}.md"
#     # report_file_path.parent.mkdir(parents=True, exist_ok=True)
#     # with open(report_file_path, "w", encoding="utf-8") as f:
#     #    f.write(md_output)
#     # print(f"\nMarkdown报告已保存到：{report_file_path}")
