from tests.sorting_tests import run_tests


def make_heap(array: list[int], length: int, idx: int) -> None:
    largest: int = idx
    left: int = 2 * idx + 1
    right: int = 2 * idx + 2
    
    if left < length and array[left] > array[largest]:
        largest = left
    
    if right < length and array[right] > array[largest]:
        largest = right
    
    if largest != idx:
        array[idx], array[largest] = array[largest], array[idx]
        make_heap(array=array, length=length, idx=largest)


def heap_sort(array: list[int]) -> None:
    """
        # Heap Sort
        ### Complexities:
        ```py
        Worst Case Time Complexity == O(n log n)
        Average Case Time Complexity == O(n log n)
        Best Case Time Complexity == O(n)
        Space Complexity == O(n) total, O(1) auxiliary
        ```
    """
    
    for i in range(len(array) // 2 - 1, -1, -1):
        make_heap(array=array, length=len(array), idx=i)
    
    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        make_heap(array=array, length=i, idx=0)


if __name__ == "__main__":
    run_tests(heap_sort)