# Todo: Clean this up #

from colorama import Fore, Style, Back
from sys import setrecursionlimit
from random import randint
from time import time


def sort_array(array: list[int], method) -> None:
    # Todo: This is a messy fix to the issue, fix later
    if method.__name__ == "quick_sort":
        method(array, 0, len(array) - 1)
    else:
        method(array)


def get_method_name(method) -> str:
    string: str = method.__name__
    string_arr: list[str] = string.split("_")
    string = ""
    for s in string_arr:
        string += s.capitalize()
    return string


def create_array(array: list[int], length: int = 1000) -> None:
    array.clear()
    for i in range(0, length):
        array.append(randint(-100, 100))


def get_array_as_str(array: list[int]) -> str:
    return f"[{array[0]} .. {array[len(array) - 1]}]"


def compare_arrays(array: list[int], method) -> None:
    print(f"{Fore.RED}Unsorted List: {get_array_as_str(array=array)}{Fore.RESET}")
    begin_time: float = time()
    sort_array(array=array, method=method)
    end_time: float = time()
    print(f"{Fore.GREEN}Sorted List: {get_array_as_str(array=array)}{Fore.RESET}")
    print(f"Time Elapsed: {end_time - begin_time}s")


def arr_is_arr(array_method_sorted: list[int], array_hand_sorted: list[int]) -> str:
    color, is_same = Fore.RED, False
    if array_method_sorted == array_hand_sorted:
        color, is_same = Fore.GREEN, True
    return f"{color}{get_array_as_str(array_method_sorted)} == {get_array_as_str(array_hand_sorted)} -> {is_same}{Fore.RESET}"


def assertion_tests(method) -> None:
    print(f"Assertion Tests:")
    array_one: list[int] = [-1, 2, 1, 3, -15, 0, 5, 12, 4, 6]
    array_two: list[int] = [0, 3, 4, 5, 6, 2, 33, 2, -66]
    array_three: list[int] = [-34, 4, 2, 0, 1, 15, 13]
    array_four: list[int] = [-9, -9, -8, -1, -3, -5, -0]
    array_five: list[int] = [0, 5, 2, 3, 2, 9, 8, 4, 9, 7]
    array_one_sorted: list[int] = [-15, -1, 0, 1, 2, 3, 4, 5, 6, 12]
    array_two_sorted: list[int] = [-66, 0, 2, 2, 3, 4, 5, 6, 33]
    array_three_sorted: list[int] = [-34, 0, 1, 2, 4, 13, 15]
    array_four_sorted: list[int] = [-9, -9, -8, -5, -3, -1, -0]
    array_five_sorted: list[int] = [0, 2, 2, 3, 4, 5, 7, 8, 9, 9]
    
    sort_array(array=array_one, method=method)
    sort_array(array=array_two, method=method)
    sort_array(array=array_three, method=method)
    sort_array(array=array_four, method=method)
    sort_array(array=array_five, method=method)
    
    print(f"{arr_is_arr(array_method_sorted=array_one, array_hand_sorted=array_one_sorted)}")
    print(f"{arr_is_arr(array_method_sorted=array_two, array_hand_sorted=array_two_sorted)}")
    print(f"{arr_is_arr(array_method_sorted=array_three, array_hand_sorted=array_three_sorted)}")
    print(f"{arr_is_arr(array_method_sorted=array_four, array_hand_sorted=array_four_sorted)}")
    print(f"{arr_is_arr(array_method_sorted=array_five, array_hand_sorted=array_five_sorted)}")


def run_tests(method) -> None:
    setrecursionlimit(5000)
    print(f"{Style.BRIGHT}{Fore.YELLOW}<====={Fore.CYAN}{get_method_name(method)}{Fore.YELLOW}=====>{Fore.RESET}{Style.RESET_ALL}")
    
    arr: list[int] = [  ]
    
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
    # Skip slow algorithms, this test will butcher them.
    if method.__name__ not in ["insertion_sort", "selection_sort", "bubble_sort"]:
        create_array(array=arr, length=100000)
        print(f"List of Length {len(arr)} Test:")
        compare_arrays(array=arr, method=method)
        print()
    else:
        print("Skipping Test cause specified algorithm is too slow.")
        print()
    
    # List Length of 1000000 Test #
    # Skip slow algorithms, this test will butcher them.
    if method.__name__ not in ["insertion_sort", "selection_sort", "bubble_sort", "quick_sort"]:
        # We skip 'quick_sort' cause in my testing it crashes python on one million, maybe to recurssive?
        create_array(array=arr, length=1000000)
        print(f"List of Length {len(arr)} Test:")
        compare_arrays(array=arr, method=method)
        print()
    else:
        print("Skipping Test cause specified algorithm is too slow.")
        print()
    
    # Assertion Tests #
    assertion_tests(method)
    
    print(f"{Style.BRIGHT}{Fore.YELLOW}<==========>{Fore.RESET}{Style.RESET_ALL}")