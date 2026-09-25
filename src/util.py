from typing import Callable, Any, Mapping

def filter[T](elements: list[T], func: Callable[[T], bool]) -> list[T]:
  return [
    element for element in elements
      if func(element)
  ]

# Would love to get rid of the Any types here, but not sure how...
def filter_property[T: Mapping[str, Any], K](elements: list[T], property: str, func: Callable[[K], bool]) -> list[T]:
  """
  Filter a list of dicts based on a function passed with the property value.

  Args:
    elements (list[T]): The list of mapping objects to evaluate.
    property (str): The key name within each dict whose value will be evaluated.
    func (Callable[[K], bool]): The predicate function used to test the property value.

  Returns:
    list[T]: A new list containing only the mapping objects whose specified property satisfies the predicate.
  """
  filter_func: Callable[[T], bool] = lambda x: func(x[property])
  return filter(elements, filter_func)

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

# Would love to get rid of the Any types here, but not sure how...
def get_property_list[T: Mapping[str, Any]](elements: list[T], property: str) -> list[Any]:
  return [element[property] for element in elements]

def average(numbers: list[int | float]) -> float:
  sum = 0

  for number in numbers:
    sum += number

  return sum / len(numbers)