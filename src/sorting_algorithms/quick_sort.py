from tests.sorting_tests import run_tests


def partition(array: list[int], left: int, right: int) -> int:
    pivot: int = array[right]
    i: int = left - 1
    for j in range(left, right):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


def quick_sort(array: list[int], left: int, right: int) -> None:
    """
        # Quick Sort
        ### Complexities:
        ```py
        Worst Case Time Complexity == O(n^2)
        Average Case Time Complexity == O(n log n)
        Best Case Time Complexity == O(n log n)
        Space Complexity == O(n)
        ```
    """
    
    if left >= right:
        return
    
    # Divide & Conquer
    part = partition(array=array, left=left, right=right)
    quick_sort(array=array, left=left, right=part-1)
    quick_sort(array=array, left=part+1, right=right)


if __name__ == "__main__":
    run_tests(quick_sort)