from sorting_algorithms.selection_sort import selection_sort
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.quick_sort import quick_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.heap_sort import heap_sort
from sorting_algorithms.threaded_quick_sort import threaded_quick_sort

from search_algorithms.linear_search import linear_search
from search_algorithms.binary_search import binary_search

from tests.searching_tests import run_tests as run_search_tests
from tests.sorting_tests import run_tests as run_sorting_tests
from colorama import Fore, Style



def help():
    """
        # Help ~ Command
        Prints all valid commands to the output.
    """
    # Todo: Automatically generate this stuff based on the COMMANDS dictionary
    print("Help:")
    print(f"help {Fore.BLUE}// Gives valid commands{Fore.RESET}")
    print(f"quit {Fore.BLUE}// Quits{Fore.RESET}")
    print(f"all {Fore.BLUE}// Runs all algorithms{Fore.RESET}")
    print(f"sorting {Fore.BLUE}// Runs all sorting algorithms{Fore.RESET}")
    print(f"searching {Fore.BLUE}// Runs all searching algorithms{Fore.RESET}")
    print(f"quick_sort {Fore.BLUE}// Runs QuickSort algorithm{Fore.RESET}")
    print(f"merge_sort {Fore.BLUE}// Runs MergeSort algorithm{Fore.RESET}")
    print(f"insertion_sort {Fore.BLUE}// Runs InsertionSort algorithm{Fore.RESET}")
    print(f"selction_sort {Fore.BLUE}// Runs SelectionSort algorithm{Fore.RESET}")
    print(f"bubble_sort {Fore.BLUE}// Runs BubbleSort algorithm{Fore.RESET}")
    print(f"heap_sort {Fore.BLUE}// Runs HeapSort algorithm{Fore.RESET}")
    print(f"threaded_quick_sort {Fore.BLUE}// Runs ThreadedQuickSort algorithm{Fore.RESET}")
    print(f"linear_search {Fore.BLUE}// Runs LinearSearch algorithm{Fore.RESET}")
    print(f"binary_search {Fore.BLUE}// Runs BinarySearch algorithm{Fore.RESET}")


def run_all_algorithms():
    """
        # Run All Algorithms ~ Command
        Runs all the algorithms.
    """
    print("Running all Algorithms...")
    run_sorting_tests(quick_sort)
    print()
    run_sorting_tests(merge_sort)
    print()
    run_sorting_tests(insertion_sort)
    print()
    run_sorting_tests(selection_sort)
    print()
    run_sorting_tests(bubble_sort)
    print()
    run_sorting_tests(heap_sort)
    print()
    run_sorting_tests(threaded_quick_sort)
    print()
    run_search_tests(linear_search)
    print()
    run_search_tests(binary_search)


def run_all_sorting_algorithms():
    """
        # Run All Sorting Algorithms ~ Command
        Runs all the sorting algorithms.
    """
    print("Running all Sorting Algorithms...")
    run_sorting_tests(quick_sort)
    print()
    run_sorting_tests(merge_sort)
    print()
    run_sorting_tests(insertion_sort)
    print()
    run_sorting_tests(selection_sort)
    print()
    run_sorting_tests(bubble_sort)
    print()
    run_sorting_tests(heap_sort)
    print()
    run_sorting_tests(threaded_quick_sort)


def run_all_searching_algorithms():
    """
        # Run All Searching Algorithms ~ Command
        Runs all the searching algorithms.
    """
    print("Running all Searching Algorithms...")
    run_search_tests(linear_search)
    print()
    run_search_tests(binary_search)


# This is redundant, find a better way to run singular tests.
def run_quick_sort(): run_sorting_tests(quick_sort)
def run_merge_sort(): run_sorting_tests(merge_sort)
def run_insertion_sort(): run_sorting_tests(insertion_sort)
def run_selection_sort(): run_sorting_tests(selection_sort)
def run_bubble_sort(): run_sorting_tests(bubble_sort)
def run_heap_sort(): run_sorting_tests(heap_sort)
def run_threaded_quick_sort(): run_sorting_tests(threaded_quick_sort)
def run_linear_search(): run_search_tests(linear_search)
def run_binary_search(): run_search_tests(binary_search)


COMMANDS = {
    "help": [help],
    "quit": [quit],
    "all": [run_all_algorithms],
    "sorting": [run_all_sorting_algorithms],
    "searching": [run_all_searching_algorithms],
    "quick_sort": [run_quick_sort],
    "merge_sort": [run_merge_sort],
    "insertion_sort": [run_insertion_sort],
    "selection_sort": [run_selection_sort],
    "bubble_sort": [run_bubble_sort],
    "heap_sort": [run_heap_sort],
    "threaded_quick_sort": [run_threaded_quick_sort],
    "linear_search": [run_linear_search],
    "binary_search": [run_binary_search],
}


def main():
    """
        # Main
        The Main Function! Currently serving as a shell for this project.
    """
    while True:
        inp = input(f"{Style.BRIGHT}{Fore.MAGENTA}py-algorithms{Fore.GREEN}:${Fore.RESET}{Style.RESET_ALL} ")
        if inp.lower() in COMMANDS.keys():
            for func in COMMANDS[inp.lower()]:
                func()
        else:
            print(f"Command {Style.BRIGHT}{Fore.RED}'{inp}'{Fore.RESET}{Style.RESET_ALL} does not exist, try {Style.BRIGHT}{Fore.GREEN}'help' for a list of commands{Fore.RESET}{Style.RESET_ALL}.")


if __name__ == "__main__":
    main()