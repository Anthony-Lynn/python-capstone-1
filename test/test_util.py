from typing import Callable
from src.util import filter, filter_property, is_equal, in_list, get_property_list, average, has_element, is_not
from pytest_mock import MockerFixture
from pytest import raises

# filter
def test_filter_int():
  list_1 = [0, 1]
  filter_func: Callable[[int], bool] = lambda x: bool(x)

  assert filter(list_1, filter_func) == [1]

def test_filter_string():
  list_1 = ["", "hello"]
  filter_func: Callable[[str], bool] = lambda x: bool(x)

  assert filter(list_1, filter_func) == ["hello"]

def test_filter_empty_list():
  list_1: list[int] = []
  filter_func: Callable[[int], bool] = lambda x: bool(x)

  assert filter(list_1, filter_func) == []

# filter_property
def test_filter_property_no_error(mocker: MockerFixture):
  list_1: list[dict[str, bool]] = [{"key_value_1": False}, {"key_value_1": True}]
  filter_func: Callable[[bool], bool] = lambda x: x

  mock_filter = mocker.patch("src.util.filter")
  mock_filter.return_value = [{"key_value_1": True}]

  assert filter_property(list_1, "key_value_1", filter_func) == [{"key_value_1": True}]

def test_filter_property_filter_called(mocker: MockerFixture):
  list_1: list[dict[str, bool]] = [{"key_value_1": False}, {"key_value_1": True}]
  filter_func: Callable[[bool], bool] = lambda x: x

  mock_filter = mocker.patch("src.util.filter")

  filter_property(list_1, "key_value_1", filter_func)
  mock_filter.assert_called_once()

# is_equal
def test_is_equal_is_equal():
  assert is_equal(1)(1)

def test_is_equal_is_unequal():
  assert not is_equal(1)(2)

# has_element
def test_has_element_found_element():
  assert has_element([1, 2, 3], 1)

def test_has_element_no_element():
  assert not has_element([1, 2, 3], 4)

def test_has_element_empty_list():
  assert not has_element([], 1)

# in_list
def test_in_list_has_element():
  list_1 = [1, 2, 3]
  assert in_list(list_1)(1)

def test_in_list_missing_element():
  list_1 = [1, 2, 3]
  assert not in_list(list_1)(4)

# is_not
def test_is_not_gives_false_when_true():
  not_func: Callable[[bool], bool] = is_not(lambda x: x)
  assert not_func(True) == False

def test_is_not_gives_true_when_false():
  not_func: Callable[[bool], bool] = is_not(lambda x: x)
  assert not_func(False) == True

# get_property_list
def test_get_property_list_gives_property_values():
  list_1 = [{"key_value_1": False}, {"key_value_1": True}]

  assert get_property_list(list_1, "key_value_1") == [False, True]

def test_get_property_list_empty_list():
  list_1: list[dict[str, bool]] = []

  assert get_property_list(list_1, "key_value_1") == []

def test_get_property_list_wrong_key():
  list_1 = [{"key_value_1": False}, {"key_value_1": True}]

  with raises(KeyError):
    get_property_list(list_1, "key_value_2")

# average
def test_average_gets_average():
  assert average([10, 20, 30, 40, 50]) == 30

def test_average_empty_list_is_zero():
  assert average([]) == 0