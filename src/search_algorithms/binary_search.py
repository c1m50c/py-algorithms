from tests.searching_tests import run_tests


def binary_search(array: list[int], finding: int) -> int:
    """
        # Binary Search
        Searches a sorted array for `finding`, returning its index within the array if found.
        ### Parameters:
        ```py
        array: list[int] # The Array to search.
        finding: int # What we're trying to find within the Array.
        left: int # Left most index of the section we're searching in.
        right: int # Right most index of the section we're searching in.
        ```
        ### Complexities:
        ```py
        Worst Case Time Complexity == O(log n)
        Average Case Time Complexity == O(log n)
        Best Case Time Complexity == O(1)
        Space Complexity == O(1)
        ```
    """
    
    left, right = 0, len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if finding == array[middle]:
            return middle
        elif finding < array[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1


if __name__ == "__main__":
    run_tests(binary_search)