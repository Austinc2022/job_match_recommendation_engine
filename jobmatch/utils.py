"""
Module: utils.py
Provides utility functions for reading jobseekers and jobs from CSV files.
"""

import csv
from .jobseeker import Jobseeker
from .job import Job


def read_jobseekers(filename):
    """Generator that reads jobseekers from a CSV file."""
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield Jobseeker(
                id=int(row['id']),
                name=row['name'],
                skills=row['skills']
            )


def read_jobs(filename):
    """Reads jobs from a CSV file and returns a list (since the number of jobs is usually manageable)."""
    jobs = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            jobs.append(Job(
                id=int(row['id']),
                title=row['title'],
                required_skills=row['required_skills']
            ))
    return jobs
