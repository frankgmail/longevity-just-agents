import dataclasses
import pathlib
from string import Template

from dataclasses import dataclass, field
from just_agents.llm_session import LLMSession
from typing import Any, Dict, List, Optional
from just_agents.utils import load_config

@dataclass
class ChatAgent(LLMSession):
    """
    Default agent class, it assumes that each agent has a role, goal, and background story.
    """
    role: str  # "Role of the agent"
    goal: Optional[str] = None  # "Goal of the agent"
    task: Optional[str] = None # Tasks of the agent
    backstory: Optional[str] = None  # "Backstory of the agent"
    config: Dict[str, Any] = field(default_factory=lambda: load_config("agent_prompts.yaml"))  # "Configuration dictionary for the agent, usually loaded from yaml"
    agent_prompt: Optional[str] = None  # "Prompt used by the agent, usually generated by the template"

    def __post_init__(self):
        """
        Post init logic
        :return:
        """
        super().__post_init__()
        agent_template: Optional[Template] = Template(self.config["agent_prompt"])

        self.agent_prompt = agent_template.substitute(role = self.role,
                goal = self.goal,
                backstory = self.backstory,
                task = self.task
            )
        print(self.agent_prompt)
        if self.agent_prompt is not None:
            self.instruct(self.agent_prompt)