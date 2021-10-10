from test import run_tests
from typing import List


def partition(array: List[int], left: int, right: int) -> int:
    pivot: int = array[right]
    i: int = left - 1
    for j in range(left, right):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


def quick_sort(array: List[int], left: int, right: int) -> None:
    """
        Quick Sort: O(n^2)
    """
    if left >= right:
        return
    
    # Divide & Conquer
    part = partition(array=array, left=left, right=right)
    quick_sort(array=array, left=left, right=part-1)
    quick_sort(array=array, left=part+1, right=right)


if __name__ == "__main__":
    run_tests(quick_sort)