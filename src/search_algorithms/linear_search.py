from tests.searching_tests import run_tests


def linear_search(array: list[any], finding: any) -> int:
    """
        # Linear Search
        Searches the array for `finding`, returning its index if found.
        ### Parameters:
        ```py
        array: list[any] # The Array to search.
        finding: any # What we're trying to find within the Array.
        ```
        ### Complexities:
        ```py
        Worst Case Time Complexity == O(n)
        Average Case Time Complexity == O(n / 2)
        Best Case Time Complexity == O(1)
        Space Complexity == O(1)
        ```
    """
    
    for i, value in enumerate(array):
        if value == finding:
            return i
    return -1


if __name__ == "__main__":
    run_tests(linear_search)