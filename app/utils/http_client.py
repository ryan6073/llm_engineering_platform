#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/utils/http_client.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/utils/http_client.py
# 异步HTTP客户端包装器 (例如，使用httpx)。
# 供连接器或其他需要发出外部HTTP请求的服务使用。

import httpx
from typing import Optional, Dict, Any, Union

class AsyncHttpClientSingleton:
    _client: Optional[httpx.AsyncClient] = None

    @classmethod
    def get_client(cls, timeout: float = 20.0, retries: int = 2) -> httpx.AsyncClient:
        if cls._client is None or cls._client.is_closed:
            # 为重试配置传输
            transport = httpx.AsyncHTTPTransport(retries=retries)
            cls._client = httpx.AsyncClient(timeout=timeout, transport=transport, follow_redirects=True)
            print("AsyncHttpClient (单例) 已初始化/重新初始化。")
        return cls._client

    @classmethod
    async def request(
        cls, 
        method: str, 
        url: str, 
        params: Optional[Dict] = None,
        data: Optional[Union[Dict, str]] = None, # 允许字符串数据 (例如，用于表单编码)
        json_payload: Optional[Any] = None, # 重命名以避免与json模块冲突
        headers: Optional[Dict] = None,
        # 请求特定超时/重试可以更细致地处理，但通常客户端级别设置已足够
    ) -> httpx.Response:
        client = cls.get_client() # 获取共享客户端实例
        try:
            effective_headers = headers or {}
            # 确保内容类型正确设置 (如果发送JSON)
            if json_payload is not None and 'Content-Type' not in effective_headers:
                effective_headers['Content-Type'] = 'application/json'

            response = await client.request(
                method=method.upper(),
                url=url,
                params=params,
                data=data, # 用于x-www-form-urlencoded
                json=json_payload, # 用于application/json
                headers=effective_headers
            )
            response.raise_for_status() # 对4XX/5XX响应引发异常
            return response
        except httpx.HTTPStatusError as e:
            print(f"HTTP错误：{e.response.status_code}，URL：{e.request.url}。响应：{e.response.text[:200]}")
            raise
        except httpx.RequestError as e: # 包括超时、连接错误等
            print(f"请求错误，URL：{e.request.url}：{e}")
            raise
        # 不在此处关闭客户端，它作为单例进行重用

    @classmethod
    async def close_client(cls): # 应用关闭时调用
        if cls._client and not cls._client.is_closed:
            await cls._client.aclose()
            cls._client = None
            print("AsyncHttpClient (单例) 已关闭。")

# 简化用法别名
async_http_client = AsyncHttpClientSingleton
