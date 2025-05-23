#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/utils/llm_clients.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/utils/llm_clients.py
# 与各种LLM服务（本地和基于云）交互的统一客户端。
# 使用app.config中的配置来选择和设置适当的客户端。

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
# from openai import AsyncOpenAI # 示例
# from anthropic import AsyncAnthropic # 示例
# from .http_client import async_http_client # 用于本地LLM服务器通信
from ..config import settings # 导入配置

class BaseLLMClient(ABC):
    def __init__(self, model_name: str):
        self.model_name = model_name

    @abstractmethod
    async def generate_completion(self, prompt: str, max_tokens: int = 2048, temperature: float = 0.7, 
                                  system_prompt: Optional[str] = None, stop_sequences: Optional[List[str]] = None) -> str:
        pass

    @abstractmethod
    async def generate_chat_completion(self, messages: List[Dict[str, str]], max_tokens: int = 2048, 
                                       temperature: float = 0.7, stop_sequences: Optional[List[str]] = None) -> str:
        pass

class OpenAIClientImpl(BaseLLMClient): # 示例实现
    def __init__(self, api_key: str, model_name: str = settings.OPENAI_MODEL_NAME):
        super().__init__(model_name)
        # self.client = AsyncOpenAI(api_key=api_key)
        print(f"OpenAIClientImpl已初始化，模型：{self.model_name}。")
        if not api_key:
            print("警告：未为OpenAIClientImpl提供OpenAI API密钥。")

    async def generate_completion(self, prompt: str, max_tokens: int = 2048, temperature: float = 0.7,
                                  system_prompt: Optional[str] = None, stop_sequences: Optional[List[str]] = None) -> str:
        # messages = []
        # if system_prompt: messages.append({"role": "system", "content": system_prompt})
        # messages.append({"role": "user", "content": prompt})
        # return await self.generate_chat_completion(messages, max_tokens, temperature, stop_sequences)
        print(f"OpenAIClientImpl: 模拟为提示词生成补全：'{prompt[:50]}...'")
        return f"来自OpenAI模型的模拟补全：{prompt[:50]}..."

    async def generate_chat_completion(self, messages: List[Dict[str, str]], max_tokens: int = 2048,
                                       temperature: float = 0.7, stop_sequences: Optional[List[str]] = None) -> str:
        # try:
        #     response = await self.client.chat.completions.create(
        #         model=self.model_name,
        #         messages=messages,
        #         max_tokens=max_tokens,
        #         temperature=temperature,
        #         stop=stop_sequences
        #     )
        #     return response.choices[0].message.content or ""
        # except Exception as e:
        #     print(f"OpenAI聊天补全出错：{e}")
        #     return f"错误：{e}"
        print(f"OpenAIClientImpl: 模拟为消息生成聊天补全：{messages}")
        return f"来自OpenAI模型的模拟聊天补全。"

class LocalLLMClientImpl(BaseLLMClient): # 本地模型示例（通过HTTP提供，如Ollama/vLLM中的Qwen）
    def __init__(self, api_base: str, model_name: str = "qwen_local"): # model_name可能在payload中指定
        super().__init__(model_name)
        self.api_base = api_base.rstrip('/')
        # self.http_client = async_http_client # 使用共享的HTTP客户端
        print(f"LocalLLMClientImpl已初始化，模型：{self.model_name}，API基地址：{self.api_base}。")

    async def generate_chat_completion(self, messages: List[Dict[str, str]], max_tokens: int = 2048,
                                       temperature: float = 0.7, stop_sequences: Optional[List[str]] = None) -> str:
        # 遵循本地服务器的API规范 (例如，OpenAI兼容端点)
        # endpoint = f"{self.api_base}/v1/chat/completions" # 示例
        # payload = {
        #     "model": self.model_name, # 服务器可能忽略此项，如果端点已绑定模型
        #     "messages": messages,
        #     "max_tokens": max_tokens,
        #     "temperature": temperature,
        #     "stop": stop_sequences,
        #     "stream": False # 通常用于非流式API
        # }
        # try:
        #     response = await self.http_client.request("POST", endpoint, json_payload=payload)
        #     response_data = response.json()
        #     return response_data["choices"][0]["message"]["content"]
        # except Exception as e:
        #     print(f"本地LLM聊天补全出错：{e}")
        #     return f"错误：{e}"
        print(f"LocalLLMClientImpl: 模拟为消息生成聊天补全：{messages}")
        return f"来自本地模型 '{self.model_name}' 的模拟聊天补全。"
    
    async def generate_completion(self, prompt: str, max_tokens: int = 2048, temperature: float = 0.7,
                                  system_prompt: Optional[str] = None, stop_sequences: Optional[List[str]] = None) -> str:
        # messages = []
        # if system_prompt: messages.append({"role": "system", "content": system_prompt})
        # messages.append({"role": "user", "content": prompt})
        # return await self.generate_chat_completion(messages, max_tokens, temperature, stop_sequences)
        print(f"LocalLLMClientImpl: 模拟为提示词生成补全：'{prompt[:50]}...'")
        return f"来自本地模型 '{self.model_name}' 的模拟补全。"


_llm_client_instance: Optional[BaseLLMClient] = None

def get_llm_client() -> BaseLLMClient:
    """工厂函数，用于获取配置的LLM客户端（单例模式）。"""
    global _llm_client_instance
    if _llm_client_instance is None:
        if settings.LLM_PROVIDER == "openai" and settings.OPENAI_API_KEY:
            _llm_client_instance = OpenAIClientImpl(api_key=settings.OPENAI_API_KEY, model_name=settings.OPENAI_MODEL_NAME)
        elif settings.LLM_PROVIDER == "local_qwen" and settings.LOCAL_LLM_API_BASE:
            _llm_client_instance = LocalLLMClientImpl(api_base=settings.LOCAL_LLM_API_BASE, model_name="qwen_local_model") # 替换为实际模型名
        # 添加其他提供商，如Azure, Anthropic等
        # elif settings.LLM_PROVIDER == "azure" and settings.AZURE_OPENAI_KEY and settings.AZURE_OPENAI_ENDPOINT:
        #     _llm_client_instance = AzureOpenAIClientImpl(...)
        else:
            print(f"警告：LLM提供商 '{settings.LLM_PROVIDER}' 不支持或配置错误。将使用占位符客户端。")
            # 返回一个无法工作的占位符或引发配置错误
            class PlaceholderLLMClient(BaseLLMClient): # 占位符
                def __init__(self): super().__init__("placeholder_model")
                async def generate_completion(self, prompt, **kwargs): return "错误：LLM客户端未正确配置。"
                async def generate_chat_completion(self, messages, **kwargs): return "错误：LLM客户端未正确配置。"
            _llm_client_instance = PlaceholderLLMClient()
            # raise ValueError(f"不支持或配置错误的LLM提供商：{settings.LLM_PROVIDER}")
    return _llm_client_instance

# 全局LLM客户端实例 (或根据需要在各处注入)
llm_client = get_llm_client()
