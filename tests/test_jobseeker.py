"""
Unit tests for the Jobseeker class.
"""

import unittest
from jobmatch.jobseeker import Jobseeker

class TestJobseeker(unittest.TestCase):
    """Tests for the Jobseeker class."""

    def test_initialization_with_string_skills(self):
        """Test initialization of a Jobseeker instance with skills as a string."""
        seeker = Jobseeker(
            id=1,
            name='Alice',
            skills='Python, SQL, Problem Solving'
        )
        self.assertEqual(seeker.id, 1)
        self.assertEqual(seeker.name, 'Alice')
        self.assertEqual(seeker.skills, {'python', 'sql', 'problem solving'})

    def test_initialization_with_set_skills(self):
        """Test initialization of a Jobseeker instance with skills as a set."""
        seeker = Jobseeker(id=2, name='Bob', skills={'Java', 'Teamwork'})
        self.assertEqual(seeker.id, 2)
        self.assertEqual(seeker.name, 'Bob')
        self.assertEqual(seeker.skills, {'java', 'teamwork'})

    def test_post_init_cleaning(self):
        """Test that name and skills are properly cleaned."""
        seeker = Jobseeker(
            id='3',
            name='  Charlie  ',
            skills='  Java , SQL , Problem Solving '
        )
        self.assertEqual(seeker.id, 3)
        self.assertEqual(seeker.name, 'Charlie')
        self.assertEqual(seeker.skills, {'java', 'sql', 'problem solving'})


if __name__ == '__main__':
    unittest.main()
