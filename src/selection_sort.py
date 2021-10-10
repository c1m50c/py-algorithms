from test import run_tests


def selection_sort(array: list[int]) -> None:
    """
        # Selection Sort
        ### Complexities:
        ```py
        Worst Case Time Complexity == O(n^2)
        Average Case Time Complexity == O(n^2)
        Best Case Time Complexity == O(n^2)
        Space Complexity == O(1)
        ```
    """
    for i in range(0, len(array) - 1):
        current_minimum_idx: int = i
        for j in range(i + 1, len(array)):
            if array[j] < array[current_minimum_idx]:
                current_minimum_idx = j
        array[i], array[current_minimum_idx] = array[current_minimum_idx], array[i]


if __name__ == "__main__":
    run_tests(selection_sort)