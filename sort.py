import sys
import os
import argparse

# key names is new folder names
extensions = {

    'images': ['jpeg', 'png', 'jpg', 'svg'],

    'video': ['avi', 'mp4', 'mov', 'mkv'],

    'documents': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],

    'audio': ['mp3', 'ogg', 'wav', 'amr'],

    'archives': ['zip', 'gz', 'tar'],

    # 'other' - for unknown extensions

}

# if len(sys.argv) != 2:
#     print("\n\033[31mNeed a name of the folder for sorting\033[0m\n")
#     quit()

# else:
#root_folder = sys.argv[1]
root_folder = r'd:\PYTHON\02'


def tree_items(path):
    all_addresses = []
    for address, dirs, files in os.walk(path):
        for name in files:
            all_addresses.append(os.path.join(address, name))
    return all_addresses


for address in tree_items(root_folder):
    print(address)

for item in tree_items(root_folder):
    for folder, extention in extensions.items():
        default_folder = 'other'
        sorted_folders = {}
        if item[item.rfind('.') + 1:] in extention:
            sorted_folders[item] = folder
            break
        else:
            sorted_folders[item] = default_folder

for adr, folder in sorted_folders.items():
    print(adr, folder)
