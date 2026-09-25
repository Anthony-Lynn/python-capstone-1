from typing import TypedDict, Callable, Any, cast, Mapping

class Submission(TypedDict):
  quiz_name: str
  quiz_module: str
  quiz_score: float
  student_id: int
  student_name: str
  submission_date: str

# util functions

def filter_property[T: Mapping[str, Any], K](elements: list[T], property: str, func: Callable[[K], bool]) -> list[T]:
  # list comprehension
  return [
    element for element in elements
      if func(cast(K, element[property]))
  ]

def is_equal(value: Any) -> Callable[[Any], bool]:
  return lambda compare: compare == value

def is_unequal(value: Any) -> Callable[[Any], bool]:
  return lambda compare: compare != value

def has_element[T](elements: list[T], has_item: T) -> bool:
  for element in elements:
    if element == has_item:
      return True

  return False

def contains[T](elements: list[T]) -> Callable[[T], bool]:
  return lambda has_item: has_element(elements, has_item)

def get_property_list[T: Mapping[str, Any]](elements: list[T], property: str) -> list[Any]:
  # list comprehension
  return [element[property] for element in elements]

def average(numbers: list[int | float]) -> float:
  sum = 0

  for number in numbers:
    sum += number

  return sum / len(numbers)

# helper functions

def filter_by_date(submission_date: str, submissions: list[Submission]) -> list[Submission]:
  return filter_property(submissions, "submission_date", is_equal(submission_date))

def filter_by_student_id(student_id: int, submissions: list[Submission]) -> list[Submission]:
  return filter_property(submissions, "student_id", is_equal(student_id))

def find_unsubmitted(submission_date: str, student_names: list[str], submissions: list[Submission]) -> list[str]:
  submissions_not_on_date = filter_property(submissions, "submission_date", is_unequal(submission_date))
  submissions_with_student_names = filter_property(submissions_not_on_date, "student_name", contains(student_names))
  
  return get_property_list(submissions_with_student_names, "student_name")

def get_average_score(submissions: list[Submission]) -> float:
  scores = get_property_list(submissions, "quiz_score")

  # TODO: precision of 1 decimal place
  return average(scores)

def get_average_score_by_module(submissions: list[Submission]) -> dict[str, float]:
  module_average_scores: dict[str, float] = {}

  for submission in submissions:
    module = submission["quiz_module"]
    score = submission["quiz_score"]
    if module_average_scores[module]:
      module_average_scores[module] += score
    else:
      module_average_scores[module] = score

  return module_average_scores