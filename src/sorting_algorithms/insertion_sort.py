from tests.sorting_tests import run_tests


def insertion_sort(array: list[int]) -> None:
    """
        # Insertion Sort
        ### Parameters:
        ```py
        array: list[int] # The Array you would like to sort.
        ```
        ### Complexities:
        ```py
        Worst Case Time Complexity == O(n^2)
        Average Case Time Complexity == O(n^2)
        Best Case Time Complexity == O(n)
        Space Complexity == O(n) total, O(1) auxiliary
        ```
    """
    
    for i in range(1, len(array)):
        j: int = i
        while array[j - 1] > array[j] and j > 0:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1


if __name__ == "__main__":
    run_tests(insertion_sort)