"""
Unit tests for the utility functions in utils.py.
"""

import unittest
import os
from jobmatch.utils import read_jobseekers, read_jobs
from jobmatch.jobseeker import Jobseeker
from jobmatch.job import Job


class TestUtils(unittest.TestCase):
    """Tests for utility functions."""

    def setUp(self):
        """Create temporary CSV files for testing."""
        self.jobseekers_csv = 'test_jobseekers.csv'
        with open(self.jobseekers_csv, 'w', encoding='utf-8') as f:
            f.write('id,name,skills\n')
            f.write('1,Alice Seeker,"Python, SQL, Problem Solving"\n')
            f.write('2,Bob Applicant,"Java, Teamwork"\n')

        self.jobs_csv = 'test_jobs.csv'
        with open(self.jobs_csv, 'w', encoding='utf-8') as f:
            f.write('id,title,required_skills\n')
            f.write('1,Python Developer,"Python, Django, REST"\n')
            f.write('2,Java Developer,"Java, Spring, Teamwork"\n')

    def tearDown(self):
        """Remove temporary CSV files after testing."""
        os.remove(self.jobseekers_csv)
        os.remove(self.jobs_csv)

    def test_read_jobseekers(self):
        """Test reading jobseekers from a CSV file."""
        jobseekers = list(read_jobseekers(self.jobseekers_csv))
        self.assertEqual(len(jobseekers), 2)
        self.assertIsInstance(jobseekers[0], Jobseeker)
        self.assertEqual(jobseekers[0].id, 1)
        self.assertEqual(jobseekers[0].name, 'Alice Seeker')
        self.assertEqual(jobseekers[0].skills, {'python', 'sql', 'problem solving'})

    def test_read_jobs(self):
        """Test reading jobs from a CSV file."""
        jobs = read_jobs(self.jobs_csv)
        self.assertEqual(len(jobs), 2)
        self.assertIsInstance(jobs[0], Job)
        self.assertEqual(jobs[0].id, 1)
        self.assertEqual(jobs[0].title, 'Python Developer')
        self.assertEqual(jobs[0].required_skills, {'python', 'django', 'rest'})

    def test_read_jobseekers_file_not_found(self):
        """Test reading jobseekers from a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            jobseekers = read_jobseekers('non_existent_file.csv')
            # Consume the generator to trigger the exception
            list(jobseekers)

    def test_read_jobs_file_not_found(self):
        """Test reading jobs from a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            read_jobs('non_existent_file.csv')


if __name__ == '__main__':
    unittest.main()
