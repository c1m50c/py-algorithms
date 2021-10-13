from sorting_algorithms.merge_sort import merge_sort
from collections.abc import Callable
from sys import setrecursionlimit
from colorama import Fore, Style
from .helper_functions import *
from time import time


def get_color(found: int) -> Fore:
    """
        # Get Color
        Returns Red or Green Foreground color depending on if the item was found within the array.
        ### Parameters:
        ```py
        found: int # Return value from a searching algorithm.
        ```
    """
    if found <= -1:
        return Fore.RED
    return Fore.GREEN


def speed_test(array: list[any], method: Callable[[list[any], any], int], sorting_method: Callable[[list[int]], None] = merge_sort, length: int = 100) -> None:
    """
        # Speed Test
        Tests a searching algorithm's speed by searching through an array of size `length`.
        ### Parameters:
        ```py
        array: list[any] # Array to search, will be created upon function call with `create_integer_array`.
        method: Callable[[list[any], any], int] # Searching Algorithm method.
        sorting_method: Callable[[list[int]], None] = merge_sort # Method for sorting the array, used when a Searching Algorithm requires the array to be sorted.
        length: int = 100 # Determines the length of the array when created.
        ```
    """
    print(f"{Style.DIM}Search Speed Test{Style.RESET_ALL}")
    
    RAND_MIN: int = -20000
    RAND_MAX: int = 20000
    
    create_integer_array(array=array, length=length, rand_min=RAND_MIN, rand_max=RAND_MAX)
    if method.__name__ in ["binary_search"]:
        # Sort Array for search algorithms that require sorting.
        print(f"Pre-Sorting Array with {Fore.BLUE}{Style.BRIGHT}'{get_method_name(sorting_method)}'{Fore.RESET}{Style.RESET_ALL}.")
        begin_time: float = time()
        sorting_method(array)
        end_time: float = time()
        print(f"{Fore.GREEN}Sorted Array in {end_time - begin_time}s{Fore.RESET}")
    
    print(f"{Fore.YELLOW}Array Length: {Style.BRIGHT}'{len(array)}'{Style.NORMAL}.{Fore.RESET}")
    begin_time: float = time()
    finding: int = randint(a=RAND_MIN, b=RAND_MAX)
    found = method(array, finding)
    end_time: float = time()
    print(f"{get_color(found=found)}Searched for {Style.BRIGHT}'{finding}'{Style.NORMAL}, found at index {Style.BRIGHT}'{found}'{Style.RESET_ALL}{Fore.RESET}.")
    print(f"Time Elapsed: {end_time - begin_time}s")


def run_tests(method: Callable[[list[any], any], int]) -> None:
    """
        # Run Tests
        Runs tests to ensure the searching algorithm method can properly search, it also tests their speed.
        ### Parameters:
        ```py
        method: Callable[[list[any], any], int] # Searching Algorithm Method.
        ```
    """
    setrecursionlimit(5000) # Handy to have this higher then default limit, be cautious of crashes when too high though
    print(f"{Style.BRIGHT}{Fore.YELLOW}<====={Fore.CYAN}{get_method_name(method)}{Fore.YELLOW}=====>{Fore.RESET}{Style.RESET_ALL}")
    
    arr: list[int] = [  ]
    
    # Speed Tests
    speed_test(array=arr, method=method, length=1000)
    print()
    speed_test(array=arr, method=method, length=10000)
    print()
    speed_test(array=arr, method=method, length=100000)
    print()
    speed_test(array=arr, method=method, length=500000)
    print()
    speed_test(array=arr, method=method, length=750000)
    print()
    speed_test(array=arr, method=method, length=1000000)
    
    print(f"{Style.BRIGHT}{Fore.YELLOW}<==========>{Fore.RESET}{Style.RESET_ALL}")