#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File : configuration.py
@Author : Ryan Zhu
@Date : 2025/5/19 01:31
"""

from dataclasses import dataclass, field
from typing import Optional, Dict, Any

@dataclass
class Configuration:
    """
    Global or configurable settings that can be passed to prompts or agents.
    These can be dynamically loaded or set.
    """
    # Example fields:
    company_name: str = "DefaultLLMPlatformUser"
    user_role: str = "analyst"
    max_iterations: int = 15 # Max iterations for ReAct or other looped agents
    debug_mode: bool = False
    custom_instructions: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    # Add fields as needed by your application
    # For example, if different agents need different base URLs for tools:
    # tool_server_url: str = "http://localhost:8081/tools"

# Example of how you might load this:
# def load_app_configuration() -> Configuration:
#     # Load from a file, environment variables, etc.
#     # For simplicity, returning a default instance here
#     return Configuration(company_name="MyOrganization", debug_mode=True)
