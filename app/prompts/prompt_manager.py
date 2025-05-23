#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/prompts/prompt_manager.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""

# app/prompts/prompt_manager.py
# 管理Jinja2提示词模板的加载和渲染，用于LLM交互。

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
from typing import Dict, Any
from ..config import settings # 导入配置以获取模板目录

class PromptManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(PromptManager, cls).__new__(cls)
            # 初始化只执行一次
            template_folder_path = Path(settings.PROMPT_TEMPLATE_DIR)
            if not template_folder_path.is_dir():
                # 尝试相对于当前文件创建（如果配置路径无效）
                # 这更像是一个回退，理想情况下配置路径应该是正确的
                alt_path = Path(__file__).resolve().parent / "templates"
                if alt_path.is_dir():
                    template_folder_path = alt_path
                    print(f"警告：配置的模板目录 '{settings.PROMPT_TEMPLATE_DIR}' 未找到。回退到 '{alt_path}'。")
                else:
                    # 如果回退路径也不存在，则创建它
                    alt_path.mkdir(parents=True, exist_ok=True)
                    template_folder_path = alt_path
                    print(f"警告：模板目录 '{settings.PROMPT_TEMPLATE_DIR}' 和 '{alt_path}' 均未找到。已创建 '{alt_path}'。请添加模板。")
            
            cls._instance.env = Environment(
                loader=FileSystemLoader(template_folder_path),
                autoescape=select_autoescape(['html', 'xml', 'md']), # 如果不需要，请小心使用自动转义
                trim_blocks=True,
                lstrip_blocks=True
            )
            print(f"PromptManager已初始化，模板文件夹：{template_folder_path}")
        return cls._instance

    def load_and_render(self, template_name: str, context: Dict[str, Any]) -> str:
        """加载指定的提示词模板并使用给定的上下文进行渲染。"""
        try:
            template = self.env.get_template(template_name)
            return template.render(context)
        except Exception as e:
            print(f"加载/渲染模板 {template_name} 时出错：{e}")
            # 回退或引发错误
            return f"错误：无法渲染提示词模板 '{template_name}'。详情：{e}"

# 单例实例
prompt_manager = PromptManager()

# 示例用法：
# if __name__ == "__main__":
#     # 确保settings.PROMPT_TEMPLATE_DIR指向一个有效的、包含模板的目录
#     # 例如，手动创建 app/prompts/templates/intent_agent.md
#     # Path(settings.PROMPT_TEMPLATE_DIR).mkdir(parents=True, exist_ok=True)
#     # with open(Path(settings.PROMPT_TEMPLATE_DIR) / "intent_agent.md", "w") as f:
#     #     f.write("User query: {{ user_query }}")
#
#     rendered_prompt = prompt_manager.load_and_render(
#         "intent_agent.md", 
#         {"user_query": "分析此项目。", "project_url": "http://..."}
#     )
#     print(rendered_prompt)
