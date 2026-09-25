from typing import Callable
from src.util import filter, filter_property

def test_filter_int_is_even():
  list_1 = [1, 2, 3, 4]
  filter_func: Callable[[int], bool] = lambda x: x % 2 == 0

  assert filter(list_1, filter_func) == [2, 4]

def test_filter_string():
  list_1: list[str] = ["", "hello"]
  filter_func: Callable[[str], bool] = lambda x: bool(x)

  assert filter(list_1, filter_func) == []

def test_filter_empty_list():
  list_1: list[int] = []
  filter_func: Callable[[int], bool] = lambda x: x % 2 == 0

  assert filter(list_1, filter_func) == []

def test_filter_property_with_filter():
  list_1 = [{"key_value_1": False}, {"key_value_1": True}]
  filter_func: Callable[[bool], bool] = lambda x: x

  assert filter_property(list_1, "key_value_1", filter_func) == [{"key_value_1": True}]

def test_filter_property_no_error():
  list_1 = [{"key_value_1": False}, {"key_value_1": True}]
  filter_func: Callable[[bool], bool] = lambda x: x

  assert filter_property(list_1, "key_value_1", filter_func) == [{"key_value_1": True}]

def test_is_equal():
  pass

def test_is_unequal():
  pass

def test_has_element():
  pass

def test_contains():
  pass

def test_get_property_list():
  pass

def test_average():
  pass