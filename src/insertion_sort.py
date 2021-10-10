from test import run_tests
from typing import List


def insertion_sort(array: List[int]) -> None:
    """
        Insertion Sort: O(n^2)
    """
    for i in range(1, len(array)):
        j: int = i
        while array[j - 1] > array[j] and j > 0:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1


if __name__ == "__main__":
    run_tests(insertion_sort)