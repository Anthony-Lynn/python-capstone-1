from src.main import Submission, filter_by_date, filter_by_student_id, find_unsubmitted, get_average_score, get_average_score_by_module

submission_1: Submission = {
  "quiz_module": "Statistics",
  "quiz_name": "Find Average",
  "quiz_score": 40.6,
  "student_id": 18650400,
  "student_name": "Carol",
  "submission_date": "09/27/2013"
}

submission_2: Submission = {
  "quiz_module": "History",
  "quiz_name": "Find Average",
  "quiz_score": 10.4,
  "student_id": 18650400,
  "student_name": "Carol",
  "submission_date": "08/28/2020"
}

submission_3: Submission = {
  "quiz_module": "Algebra",
  "quiz_name": "Find Average",
  "quiz_score": 6.8,
  "student_id": 18650400,
  "student_name": "Carol",
  "submission_date": "12/15/2017"
}

submission_4: Submission = {
  "quiz_module": "History",
  "quiz_name": "Find Average",
  "quiz_score": 78.7,
  "student_id": 79090787,
  "student_name": "Alaiya",
  "submission_date": "07/27/2014"
}

submission_5: Submission = {
  "quiz_module": "Algebra",
  "quiz_name": "Find Average",
  "quiz_score": 31.6,
  "student_id": 44540177,
  "student_name": "Ada",
  "submission_date": "07/27/2014"
}

submission_6: Submission = {
  "quiz_module": "Algebra",
  "quiz_name": "Find Average",
  "quiz_score": 6.8,
  "student_id": 30831074,
  "student_name": "Savanna",
  "submission_date": "07/27/2014"
}

submission_7: Submission = {
  "quiz_module": "Statistics",
  "quiz_name": "Find Average",
  "quiz_score": 50.8,
  "student_id": 90019151,
  "student_name": "Ada",
  "submission_date": "02/28/2015"
}

submission_8: Submission = {
  "quiz_module": "Algebra",
  "quiz_name": "Find Average",
  "quiz_score": 55.7,
  "student_id": 34060603,
  "student_name": "Dulce",
  "submission_date": "07/15/2013"
}

submission_9: Submission = {
  "quiz_module": "Statistics",
  "quiz_name": "Find Average",
  "quiz_score": 100,
  "student_id": 98220764,
  "student_name": "Alaiya",
  "submission_date": "11/05/2012"
}

submission_10: Submission = {
  "quiz_module": "History",
  "quiz_name": "Find Average",
  "quiz_score": 0,
  "student_id": 90799374,
  "student_name": "Ada",
  "submission_date": "06/04/2013"
}

submissions: list[Submission] = [
  submission_1,
  submission_2,
  submission_3,
  submission_4,
  submission_5,
  submission_6,
  submission_7,
  submission_8,
  submission_9,
  submission_10
]

def test_filter_by_date_found_date():
  assert filter_by_date("07/27/2014", submissions) == [submission_4, submission_5, submission_6]

def test_filter_by_date_missing_date():
  assert filter_by_date("07/27/2025", submissions) == []

def test_filter_by_date_no_submissions():
  assert filter_by_date("07/27/2014", []) == []

def test_filter_by_student_id_found_id():
  assert filter_by_student_id(18650400, submissions) == [submission_1, submission_2, submission_3]

def test_filter_by_student_id_missing_id():
  assert filter_by_student_id(0, submissions) == []

def test_filter_by_student_id_no_submissions():
  assert filter_by_student_id(18650400, []) == []

def test_find_unsubmitted_find_unsubmitted():
  assert find_unsubmitted("07/27/2014", ["Ada", "Alaiya", "Carol"], submissions) == ["Carol"]

def test_find_unsubmitted_no_names():
  assert find_unsubmitted("07/27/2014", [], submissions) == []

def test_find_unsubmitted_no_submissions():
  assert find_unsubmitted("07/27/2025", ["Ada", "Alaiya", "Carol"], submissions) == []

def test_find_unsubmitted_missing_students():
  assert find_unsubmitted("07/27/2014", ["Mills", "Mike", "Mavrick"], submissions) == ["Mills", "Mike", "Mavrick"]

def test_get_average_score():
  pass

def test_get_average_score_by_module():
  pass