#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File : llm.py
@Author : Ryan Zhu
@Date : 2025/5/19 01:31
"""

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
# Add imports for other LLM providers as needed, e.g., from langchain_community.chat_models import ChatOllama
from src.config.settings import get_settings # Assuming settings.py handles API key loading

# Global settings instance
settings = get_settings()

def get_llm_by_type(llm_config: dict):
    """
    Retrieves an LLM instance based on its type and configuration.
    `llm_config` is expected to be a dictionary like:
    {
        "provider": "openai",
        "model_name": "gpt-3.5-turbo",
        "temperature": 0.7,
        # API key might be handled globally via settings or passed explicitly
    }
    """
    provider = llm_config.get("provider", "").lower()
    model_name = llm_config.get("model_name")
    temperature = llm_config.get("temperature", 0.7)
    max_tokens = llm_config.get("max_tokens", 1024) # Example of another common param

    print(f"Attempting to get LLM for provider: {provider}, model: {model_name}")

    if provider == "openai":
        api_key = settings.openai_api_key
        if not api_key:
            raise ValueError("OpenAI API key not found in settings.")
        return ChatOpenAI(
            model_name=model_name, 
            temperature=temperature, 
            max_tokens=max_tokens,
            openai_api_key=api_key
        )
    elif provider == "anthropic":
        api_key = settings.anthropic_api_key
        if not api_key:
            raise ValueError("Anthropic API key not found in settings.")
        return ChatAnthropic(
            model=model_name, # Anthropic uses 'model' not 'model_name'
            temperature=temperature, 
            max_tokens=max_tokens,
            anthropic_api_key=api_key
        )
    # Example for Ollama (local LLM)
    # elif provider == "ollama":
    #     # Ollama typically runs as a service; base_url might be configurable
    #     # from langchain_community.chat_models import ChatOllama
    #     return ChatOllama(
    #         model=model_name, 
    #         temperature=temperature
    #         # base_url=settings.ollama_base_url # If configurable
    #     )
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
