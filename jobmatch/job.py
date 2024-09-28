"""
Module: job.py
Defines the Job class, representing a job with required skills.
"""

from dataclasses import dataclass, field
from typing import Set


@dataclass
class Job:
    """Represents a job with required skills."""
    id: int
    title: str
    required_skills: Set[str] = field(default_factory=set)

    def __post_init__(self):
        self.id = int(self.id)
        self.title = self.title.strip()
        self.required_skills = self._parse_skills(self.required_skills)

    @staticmethod
    def _parse_skills(skills):
        if isinstance(skills, str):
            skills_iterable = skills.split(',')
        else:
            skills_iterable = skills
        return set(skill.strip().lower() for skill in skills_iterable)
