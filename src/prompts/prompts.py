# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

import os
import dataclasses
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
from typing import List, Dict, Any

# Assuming AgentState might be a TypedDict or Pydantic model.
# For LangGraph, AgentState is often a TypedDict.
# from langgraph.prebuilt.chat_agent_executor import AgentState 
# If you define your own AgentState (e.g. in src/models/agent_io.py):
from src.models.agent_io import AgentState # Make sure this model is defined

from src.config.configuration import Configuration # Make sure this path is correct

# Initialize Jinja2 environment
# This expects .md template files to be in the same directory as this prompts.py file
PROMPTS_DIR = os.path.dirname(__file__)
env = Environment(
    loader=FileSystemLoader(PROMPTS_DIR),
    autoescape=select_autoescape(['html', 'xml', 'md']), # Be specific about autoescape
    trim_blocks=True,
    lstrip_blocks=True,
    keep_trailing_newline=True,
)


def get_prompt_template_string(prompt_name: str) -> str:
    """
    Load and return a raw prompt template string using Jinja2.

    Args:
        prompt_name: Name of the prompt template file (without .md extension)

    Returns:
        The raw template string.
    """
    try:
        # Jinja2's get_template returns a Template object. To get the string,
        # you'd typically read the file directly or render it.
        # For raw string, it's often easier to just read the file.
        template_path = os.path.join(PROMPTS_DIR, f"{prompt_name}.md")
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        raise ValueError(f"Error loading template string {prompt_name}: {e}")


def apply_prompt_template(
    prompt_name: str, state: AgentState, configurable: Configuration = None
) -> List[Dict[str, Any]]:
    """
    Apply template variables to a prompt template and return formatted messages.

    Args:
        prompt_name: Name of the prompt template to use.
        state: Current agent state containing variables to substitute.
               Ensure 'messages' is a key in state if using AgentState directly.
        configurable: Optional configuration object.

    Returns:
        List of messages with the system prompt as the first message.
    """
    current_state_dict = dict(state) if not isinstance(state, dict) else state

    state_vars = {
        "CURRENT_TIME": datetime.now().strftime("%a %b %d %Y %H:%M:%S %z"),
        **current_state_dict,
    }

    if configurable:
        # Ensure configurable is a dict or can be converted to one
        if dataclasses.is_dataclass(configurable):
            state_vars.update(dataclasses.asdict(configurable))
        elif isinstance(configurable, dict):
            state_vars.update(configurable)
        # else: log a warning or raise error if configurable is of unexpected type

    try:
        template = env.get_template(f"{prompt_name}.md")
        system_prompt_content = template.render(**state_vars)

        existing_messages = current_state_dict.get("messages", [])
        if not isinstance(existing_messages, list):
            # Log warning or handle error if messages format is unexpected
            existing_messages = []

        # The structure [{role: "system", content: ...}] + other_messages is common
        # for many LangChain/LangGraph chat models.
        return [{"role": "system", "content": system_prompt_content}] + existing_messages
    except Exception as e:
        # Consider more specific exception handling (e.g., jinja2.exceptions.TemplateNotFound)
        raise ValueError(f"Error applying template {prompt_name} with state {state_vars.keys()}: {e}")

