import typing as t
from collections import deque

from grid import Grid
from trie import Trie


def full_search(grid: Grid, start: int, word_trie: Trie) -> set:
    """
    Search all possible paths from starting cell, terminating paths which are not valid words or prefixes.

    Args:
	grid: grid on which to perform search
        start: index of starting cell in flattened letter array
        trie: constructed trie dictionary for validating words 

    Returns:
        set of valid words found when starting from this cell

    """
    paths = deque([[start]])  # initialize deque with starting path
    found_words = set()
    while paths:
        path = paths.popleft()  # take new path to search from top of deque
        # check for valid words and prefixes among this paths immediate neighbors
        new_words, next_paths = search(grid, path, word_trie)
        found_words = found_words.union(new_words)  # collect unique new words
        paths.extend(next_paths)  # add new paths to the back of deque for later searching
    return found_words

def search(grid: Grid, path: t.List[int], word_trie: Trie) -> t.Tuple[t.List[bool], t.List[bool]]:
    """
    Search for all possible neighbors given a path.

    Args:
        grid: Grid on which to perform search

    Returns:
        list of valid words, list of valid next paths 

    """
    # get all possible neighbor indices (unused in current word)
    neighbors  = [l for l in grid.graph[path[-1]] if l not in path]

    # construct all candidate paths
    candidates = [path + [l] for l in neighbors]

    if len(path) < 2 or not candidates:
        # candidate_words must be 3 characters or longer
        return [], candidates

    # translate index paths to corresponding letter sequences
    candidate_words = [''.join([grid.letters[i] for i in candidate]) for candidate in candidates]

    # Check all candidate words for validity as words or prefixes
    valid = [word_trie.search(cw) for cw in candidate_words]
    valid
    valid_words, valid_candidates = list(zip(*valid))

    # Collect valid words and valid prefixes for further searching
    good_words = [w for i, w in enumerate(candidate_words) if valid_words[i]]
    good_candidates = [w for i, w in enumerate(candidates) if valid_candidates[i]]

    return good_words, good_candidates

