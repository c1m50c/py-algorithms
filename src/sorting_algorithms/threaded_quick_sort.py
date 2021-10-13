from sorting_algorithms.quick_sort import quick_sort
from tests.sorting_tests import run_tests
from threading import Thread
from colorama import Style


def threaded_quick_sort(array: list[int]) -> None:
    """
        # Threaded Quick Sort
        The quick sort algorithm with multi-threading.
        ### Parameters:
        ```py
        array: list[int] # The Array you would like to sort.
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