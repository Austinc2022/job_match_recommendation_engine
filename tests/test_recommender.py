"""
Unit tests for the Recommender class.
"""

import unittest
from jobmatch.recommender import Recommender
from jobmatch.jobseeker import Jobseeker
from jobmatch.job import Job


class TestRecommender(unittest.TestCase):
    """Tests for the Recommender class."""

    def setUp(self):
        """Set up test data for each test."""
        self.jobseekers = [
            Jobseeker(id=1, name='Alice', skills='Python, SQL, Problem Solving'),
            Jobseeker(id=2, name='Bob', skills='Java, Teamwork')
        ]
        self.jobs = [
            Job(
                id=1,
                title='Python Developer',
                required_skills='Python, Django, REST'
            ),
            Job(
                id=2,
                title='Java Developer',
                required_skills='Java, Spring, Teamwork'
            ),
            Job(
                id=3,
                title='Data Analyst',
                required_skills='SQL, Excel, Communication'
            )
        ]
        self.recommender = Recommender(self.jobseekers, self.jobs)

    def test_generate_recommendations(self):
        """Test that recommendations are generated correctly."""
        recommendations = self.recommender.generate_recommendations()
        expected = [
            {
                'jobseeker_id': 1,
                'jobseeker_name': 'Alice',
                'job_id': 1,
                'job_title': 'Python Developer',
                'matching_skill_count': 1,
                'matching_skill_percent': 33  # 1 out of 3 skills
            },
            {
                'jobseeker_id': 1,
                'jobseeker_name': 'Alice',
                'job_id': 3,
                'job_title': 'Data Analyst',
                'matching_skill_count': 1,
                'matching_skill_percent': 33  # 1 out of 3 skills
            },
            {
                'jobseeker_id': 2,
                'jobseeker_name': 'Bob',
                'job_id': 2,
                'job_title': 'Java Developer',
                'matching_skill_count': 2,
                'matching_skill_percent': 67  # 2 out of 3 skills
            }
        ]
        recommendations = list(self.recommender.generate_recommendations())
        self.assertEqual(len(recommendations), 3)
        for rec in expected:
            self.assertIn(rec, recommendations)

    def test_sort_recommendations(self):
        """Test that recommendations are sorted correctly."""
        sorted_recommendations = list(self.recommender.generate_recommendations())

        expected_order = [
            {
                'jobseeker_id': 1,
                'jobseeker_name': 'Alice',
                'job_id': 1,
                'job_title': 'Python Developer',
                'matching_skill_count': 1,
                'matching_skill_percent': 33
            },
            {
                'jobseeker_id': 1,
                'jobseeker_name': 'Alice',
                'job_id': 3,
                'job_title': 'Data Analyst',
                'matching_skill_count': 1,
                'matching_skill_percent': 33
            },
            {
                'jobseeker_id': 2,
                'jobseeker_name': 'Bob',
                'job_id': 2,
                'job_title': 'Java Developer',
                'matching_skill_count': 2,
                'matching_skill_percent': 67
            }
        ]

        self.assertEqual(sorted_recommendations, expected_order)

if __name__ == '__main__':
    unittest.main()
