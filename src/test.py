# Todo: Clean this up #

from colorama import Fore, Style, Back
from random import randint
from typing import List
from time import time


def sort_array(array: List[int], method) -> None:
    # Todo: This is a messy fix to the issue, fix later
    if method.__name__ == "quick_sort":
        method(array, 0, len(array) - 1)
    else:
        method(array)


def get_method_name(method) -> str:
    string: str = method.__name__
    string_arr: List[str] = string.split("_")
    string = ""
    for s in string_arr:
        string += s.capitalize()
    return string


def create_array(array: List[int], length: int = 1000) -> None:
    array.clear()
    for i in range(0, length):
        array.append(randint(-100, 100))


def get_array_as_str(array: List[int]) -> str:
    return f"[{array[0]} .. {array[len(array) - 1]}]"


def compare_arrays(array: List[int], method) -> None:
    print(f"{Fore.RED}Unsorted List: {get_array_as_str(array=array)}{Fore.RESET}")
    begin_time: float = time()
    sort_array(array=array, method=method)
    end_time: float = time()
    print(f"{Fore.GREEN}Sorted List: {get_array_as_str(array=array)}{Fore.RESET}")
    print(f"Time Elapsed: {end_time - begin_time}s")


def arr_is_arr(array_method_sorted: List[int], array_hand_sorted: List[int]) -> str:
    color, is_same = Fore.RED, False
    if array_method_sorted == array_hand_sorted:
        color, is_same = Fore.GREEN, True
    return f"{color}{get_array_as_str(array_method_sorted)} == {get_array_as_str(array_hand_sorted)} -> {is_same}{Fore.RESET}"



def assertion_tests(method) -> None:
    print(f"Assertion Tests:")
    array_one: List[int] = [-1, 2, 1, 3, -15, 0, 5, 12, 4, 6]
    array_two: List[int] = [0, 3, 4, 5, 6, 2, 33, 2, -66]
    array_three: List[int] = [-34, 4, 2, 0, 1, 15, 13]
    array_one_sorted: List[int] = [-15, -1, 0, 1, 2, 3, 4, 5, 6, 12]
    array_two_sorted: List[int] = [-66, 0, 2, 2, 3, 4, 5, 6, 33]
    array_three_sorted: List[int] = [-34, 0, 1, 2, 4, 13, 15]
    
    sort_array(array=array_one, method=method)
    sort_array(array=array_two, method=method)
    sort_array(array=array_three, method=method)
    
    print(f"{arr_is_arr(array_method_sorted=array_one, array_hand_sorted=array_one_sorted)}")
    print(f"{arr_is_arr(array_method_sorted=array_two, array_hand_sorted=array_two_sorted)}")
    print(f"{arr_is_arr(array_method_sorted=array_three, array_hand_sorted=array_three_sorted)}")


def run_tests(method) -> None:
    print(f"<====={get_method_name(method)}=====>")
    
    arr: List[int] = [  ]
    
    # List Length of 100 Test #
    create_array(array=arr, length=100)
    print(f"List of Length {len(arr)} Test:")
    compare_arrays(array=arr, method=method)
    print()
    
    # List Length of 1000 Test #
    create_array(array=arr, length=1000)
    print(f"List of Length {len(arr)} Test:")
    compare_arrays(array=arr, method=method)
    print()
    
    # List Length of 10000 Test #
    create_array(array=arr, length=10000)
    print(f"List of Length {len(arr)} Test:")
    compare_arrays(array=arr, method=method)
    print()
    
    # List Length of 100000 Test #
    create_array(array=arr, length=100000)
    print(f"List of Length {len(arr)} Test:")
    compare_arrays(array=arr, method=method)
    print()
    
    # Assertion Tests #
    assertion_tests(method)
    
    print(f"<==========>")