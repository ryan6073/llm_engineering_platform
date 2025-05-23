#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/knowledge_base/graph_store/graph_utils.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/knowledge_base/graph_store/graph_utils.py
# 主要使用NetworkX处理图数据的实用程序。
# 包括图创建、操作、分析和序列化/反序列化功能。

import networkx as nx
from typing import List, Dict, Any, Tuple, Optional, Union
from pathlib import Path

def create_graph_from_edges(edges: List[Tuple[Any, Any, Optional[Dict]]], directed: bool = False) -> Union[nx.Graph, nx.DiGraph]:
    """从边列表创建NetworkX图。边可以具有属性。"""
    G = nx.DiGraph() if directed else nx.Graph()
    for edge in edges:
        u, v, *attrs = edge
        attr_dict = attrs[0] if attrs else {}
        G.add_edge(u, v, **attr_dict)
    print(f"已创建图，包含 {G.number_of_nodes()} 个节点和 {G.number_of_edges()} 条边。")
    return G

def add_nodes_with_attributes(G: Union[nx.Graph, nx.DiGraph], nodes_data: List[Tuple[Any, Dict]]):
    """向图中的节点添加节点及其属性。"""
    for node, attrs in nodes_data:
        G.add_node(node, **attrs)
    print(f"已添加/更新 {len(nodes_data)} 个节点的属性。")


def graph_to_graphml(G: Union[nx.Graph, nx.DiGraph], filepath: Union[str, Path]) -> None:
    """将NetworkX图序列化为GraphML格式。"""
    path_obj = Path(filepath)
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    nx.write_graphml(G, str(path_obj)) # write_graphml需要字符串路径
    print(f"图已保存到GraphML：{path_obj}")

def graphml_to_graph(filepath: Union[str, Path]) -> Optional[Union[nx.Graph, nx.DiGraph]]:
    """从GraphML格式反序列化NetworkX图。"""
    path_obj = Path(filepath)
    if path_obj.exists():
        G = nx.read_graphml(str(path_obj))
        print(f"图已从GraphML加载：{path_obj}。节点：{G.number_of_nodes()}，边：{G.number_of_edges()}")
        return G
    else:
        print(f"GraphML文件未找到：{path_obj}")
        return None

def get_basic_graph_metrics(G: Union[nx.Graph, nx.DiGraph]) -> Dict[str, Any]:
    """计算图的一些基本指标。"""
    if not G: return {}
    num_nodes = G.number_of_nodes()
    metrics = {
        "num_nodes": num_nodes,
        "num_edges": G.number_of_edges(),
        "density": nx.density(G)
    }
    if num_nodes > 0:
        if isinstance(G, nx.Graph): # 无向图指标
            metrics["is_connected"] = nx.is_connected(G)
            # metrics["average_clustering_coefficient"] = nx.average_clustering(G)
        elif isinstance(G, nx.DiGraph): # 有向图指标
            metrics["is_strongly_connected"] = nx.is_strongly_connected(G)
            metrics["is_weakly_connected"] = nx.is_weakly_connected(G)
        
        # degrees = [val for (node, val) in G.degree()]
        # metrics["average_degree"] = sum(degrees) / num_nodes if num_nodes > 0 else 0
    print(f"已计算基本图指标：{metrics}")
    return metrics
