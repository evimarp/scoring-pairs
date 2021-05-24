from typing import Tuple, List
import heapq as hq


def max_pair(words: List[str]) -> Tuple[str, str]:
    """ Given a list of words, find a word pair with the highest score.

    The score is determined by multiplying the lengths of the words
    by one another with none common char.
    """
    def hash(word):
        word_set = set(word)
        word_hash = 0
        for char in word_set:
            word_hash |= bits.get(char, 0)
        return word_hash

    def find_match(word_hash):
        s, i = max((value for key, value in hashes.items() if not (key & word_hash)),
                   key=lambda x: x[0])
        if i:
            return words[i]

    bits = {
        'a': 1, 'b': 2, 'c': 4, 'd': 8, 'e': 16, 'f': 32, 'g': 64, 'h': 128, 'i': 256,
        'j': 512, 'k': 1024, 'l': 2048, 'm': 4096, 'n': 8192, 'o': 16384, 'p': 32768,
        'q': 65536, 'r': 131072, 's': 262144, 't': 524288, 'u': 1048576, 'v': 2097152,
        'w': 4194304, 'x': 8388608, 'y': 16777216, 'z': 33554432
    }

    heap = []
    # pre-processing, create a heap
    for i, word in enumerate(words):
        hq.heappush(heap, (-len(word), i))

    # maps a hash -> len_word, word_index
    hashes = {0: (0, None)}  # this is Sentinel
    answer = words[0], words[1]

    while heap:
        size, index = hq.heappop(heap)

        word = words[index]
        word_hash = hash(word)
        best = find_match(word_hash)
        if best:
            return word, best

        if word_hash not in hashes:
            hashes[word_hash] = (-size, index)

    return answer

