#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : llm_engineering_platform
@File    : app/models/project_data.py
@Author  : Ryan Zhu
@Date    : 2025/05/19 01:31
"""


from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List as PyList, Dict, Any, Union
from enum import Enum
import uuid
from datetime import datetime, timezone
from .common import BaseModelWithTimestamps, Identifier

# --- Specific Model Definition for Project Data ---

class CommitData(BaseModel):
    sha: str
    author_name: Optional[str] = None
    author_login: Optional[str] = None
    date: datetime
    message: str

class IssueData(BaseModel):
    id: Union[int, str]
    title: str
    state: str
    created_at: datetime
    closed_at: Optional[datetime] = None
    assignee_login: Optional[str] = None
    labels: PyList[str] = Field(default_factory=list)

class ProjectSourceCodeInfo(BaseModel):
    main_language: Optional[str] = None
    languages_distribution: Optional[Dict[str, float]] = None
    lines_of_code: Optional[int] = None

class ProjectDataModel(BaseModelWithTimestamps, Identifier):
    project_url: HttpUrl
    project_name: Optional[str] = None
    description: Optional[str] = None
    last_fetched_at: Optional[datetime] = None
    commits: PyList[CommitData] = Field(default_factory=list)
    issues: PyList[IssueData] = Field(default_factory=list)
    license_info: Optional[Dict[str, Any]] = None
    vulnerabilities: PyList[Dict[str, Any]] = Field(default_factory=list)
    web_search_results: PyList[Dict[str, Any]] = Field(default_factory=list)
    graph_data_summary: Optional[Dict[str, Any]] = None
    source_code_info: Optional[ProjectSourceCodeInfo] = None


# Example usage:
# if __name__ == "__main__":
#     if "project_data" == "intent": 
#         # Example: test_intent = IntentModel(query="analyze this repo", evaluation_aspects=["activity"])
#         # print(test_intent.model_dump_json(indent=2))
#         pass
