from time import time
from multiprocessing import Process, Manager
from find_key_words import find_key_words
from print_results import print_results


def worker(callback, *args):
    callback(args[0], args[1], args[2])


def perform_multiprocessing_search(file_list, key_words):
    start_multiprocessing_manager = time()

    with Manager() as manager:
        shared_dict = manager.dict({word: manager.list([]) for word in key_words})

        pr = []
        for file_path in file_list:
            process = Process(
                target=worker,
                args=(find_key_words, file_path, key_words, shared_dict),
            )
            process.start()
            pr.append(process)
        [el.join() for el in pr]
        time_multiprocessing_manager = time() - start_multiprocessing_manager

        print_results(
            time_multiprocessing_manager, dict(shared_dict), "Time Multiprocessing: "
        )

