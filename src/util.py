from typing import Callable, Any, Mapping

def filter[T](elements: list[T], func: Callable[[T], bool]) -> list[T]:
  """
  Filter a list based on a functions return value of the elements.

  Args:
    elements (list[T]): The list to evaluate.
    func (Callable[[T], bool]): The function used to filter each value.

  Returns:
    list[T]: A new list thats elements passed true in the function.
  """
  return [
    element for element in elements
      if func(element)
  ]

# Would love to get rid of the Any type here, but not sure how...
def filter_property[T: Mapping[str, Any], K](elements: list[T], property: str, func: Callable[[K], bool]) -> list[T]:
  """
  Filter a list of dictionaries based on a functions return value of the specified property.

  Args:
    elements (list[T]): The list of dictionaries to evaluate.
    property (str): The key name within each dictionary whose value will be evaluated.
    func (Callable[[K], bool]): The function used to test the property value.

  Returns:
    list[T]: A new list of dictionaries whose property value passed true in the function.
  """
  filter_func: Callable[[T], bool] = lambda x: func(x[property])
  return filter(elements, filter_func)

def is_equal(value: Any) -> Callable[[Any], bool]:
  """
  Get a function that checks if a argument is equal to the value.

  Args:
    value (Any): The first value to compare to.

  Returns:
    Callable[[Any], bool]: A function that returns whether the argument passed is equal to the value.
  """
  return lambda compare: compare == value

def has_element[T](elements: list[T], item: T) -> bool:
  """
  Check if a argument is within the list.

  Args:
    elements (list[T]): The list to check if the argument is within.
    item (T): The item to check for.

  Returns:
    bool: Whether or not the element is within the list
  """
  for element in elements:
    if element == item:
      return True

  return False

def in_list[T](elements: list[T]) -> Callable[[T], bool]:
  """
  Get a function that checks if an argument is within the list.

  Args:
    elements (list[T]): The list to check if the argument is within.

  Returns:
    Callable[[T], bool]: A function that returns whether the argument passed is in the list.
  """
  return lambda element: has_element(elements, element)

def is_not[T](func: Callable[[T], bool]) -> Callable[[T], bool]:
  """
  Get a function that returns the not value of the function given.

  Args:
    func (Callable[[T], bool]): The function to apply the not to

  Returns:
    Callable[[T], bool]: The function that's identical to the one passed in but has its boolean return value flipped
  """
  return lambda value: not func(value)

# Would love to get rid of the Any types here, but not sure how...
def get_property_list[T: Mapping[str, Any]](elements: list[T], property: str) -> list[Any]:
  """
  Map a list of dictionaries to a list of property values.

  Args:
    elements (list[T]): The list of dictionaries to be mapped.
    property (str): The shared property of dictionaries to map to the new list.

  Returns:
    list[Any]: The new list containing the property values of the dictionaries.
  """
  return [element[property] for element in elements]

def average(numbers: list[int | float]) -> float:
  """
  Get the average of numbers.

  Args:
    numbers (list[int | float]): The list of numbers to find the average of.

  Returns:
    float: The average of numbers passed.
  """
  if len(numbers) == 0:
    return 0

  sum = 0

  for number in numbers:
    sum += number

  return sum / len(numbers)