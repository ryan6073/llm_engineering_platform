#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File : factory.py
@Author : Ryan Zhu
@Date : 2025/5/19 01:31
"""

from langgraph.prebuilt import create_react_agent # Standard ReAct agent factory
# For more complex agent types or custom graphs, you might use other LangGraph components
# from langgraph.graph import StateGraph, END

from src.prompts.prompts import apply_prompt_template 
from src.llms.llm import get_llm_by_type
from src.config.agents import AGENT_LLM_MAP
from src.models.agent_io import AgentState # Assuming AgentState is defined here

# Example: If you need a specific prompt template for ReAct
from langchain_core.prompts import ChatPromptTemplate


def create_llm_engineering_agent(agent_name: str, agent_type: str, tools: list, prompt_template_name: str):
    """
    Factory function to create LangGraph agents.
    This example focuses on the ReAct agent, but can be extended.
    """
    llm_config = AGENT_LLM_MAP.get(agent_type)
    if not llm_config:
        raise ValueError(f"LLM configuration for agent type '{agent_type}' not found in AGENT_LLM_MAP.")

    llm_instance = get_llm_by_type(llm_config)

    # For create_react_agent, the 'prompt' argument is typically a ChatPromptTemplate
    # that defines the system message. The ReAct logic (Thought, Action, Observation)
    # is handled by the graph structure itself.
    # Your `apply_prompt_template` function seems to generate a full message list
    # including the system prompt. This is more aligned with how a `ChatAgentExecutor`
    # or a custom graph node might consume prompts.

    # Option 1: Adapt apply_prompt_template to be used for the system message of ReAct
    # This means the Jinja template (e.g., example_prompt.md) should be designed
    # primarily as a system message for the ReAct agent.

    # A simplified system message for ReAct might look like:
    # react_system_message_template = "You are a ReAct agent. Your name is {agent_name}. Use tools to answer."
    # react_prompt = ChatPromptTemplate.from_messages([
    #     ("system", react_system_message_template.format(agent_name=agent_name))
    # ])
    # This is a very basic example. The prompt_template_name could point to a more complex system message.

    # Let's assume prompt_template_name refers to a Jinja template that, when rendered
    # with minimal state (or just global vars like agent_name), produces the system message content.

    # Minimal state for rendering a system message template
    # The `state` passed to `apply_prompt_template` by the lambda in the original user code
    # `lambda state: apply_prompt_template(prompt_template_name, state)`
    # might be problematic if `create_react_agent` doesn't provide a rich state object
    # for its `prompt` callable during its internal setup.
    # The `prompt` in `create_react_agent` is usually simpler.

    # For `create_react_agent`, the `messages_modifier` is often used to inject the system prompt.
    # Let's use `messages_modifier` as it's more idiomatic for `create_react_agent`.

    # The `apply_prompt_template` function expects an `AgentState`.
    # We need to construct a minimal or representative AgentState for the system prompt generation.
    # This is a bit of a workaround because the system prompt is usually static or has few variables.

    # Create a placeholder state for rendering the system prompt via apply_prompt_template
    # This assumes your prompt template for ReAct is designed to be the *system message* part.
    initial_system_prompt_state = AgentState(messages=[], intermediate_steps=[]) # Corrected key name

    # The apply_prompt_template returns a list of messages. We need the system message content.
    # This is a bit convoluted if the template is just for the system message.
    # A simpler Jinja template just for the system message string would be more direct.

    # Let's make the system message template rendering more direct:
    from src.prompts.prompts import env as jinja_env # Access Jinja environment directly
    try:
        system_template = jinja_env.get_template(f"{prompt_template_name}.md")
        # Pass variables relevant to the system message
        system_message_content = system_template.render(
            agent_name=agent_name,
            agent_type=agent_type,
            tools=tools # Making tools available to the system prompt template
        )
    except Exception as e:
        raise ValueError(f"Error rendering system prompt template {prompt_template_name} for ReAct agent: {e}")

    # The `create_react_agent` function returns a compiled LangGraph.
    agent_graph = create_react_agent(
        model=llm_instance,
        tools=tools,
        # The system message can be passed directly or via messages_modifier
        messages_modifier=system_message_content # Pass the rendered system message string
    )

    print(f"ReAct Agent graph '{agent_name}' (type: '{agent_type}') created using template '{prompt_template_name}'.")
    return agent_graph

# You might have other factory functions for different types of LangGraph agents
# e.g., a custom StateGraph based agent
# def create_custom_graph_agent(agent_name: str, ...):
#     workflow = StateGraph(AgentState)
#     # ... define nodes and edges ...
#     app = workflow.compile()
#     return app

