"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ORDER = "ascending"


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"Unable to sort {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    order = DEFAULT_ORDER
    if (len(sys.argv) == 3) or (len(sys.argv) == 4):
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        if len(sys.argv) == 4:
            order = sys.argv[3].lower()
            if not ((order == "ascending") or (order == "descending")):
                print("Opcion de order no valida, por favor asegurate de que sea ascending o descending")
                sys.exit(1)
    else:
        print("You must specify a file as first argument")
        print("Second argument for deleting duplicates")
        sys.exit(1)

    print(f"Words from file {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"{filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list, order == "ascending"))
