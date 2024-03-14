def build_shift_table(pattern):
    # shift table creation for Boyer-Moore algorithm
    table = {}
    length = len(pattern)

    # for each substring symbol set shift that is equal substring length
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1

    # if there is no such symbol in the table, shift will be equal to the pattern length
    table.setdefault(pattern[-1], length)

    return table


# boyer-moore search algorithm realisation
def boyer_moore_search(text, pattern):
    # create a shift table for the given pattern
    shift_table = build_shift_table(pattern)

    # initialise initial index for main text
    i = 0

    # move through main text, comparing with a pattern
    while i <= len(text) - len(pattern):
        # starting from the pattern end
        j = len(pattern) - 1

        # compare symbols starting from the pattern end to the start
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        # if the whole pattern coinside, return its position in the text
        if j < 0:
            return i

        # shift the index based on the shift table shorting the search time
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    # if pattern was not found return -1
    return -1


# find key words in the given file
def find_key_words(file_path, words=list(), dictionary={}):
    with open(file_path, "r") as fh:
        text = fh.read()

        for word in words:
            result = boyer_moore_search(text, word)
            if result >= 0:
                dictionary[word].append(file_path.name)
        return dictionary
