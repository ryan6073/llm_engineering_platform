#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/reporting/visualizations.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/reporting/visualizations.py
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
    """
    为开发者活动趋势（例如，随时间变化的提交）生成绘图。
    保存绘图并返回其路径。
    'activity_data' 应为字典列表，例如：[{'date': '2023-01-01', 'commits': 10}, ...]
    """
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
    """
    为按严重性划分的漏洞分布生成条形图。
    'vuln_summary' 例如：{"CRITICAL": 2, "HIGH": 5, "MEDIUM": 10, "LOW": 3}
    """
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
