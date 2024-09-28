"""
Unit tests for the Job class.
"""

import unittest
from jobmatch.job import Job


class TestJob(unittest.TestCase):
    """Tests for the Job class."""

    def test_initialization_with_string_skills(self):
        """Test initialization of a Job instance with skills as a string."""
        job = Job(
            id=1,
            title='Python Developer',
            required_skills='Python, Django, REST'
        )
        self.assertEqual(job.id, 1)
        self.assertEqual(job.title, 'Python Developer')
        self.assertEqual(job.required_skills, {'python', 'django', 'rest'})

    def test_initialization_with_set_skills(self):
        """Test initialization of a Job instance with skills as a set."""
        job = Job(
            id=2,
            title='Data Scientist',
            required_skills={'Python', 'Machine Learning'}
        )
        self.assertEqual(job.id, 2)
        self.assertEqual(job.title, 'Data Scientist')
        self.assertEqual(job.required_skills, {'python', 'machine learning'})

    def test_post_init_cleaning(self):
        """Test that title and skills are properly cleaned."""
        job = Job(
            id='3',
            title='  Data Engineer  ',
            required_skills='  Python , SQL , ETL '
        )
        self.assertEqual(job.id, 3)
        self.assertEqual(job.title, 'Data Engineer')
        self.assertEqual(job.required_skills, {'python', 'sql', 'etl'})


if __name__ == '__main__':
    unittest.main()
