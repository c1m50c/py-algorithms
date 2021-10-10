from quick_sort import quick_sort
from merge_sort import merge_sort
from colorama import Fore, Style
from test import run_tests


def help():
    print("Help:")
    print(f"1. help {Fore.BLUE}// Gives valid commands{Fore.RESET}")
    print(f"2. quit {Fore.BLUE}// Quits{Fore.RESET}")
    print(f"3. all {Fore.BLUE}// Runs all algorithms{Fore.RESET}")
    print(f"4. quick_sort {Fore.BLUE}// Runs QuickSort algorithm{Fore.RESET}")
    print(f"5. merge_sort {Fore.BLUE}// Runs MergeSort algorithm{Fore.RESET}")


def run_all_algorithms():
    print("Running all Algorithms...")
    run_tests(quick_sort)
    print()
    run_tests(merge_sort)


# This is redundant, find a better way to run singular tests.
def run_quick_sort(): run_tests(quick_sort)
def run_merge_sort(): run_tests(merge_sort)


COMMANDS = {
    "help": [help],
    "quit": [quit],
    "all": [run_all_algorithms],
    "quick_sort": [run_quick_sort],
    "merge_sort": [run_merge_sort],
}


def main():
    while True:
        inp = input(f"{Style.BRIGHT}{Fore.MAGENTA}py-algorithms{Fore.GREEN}:${Fore.RESET}{Style.RESET_ALL} ")
        if inp.lower() in COMMANDS.keys():
            for func in COMMANDS[inp.lower()]:
                func()


if __name__ == "__main__":
    main()