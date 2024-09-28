"""
Module: jobseeker.py
Defines the Jobseeker class, representing a jobseeker with a set of skills.
"""

from dataclasses import dataclass, field
from typing import Set


@dataclass
class Jobseeker:
    """Represents a jobseeker with a set of skills."""
    id: int
    name: str
    skills: Set[str] = field(default_factory=set)

    def __post_init__(self):
        self.id = int(self.id)
        self.name = self.name.strip()
        self.skills = self._parse_skills(self.skills)

    @staticmethod
    def _parse_skills(skills):
        if isinstance(skills, str):
            skills_iterable = skills.split(',')
        else:
            skills_iterable = skills
        return set(skill.strip().lower() for skill in skills_iterable)
