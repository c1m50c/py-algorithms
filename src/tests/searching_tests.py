from sorting_algorithms.merge_sort import merge_sort
from collections.abc import Callable
from sys import setrecursionlimit
from colorama import Fore, Style
from .helper_functions import *
from time import time


def speed_test(array: list[any], method: Callable[[list[any], any], int], sorting_method: Callable[[list[int]], None] = merge_sort, length: int = 100) -> None:
    print(f"Search Speed Test")
    
    RAND_MIN: int = -1000
    RAND_MAX: int = 1000
    
    # Array Length of 10000 Test #
    create_integer_array(array=array, length=length, rand_min=RAND_MIN, rand_max=RAND_MAX)
    if method.__name__ in ["binary_search"]:
        print(f"Pre-Sorting Array with '{get_method_name(sorting_method)}'.")
        sorting_method(array)
    print(f"Array Length: '{len(array)}'.")
    begin_time: float = time()
    finding: int = randint(a=RAND_MIN, b=RAND_MAX)
    found = method(array, finding)
    end_time: float = time()
    print(f"Searched for '{finding}', found at index '{found}'.")
    print(f"Time Elapsed: {end_time - begin_time}s")


def run_tests(method: Callable[[list[any], any], int]) -> None:
    setrecursionlimit(5000) # Handy to have this higher then default limit, be cautious of crashes when too high though
    print(f"{Style.BRIGHT}{Fore.YELLOW}<====={Fore.CYAN}{get_method_name(method)}{Fore.YELLOW}=====>{Fore.RESET}{Style.RESET_ALL}")
    
    arr: list[int] = [  ]
    
    # Speed Test
    speed_test(array=arr, method=method, length=10000)
    
    print(f"{Style.BRIGHT}{Fore.YELLOW}<==========>{Fore.RESET}{Style.RESET_ALL}")