from sorting_algorithms.merge_sort import merge_sort
from collections.abc import Callable
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


def speed_test(method: Callable[[list[any], any], int], sorting_method: Callable[[list[int]], None] = merge_sort, length: int = 100) -> None:
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
    
    array: list[any] = [  ]
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


def assert_compare(method: Callable[[list[any], any], int], array: list[any], finding: any, idx: int) -> None:
    """
        # Assert Compare
        Compares searching algorithm findings to see if they correctly found an element within the given array.
        ### Parameters:
        ```py
        method: Callable[[list[any], any], int] # Searching Algorithm Method.
        array: list[any] # Array to be tested.
        finding: any # What we wanted to find.
        idx: int # Index of what we wanted to find.
        ```
    """
    
    found: int = method(array, finding)
    if found == idx and idx == -1: # Has been found but does not exist
        print(f"{Fore.GREEN}Element {Style.BRIGHT}'{finding}'{Style.NORMAL} does not exist in {Style.BRIGHT}'{get_array_as_str(array=array)}'{Style.NORMAL} at {Style.BRIGHT}'{idx}'{Style.RESET_ALL}.")
    elif found == idx: # Has been found
        print(f"{Fore.GREEN}Found {Style.BRIGHT}'{finding}'{Style.NORMAL} in {Style.BRIGHT}'{get_array_as_str(array=array)}'{Style.NORMAL} at index {Style.BRIGHT}'{found}'{Style.RESET_ALL}.")
    else: # Has not been found and does exist
        print(f"{Fore.RED}Did not find {Style.BRIGHT}'{finding}'{Style.NORMAL} in {Style.BRIGHT}'{get_array_as_str(array=array)}'{Style.NORMAL} at index {Style.BRIGHT}'{idx}'{Style.RESET_ALL}.")

def assertion_test(method: Callable[[list[any], any], int]) -> None:
    """
        # Assertion Test
        Used to ensure that the searching method is finding things properly, or just finding them at all.
        ### Parameters:
        ```py
        method: Callable[[list[any], any], int] # Searching Algorithm Method.
        ```
    """
    
    # Already sorted for algorithms like Binary Search #
    array_a, finding_a, idx_a = [ 0, 13, 23, 215, 532, 932], 932, 5
    array_b, finding_b, idx_b = [ 14, 29, 45, 46, 68, 92, 132 ], 29, 1
    array_c, finding_c, idx_c = [ 123, 456, 557, 559, 612, 722 ], 666, -1
    array_d, finding_d, idx_d = [ 100, 110, 120, 130, 140, 150 ], 130, 3
    array_e, finding_e, idx_e = [ 1, 2, 3, 3, 5, 9, 10, 11, 24, 29 ], 29, 9
    
    print(f"{Style.DIM}Assertion Test:{Style.RESET_ALL}")
    
    assert_compare(method=method, array=array_a, finding=finding_a, idx=idx_a)
    assert_compare(method=method, array=array_b, finding=finding_b, idx=idx_b)
    assert_compare(method=method, array=array_c, finding=finding_c, idx=idx_c)
    assert_compare(method=method, array=array_d, finding=finding_d, idx=idx_d)
    assert_compare(method=method, array=array_e, finding=finding_e, idx=idx_e)


def run_tests(method: Callable[[list[any], any], int]) -> None:
    """
        # Run Tests
        Runs tests to ensure the searching algorithm method can properly search, it also tests their speed.
        ### Parameters:
        ```py
        method: Callable[[list[any], any], int] # Searching Algorithm Method.
        ```
    """
    
    print(f"{Style.BRIGHT}{Fore.YELLOW}<====={Fore.CYAN}{get_method_name(method)}{Fore.YELLOW}=====>{Fore.RESET}{Style.RESET_ALL}")
    
    # Speed Tests
    speed_test(method=method, length=1000)
    print()
    speed_test(method=method, length=10000)
    print()
    speed_test(method=method, length=100000)
    print()
    speed_test(method=method, length=500000)
    print()
    speed_test(method=method, length=750000)
    print()
    speed_test(method=method, length=1000000)
    print()
    
    assertion_test(method=method)
    
    print(f"{Style.BRIGHT}{Fore.YELLOW}<==========>{Fore.RESET}{Style.RESET_ALL}")