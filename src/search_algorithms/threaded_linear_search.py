from threading import Thread


def linear_search(array: list[any], finding: any, result: list[list[int, int]]) -> None:
    """
        # Linear Search
        An implementation of linear search to be used with `threaded_linear_search`, time complexities can be found in `threaded_linear_search`.
        ### Parameters:
        ```py
        array: list[any] # Array to search.
        finding: any # What to look for.
        result: list[list[int, int]] # The array to append [ length of array, index of finding ].
        ``` 
    """
    
    for i, value in enumerate(array):
        if value == finding:
            result.append([len(array), i])
            return
    result.append([len(array), -1])


def threaded_linear_search(array: list[any], finding: any) -> int:
    """
        # Threaded Linear Search
        Searches the array for `finding`, returning its index if found. With this implementation this is done with multiple threads.
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
    
    # Todo: Make parameter for thread amount, to allow selection of how many threads to use.
    middle: int = len(array) // 2
    result: list[list[int, int]] = [  ] # Array Length, Index
    thread_one: Thread = Thread(target=linear_search, args=[array[:middle], finding, result])
    thread_two: Thread = Thread(target=linear_search, args=[array[middle:], finding, result])
    
    thread_one.start()
    thread_two.start()
    
    thread_one.join()
    thread_two.join()
    
    for idx, arr in enumerate(result):
        if arr[1] != -1:
            ret: int = 0
            for i in range(0, idx):
                # Add indexes of previous results to get true index in merged array.
                ret += result[i][0]
            return ret + arr[1]
    return -1