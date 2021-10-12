from collections.abc import Callable


def get_method_name(method: Callable[[], any]) -> str:
    """
        # Get Method Name
        Returns the method's name as PascalCase, example below.
        ```py
        get_method_name(quick_sort()) # Returns "QuickSort"
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