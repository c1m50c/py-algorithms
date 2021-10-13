from collections.abc import Callable
from random import randint


def get_method_name(method: Callable[[], any]) -> str:
    """
        # Get Method Name
        Returns the method's name as PascalCase, example below.
        ```py
        get_method_name(quick_sort()) # Returns "QuickSort".
        ```
        ### Parameters:
        ```py
        method: Callable[[], any] # Method you would like to get the name of.
        ```
    """
    string: str = method.__name__
    string_arr: list[str] = string.split("_")
    string = ""
    for s in string_arr:
        string += s.capitalize()
    return string


def get_array_as_str(array: list[any]) -> str:
    """
        # Get Array as String
        Formats an array to a nicely formatted string, example below.
        ```py
        get_array_as_str(array=[59, 3, 2, 13, 5]) # Returns "[59 .. 5]"
        ```
        ### Parameters:
        array: list[any] # Array you would like to format as a string.
    """
    return f"[{array[0]} .. {array[len(array) - 1]}]"


def create_integer_array(array: list[any], length: int = 1000, rand_min: int = -100, rand_max: int = 100) -> None:
    """
        # Create Integer Array
        Creates an array (list) to be used for testing sorting algorithms.
        ### Parameters:
        ```py
        array: list[any] # Array to fill with integers.
        length: int = 1000 # Desired array length.
        ```
    """
    array.clear()
    for i in range(0, length):
        array.append(randint(rand_min, rand_max))