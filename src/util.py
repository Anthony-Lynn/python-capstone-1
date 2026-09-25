from typing import Callable, Any, cast, Mapping

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