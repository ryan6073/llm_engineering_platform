#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/knowledge_base/vector_store/faiss_client.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/knowledge_base/vector_store/faiss_client.py
# 与FAISS向量索引交互的客户端。
# 处理嵌入生成（或假设预计算的嵌入）、索引加载和相似性搜索。

import faiss # type: ignore
import numpy as np
from typing import List, Tuple, Optional, Union
from pathlib import Path
# from sentence_transformers import SentenceTransformer # 嵌入生成示例
# from ...config import settings # 用于配置

class FaissClient:
    def __init__(self, index_path: str, embedding_model_name: Optional[str] = None, dimension: Optional[int] = None):
        self.index_file_path = Path(index_path)
        self.index: Optional[faiss.Index] = None
        self.embedding_model = None
        self._dimension = dimension

        if embedding_model_name:
            # try:
            #     self.embedding_model = SentenceTransformer(embedding_model_name)
            #     self._dimension = self.embedding_model.get_sentence_embedding_dimension()
            #     print(f"SentenceTransformer模型 '{embedding_model_name}' 已加载，维度：{self._dimension}")
            # except Exception as e:
            #     print(f"加载SentenceTransformer模型 '{embedding_model_name}' 失败：{e}。请确保模型已安装。")
            #     # 如果模型加载失败但维度已提供，则继续；否则可能无法创建索引。
            #     if not self._dimension:
            #         print("错误：嵌入模型加载失败且未提供维度。FaissClient可能无法正常工作。")
            pass # 占位：实际应加载模型或确保维度已知

        if not self._dimension: # 如果模型未加载且未提供维度，则设置一个默认值或引发错误
            self._dimension = 384 # 示例：all-MiniLM-L6-v2的维度
            print(f"警告：未指定嵌入维度，使用默认值：{self._dimension}。这可能与您的数据不匹配。")

        self._load_or_create_index()
        print(f"FaissClient已初始化。索引路径：{self.index_file_path}, 维度：{self._dimension}")

    def _load_or_create_index(self):
        if self.index_file_path.exists():
            try:
                self.index = faiss.read_index(str(self.index_file_path))
                print(f"FAISS索引已从 {self.index_file_path} 加载。索引大小：{self.index.ntotal if self.index else 0}")
                if self.index and self._dimension and self.index.d != self._dimension:
                    print(f"警告：索引维度 ({self.index.d}) 与模型/配置维度 ({self._dimension}) 不同。可能导致问题。")
                    # 可以选择重建索引或引发错误
            except Exception as e:
                print(f"加载FAISS索引时出错：{e}。如果维度已知，将在首次添加时创建新索引。")
                self.index = None # 确保如果加载失败，索引为None
        else:
            print(f"在 {self.index_file_path} 未找到FAISS索引文件。如果维度已知，将在首次添加时创建。")
        
        if not self.index and self._dimension:
            # 如果无法加载但维度已知，则创建新索引
            self.index = faiss.IndexFlatL2(self._dimension) # 示例：L2距离索引
            print(f"已创建新的空FAISS IndexFlatL2，维度 {self._dimension}。")

    async def get_embedding(self, text: Union[str, List[str]]) -> Optional[np.ndarray]:
        if not self.embedding_model:
            print("错误：嵌入模型未加载。无法生成嵌入。")
            return None
        # try:
        #     # SentenceTransformer的encode方法是同步的，如果用于异步代码，应考虑在线程池中运行
        #     # import asyncio
        #     # loop = asyncio.get_running_loop()
        #     # embeddings = await loop.run_in_executor(None, self.embedding_model.encode, text)
        #     # return np.array(embeddings)
        #     return np.array(self.embedding_model.encode(text)) # 简单同步调用
        # except Exception as e:
        #     print(f"生成嵌入时出错：{e}")
        #     return None
        print(f"模拟为 '{text}' 生成嵌入。") # 占位
        return np.random.rand(1 if isinstance(text, str) else len(text), self._dimension).astype(np.float32)


    async def add_texts(self, texts: List[str], text_ids: Optional[List[Any]] = None): # text_ids用于元数据存储
        if not self.embedding_model:
            print("无法添加文本：嵌入模型未加载。")
            return
        embeddings = await self.get_embedding(texts)
        if embeddings is not None:
            # TODO: 实现元数据存储以将text_ids与FAISS内部索引关联起来
            # 对于IndexFlatL2，FAISS索引是连续的。需要外部映射。
            self.add_embeddings(embeddings) # 简单添加，不处理ID映射
            print(f"已为 {len(texts)} 个文本添加嵌入。元数据ID（如果提供）需要外部管理。")

    def add_embeddings(self, embeddings: np.ndarray):
        if not self.index:
            if self._dimension and embeddings.shape[1] == self._dimension:
                self.index = faiss.IndexFlatL2(self._dimension)
                print("在add_embeddings期间因缺少索引而初始化了新的FAISS索引。")
            else:
                raise ValueError("FAISS索引未初始化且维度不匹配或嵌入形状不正确。")

        if embeddings.shape[1] != self.index.d:
            raise ValueError(f"嵌入维度 ({embeddings.shape[1]}) 与索引维度 ({self.index.d}) 不匹配。")
        
        self.index.add(embeddings.astype(np.float32))
        print(f"已向FAISS索引添加 {embeddings.shape[0]} 个嵌入。总数：{self.index.ntotal}")

    async def search_by_text(self, query_text: str, top_k: int = 5) -> Tuple[Optional[np.ndarray], Optional[np.ndarray]]:
        if not self.embedding_model:
            print("无法按文本搜索：嵌入模型未加载。")
            return None, None
        query_embedding = await self.get_embedding(query_text)
        if query_embedding is not None:
            return self.search_by_embedding(query_embedding, top_k)
        return None, None

    def search_by_embedding(self, query_embedding: np.ndarray, top_k: int = 5) -> Tuple[Optional[np.ndarray], Optional[np.ndarray]]:
        if not self.index or self.index.ntotal == 0:
            print("FAISS索引未加载或为空。")
            return np.array([]), np.array([])
        if query_embedding.ndim == 1:
            query_embedding = np.expand_dims(query_embedding, axis=0).astype(np.float32)
        elif query_embedding.ndim == 2:
            query_embedding = query_embedding.astype(np.float32)
        else:
            raise ValueError("查询嵌入必须是1D或2D NumPy数组。")

        if query_embedding.shape[1] != self.index.d:
            raise ValueError(f"查询嵌入维度 ({query_embedding.shape[1]}) 与索引维度 ({self.index.d}) 不匹配。")
        
        distances, indices = self.index.search(query_embedding, top_k)
        return distances, indices # 最近邻的距离和索引

    def save_index(self):
        if self.index:
            self.index_file_path.parent.mkdir(parents=True, exist_ok=True)
            faiss.write_index(self.index, str(self.index_file_path))
            print(f"FAISS索引已保存到 {self.index_file_path}")
        else:
            print("无法保存：FAISS索引未初始化。")
