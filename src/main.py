from typing import TypedDict
from src.util import in_list, average, get_property_list, filter_property, is_equal, filter, is_not

class Submission(TypedDict):
  quiz_name: str
  quiz_module: str
  quiz_score: float
  student_id: int
  student_name: str
  submission_date: str

def filter_by_date(submission_date: str, submissions: list[Submission]) -> list[Submission]:
  """
  Filter a list of submissions by date.

  Args:
    submission_date (str): The date to check each submission against.

  Returns:
    list[Submission]: A new list of submissions thats date is equal to.
  """
  return filter_property(submissions, "submission_date", is_equal(submission_date))

def filter_by_student_id(student_id: int, submissions: list[Submission]) -> list[Submission]:
  """
  Filter a list of submissions by student id.

  Args:
    student_id (int): The student id to check each submission against.

  Returns:
    list[Submission]: A new list of submissions thats student id is equal to.
  """
  return filter_property(submissions, "student_id", is_equal(student_id))

# TODO: Check the names list is what's being modified, names may not be in submissions.
def find_unsubmitted(submission_date: str, student_names: list[str], submissions: list[Submission]) -> list[str]:
  """
  Get a list of student names who match the passed student names and haven't had a submission on the date.

  Args:
    submission_date (str): The date to check submissions on.
    student_names (list[str]): The names of students to check for.
    submissions (list[Submission]): The submissions to check against.

  Returns:
    list[str]: A new list of student names that haven't submitted on the specified date.
  """
  submissions_on_date = filter_property(submissions, "submission_date", is_equal(submission_date))
  submitted_students: list[str] = get_property_list(submissions_on_date, "student_name")
  unsubmitted_names = filter(student_names, is_not(in_list(submitted_students)))
  
  return unsubmitted_names

def get_average_score(submissions: list[Submission]) -> float:
  """
  Get average score of submissions.

  Args:
    submissions (list[Submission]): The submissions to get the average score of.

  Returns:
    float: An average score of the submissions.
  """
  scores = get_property_list(submissions, "quiz_score")
  average_score = average(scores)

  return round(average_score, 1)

def get_average_score_by_module(submissions: list[Submission]) -> dict[str, float]:
  """
  Get average score of submissions categorized by module.

  Args:
    submissions (list[Submission]): The submissions to get the average score of.

  Returns:
    dict[str, float]: The modules and their average scores
  """
  # Categorize the modules scores into their own lists
  module_scores: dict[str, list[float]] = {}
  for submission in submissions:
    module = submission["quiz_module"]
    if not module_scores[module]:
      module_scores[module] = []
    
    module_scores[module].append(submission["quiz_score"])

  # Find the average of the lists
  module_average_scores: dict[str, float] = {}
  for module, scores in module_scores.items():
    module_average_scores[module] = average(scores)
  
  return module_average_scores
