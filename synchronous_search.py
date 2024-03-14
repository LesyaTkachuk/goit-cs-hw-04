from time import time
from collections import defaultdict

from find_key_words import find_key_words
from print_results import print_results


def perform_synchronous_search(file_list, key_words):
    grouped_words = defaultdict(list)
    start_general = time()
    for file_path in file_list:
        find_key_words(file_path, key_words, grouped_words)
    time_general = time() - start_general

    print_results(time_general, grouped_words, "Time Synchronous search")
