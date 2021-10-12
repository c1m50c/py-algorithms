from tests.searching_tests import run_tests


def binary_search(array: list[int], finding: int, left: int, right: int) -> int:
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
    if right >= left:
        middle: int = left + (right - 1) // 2
        if array[middle] == finding:
            return middle
        elif array[middle] > finding:
            return binary_search(array=array, finding=finding, left=left, right=middle-1)
        else:
            return binary_search(array=array, finding=finding, left=middle+1, right=right)
    else:
        return -1


if __name__ == "__main__":
    run_tests(binary_search)