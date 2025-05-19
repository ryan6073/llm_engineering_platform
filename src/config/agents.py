#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File : agents.py
@Author : Ryan Zhu
@Date : 2025/5/19 01:31
"""

# Example configuration for AGENT_LLM_MAP
# Maps agent types (or specific agent names) to LLM configurations 
# that src.llms.llm.get_llm_by_type can understand.

AGENT_LLM_MAP = {
    "default_react_agent": { # This is an agent_type key
        "provider": "openai",  # or "anthropic", "ollama", etc.
        "model_name": "gpt-3.5-turbo",
        "temperature": 0.7,
        "max_tokens": 1500,
    },
    "data_query_react_agent": {
        "provider": "openai",
        "model_name": "gpt-4o", 
        "temperature": 0.2,
        "max_tokens": 2000,
    },
    "creative_writing_agent": {
        "provider": "anthropic",
        "model_name": "claude-3-sonnet-20240229",
        "temperature": 0.8,
        "max_tokens": 3000,
    },
    # "ollama_mistral_agent": {
    #     "provider": "ollama", 
    #     "model_name": "mistral", 
    #     "temperature": 0.5,
    # }
    # The keys (e.g., "default_react_agent") should match the `agent_type`
    # parameter passed to your agent factory function.
}
