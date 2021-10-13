from tests.sorting_tests import run_tests
from sorting_algorithms import quick_sort
from threading import Thread
from colorama import Style


def threaded_quick_sort(array: list[int], threads: int = 2) -> None:
    """
        # Threaded Quick Sort
        The quick sort algorithm with multi-threading.
        ### Parameters:
        ```py
        array: list[int] # The Array you would like to sort.
        left: int # Left position, usually set to the first index of the Array.
        right: int # Right position, usually set to the last index of the Array.
        ```
        ### Complexities:
        ```py
        Worst Case Time Complexity == O(n^2)
        Average Case Time Complexity == O(n log n)
        Best Case Time Complexity == O(n log n)
        Space Complexity == O(n)
        ```
    """

if __name__ == "__main__":
    run_tests(threaded_quick_sort)