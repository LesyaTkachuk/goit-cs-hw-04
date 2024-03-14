from argparse import ArgumentParser
from pathlib import Path

from multithreading_search import perform_multithreading_search
from multiprocessing_search import perform_multiprocessing_search
from synchronous_search import perform_synchronous_search


def get_file_list(path):
    file_list = []
    if path.is_dir():
        for child in path.iterdir():
            file_list += get_file_list(child)
    elif path.is_file():
        file_list.append(path)
    else:
        print("Uknown path object")
    return file_list


def main():
    try:
        parser = ArgumentParser()

        parser.add_argument("-s", "--source", help="Source foulder", default="test")

        args = parser.parse_args()

        root_path = Path(args.source)

        # get the list of all files inside root folder and all it's child folders
        file_list = get_file_list(root_path)

        # the list of key words for search in files
        key_words = ["pleasure", "text", "hand", "Python"]

        # multithreading search
        perform_multithreading_search(file_list, key_words)

        #  multiprocessing search
        perform_multiprocessing_search(file_list, key_words)

        # synchronous search
        perform_synchronous_search(file_list, key_words)
    except Exception as e:
        print(f"Ooooopps. Error happend! {e}")


if __name__ == "__main__":
    main()
