import os
from helpers import collect_extensions_and_save, collect_sizes_and_save, organize_files_in_subfolders


def run_organizer():
    path = input("Enter a path: ")

    if not os.path.isdir(path):
        raise ValueError("Path is incorrect! There is no such folder.")

    print(collect_extensions_and_save(path))
    print(collect_sizes_and_save(path))
    organize_files_in_subfolders(path)

if __name__ == "__main__":
    run_organizer()