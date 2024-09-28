"""
Main module to run the job match recommendation engine.
Reads data, generates recommendations, and outputs the results.
"""

import argparse
import os
import json
from jobmatch.utils import read_jobseekers, read_jobs
from jobmatch.recommender import Recommender


def parse_arguments():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description='Job Match Recommendation Engine')
    parser.add_argument('--jobseekers', type=str, default='data/jobseekers.csv',
                        help='Path to the jobseekers CSV file')
    parser.add_argument('--jobs', type=str, default='data/jobs.csv',
                        help='Path to the jobs CSV file')
    parser.add_argument('--jobseeker_id', type=int,
                        help='ID of the jobseeker to generate recommendations for')
    parser.add_argument('--jobseeker_name', type=str,
                        help='Name of the jobseeker to generate recommendations for')
    return parser.parse_args()


def main():
    """Main function to execute the recommendation engine."""
    args = parse_arguments()

    # Check if the input files exist
    if not os.path.isfile(args.jobseekers):
        print(f"Jobseekers file not found: {args.jobseekers}")
        return
    if not os.path.isfile(args.jobs):
        print(f"Jobs file not found: {args.jobs}")
        return

    # Read jobs into memory (assuming manageable size)
    jobs = read_jobs(args.jobs)

    # Read jobseekers as a generator
    jobseekers_gen = read_jobseekers(args.jobseekers)

    # Filter jobseekers if ID or name is specified
    if args.jobseeker_id is not None:
        jobseekers = (js for js in jobseekers_gen if js.id == args.jobseeker_id)
    elif args.jobseeker_name:
        jobseekers = (js for js in jobseekers_gen if js.name.lower() == args.jobseeker_name.lower())
    else:
        jobseekers = jobseekers_gen  # Use the full generator

    recommender = Recommender(jobseekers, jobs)
    recommendations = recommender.generate_recommendations(include_skills=True)

    # Output the recommendations as they are generated
    print('jobseeker_id, jobseeker_name, job_id, job_title, matching_skill_count, '
          'matching_skill_percent, matched_skills, unmatched_skills')
    for rec in recommendations:
        matched_skills = rec['matched_skills'] if rec['matched_skills'] else []
        unmatched_skills = rec['unmatched_skills'] if rec['unmatched_skills'] else []
        matched_skills_str = json.dumps(matched_skills)
        unmatched_skills_str = json.dumps(unmatched_skills)
        print(f"{rec['jobseeker_id']}, {rec['jobseeker_name']}, {rec['job_id']}, "
              f"{rec['job_title']}, {rec['matching_skill_count']}, "
              f"{rec['matching_skill_percent']}, "
              f"{matched_skills_str}, {unmatched_skills_str}")


if __name__ == '__main__':
    main()
