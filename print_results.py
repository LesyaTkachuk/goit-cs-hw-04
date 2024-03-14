OKBLUE = "\033[94m"
ENDC = "\033[0m"
DGRAY = "\033[1;30;40m"


def print_results(time, result_dict, title="Time: "):
    print(DGRAY + "-" * 80 + ENDC)
    print(OKBLUE + f"{title} {time}" + ENDC)
    for key, value in sorted(result_dict.items()):
        print(f"{key}: {value}")
    print(DGRAY + "-" * 80 + ENDC)
