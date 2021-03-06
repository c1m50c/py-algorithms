from tests.sorting_tests import run_tests


def bubble_sort(array: list[int]) -> None:
    """
        # Bubble Sort
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
    
    for i in range(0, len(array)):
        swapped: bool = False
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped == False:
            break


if __name__ == "__main__":
    run_tests(bubble_sort)