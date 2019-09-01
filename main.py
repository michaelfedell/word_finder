import random, string
import time

from grid import Grid
from smart_search import full_search as smart_search
from trie import Trie


def run_smart_search(grid: Grid, dictionary: set) -> set:
    alpha = set(grid.letters)  # get unique letters in grid
    alpha_dict = {l: i for i, l in enumerate(alpha)}  # convert unique letters to lookup map

    word_trie = Trie(alpha_dict)  # pass alpha_dict to Trie so as to not waste space with unavailable chars
    filtered_dictionary = set()  # keep track of words after filtering for available chars
    for word in dictionary:
        if set(word).difference(alpha) or len(word) > len(grid.letters):
            continue  # skip words which are not subset of available alphabet or are longer than grid
        filtered_dictionary.add(word)
        word_trie.insert(word)

    print('Available Letters:', alpha)
    print(f'Filtered Dictionary has {len(filtered_dictionary)} words')

    all_words = set()
    # Perform a full search starting from each of the cells in the grid
    for i in range(len(grid.letters)):
        all_words = all_words.union(smart_search(grid, i, word_trie))

    return all_words


def run():
    C = min(int(input('Desired number of columns in grid (<=10): ')), 10)
    R = min(int(input('Desired number of rows in grid (<=10): ')), 10)
    LETTERS = string.ascii_lowercase
    ROWS = [[random.choice(LETTERS)
             for _ in range(C)]
             for _ in range (R)]
    grid = Grid(ROWS)
    print('\n'.join([' | '.join(row) for row in ROWS]))

    # read in sample dictionary - taken from https://www.mit.edu/~ecprice/wordlist.10000
    with open('./data/english_words.txt') as f:
        word_dictionary = f.read().splitlines()

    simple_word_dictionary = set(word_dictionary)  # ensure no duplicate words passed in dict
    start_time = time.time()
    all_words = run_smart_search(grid, simple_word_dictionary)
    print(f'Took {time.time() - start_time} to build dictionary and find {len(all_words)} words in grid')
    assert(all_words.issubset(simple_word_dictionary))

    all_words = list(all_words)
    print('\nSample of found words:')
    print_words = all_words if len(all_words) < 20 else all_words[:20]
    print(print_words)

    with open('./data/extracted_words.txt', 'w') as f:
        f.writelines([w + '\n' for w in all_words])
	
if __name__ == '__main__':
    run()
