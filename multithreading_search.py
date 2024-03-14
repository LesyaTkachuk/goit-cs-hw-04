from time import time
from threading import Thread
from collections import defaultdict

from find_key_words import find_key_words
from print_results import print_results


def worker(callback, *args):
    callback(args[0], args[1], args[2])


def perform_multithreading_search(file_list, key_words):
    # results dictionary
    grouped_words = defaultdict(list)
    threads = []
    start_multithreading = time()
    for file_path in file_list:
        thread = Thread(
            target=worker,
            args=(find_key_words, file_path, key_words, grouped_words),
        )
        thread.start()
        threads.append(thread)

    [el.join() for el in threads]
    time_multithreading = time() - start_multithreading
    
    print_results(time_multithreading, grouped_words, "Time Multithreading: ")

