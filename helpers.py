import os
import json


def convert_bytes(bytes_count: int) -> str:
    size_repr = ['B', 'KB', 'MB', 'GB', 'TB']
    i = 0

    while bytes_count >= 1024 and i < len(size_repr) - 1:
        bytes_count /= 1024
        i += 1

    return f"{bytes_count:.1f} {size_repr[i]}" # 3.171463 MB

def save_json(file_path, obj):
    with open(file_path, 'w') as f:
        json.dump(obj, f, indent=4) # .write()

def collect_extensions_and_save(path: str) -> dict:
    files_name = [path for path in os.listdir(path) if '.' in path]

    extension_count = {}

    for file_name in files_name:
        extension = file_name.split('.')[-1]

        if extension not in extension_count:
            extension_count[extension] = 0

        extension_count[extension] += 1

    extension_count = dict(sorted(extension_count.items())) # sort dict by keys

    save_json(os.path.join(path, "file_distribution.json"), extension_count)

    return extension_count


def collect_sizes_and_save(path: str) -> dict:
    files_name = [path for path in os.listdir(path) if '.' in path]

    size_paths = {} # {'key1': [], 'key2: []}

    for file_name in files_name:
        file_path = os.path.join(path, file_name)

        size_byte = os.path.getsize(file_path)

        size = convert_bytes(size_byte)

        if size not in size_paths:
            size_paths[size] = []

        size_paths[size].append(file_path)

    save_json(os.path.join(path, "file_sizes.json"), size_paths)

    return size_paths

def organize_files_in_subfolders(path: str) -> None:
    files_name = [path for path in os.listdir(path) if '.' in path]

    for file_name in files_name:
        extension = file_name.split('.')[-1]
    
        os.makedirs(os.path.join(path, extension), exist_ok=True)

        os.rename(os.path.join(path, file_name), os.path.join(path, extension, file_name))