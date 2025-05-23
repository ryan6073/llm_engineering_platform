#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/evaluation/metrics.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/evaluation/metrics.py
# 定义特定的评估指标及其计算逻辑。
# 这些函数通常由EvaluationAgent调用。

from typing import Dict, Any, List, Optional

def calculate_developer_activity(commit_data: Optional[List[Dict]], issue_data: Optional[List[Dict]]) -> Dict[str, Any]:
    """
    计算开发者活动指标。
    示例：提交频率、活跃贡献者、Issue解决率。
    """
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
    """
    根据检测到的许可证和项目上下文检查许可证合规性。
    可能涉及对照批准/有问题的许可证列表进行检查。
    """
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
    """
    根据已识别的漏洞（例如，来自OSV）对项目进行评分。
    考虑漏洞的严重性和数量。
    """
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
