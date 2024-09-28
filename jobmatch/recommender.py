"""
Module: recommender.py
Contains the Recommender class for generating and sorting job recommendations.
"""


class Recommender:
    """Generates and sorts job recommendations for jobseekers."""

    def __init__(self, jobseekers, jobs):
        self.jobseekers = jobseekers
        self.jobs = jobs

    def generate_recommendations(self, include_skills=False):
        """Generates recommendations as a generator."""
        for seeker in self.jobseekers:
            recommendations = []
            for job in self.jobs:
                matched_skills = seeker.skills & job.required_skills
                if matched_skills:
                    unmatched_skills = job.required_skills - seeker.skills
                    matching_skill_count = len(matched_skills)
                    matching_skill_percent = round(
                        (matching_skill_count / len(job.required_skills)) * 100
                    )
                    recommendation = {
                        'jobseeker_id': seeker.id,
                        'jobseeker_name': seeker.name,
                        'job_id': job.id,
                        'job_title': job.title,
                        'matching_skill_count': matching_skill_count,
                        'matching_skill_percent': matching_skill_percent
                    }
                    if include_skills:
                        recommendation['matched_skills'] = sorted(matched_skills)
                        recommendation['unmatched_skills'] = sorted(unmatched_skills)
                    recommendations.append(recommendation)
            # Sort recommendations for the current jobseeker
            sorted_recommendations = sorted(
                recommendations,
                key=lambda x: (-x['matching_skill_percent'], x['job_id'])
            )
            # Yield recommendations one by one
            for rec in sorted_recommendations:
                yield rec
