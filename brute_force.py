from collections import deque
import typing as t

from grid import Grid


def full_search(grid: Grid, start: int, dictionary: set):
    # initiallize queue for paths to search
    paths = deque([[start]])
    found_words = set()
    while paths:
        path = paths.popleft()
        new_words, next_paths = search(grid, path, dictionary)
        found_words = found_words.union(new_words)
        paths.extend(next_paths)
    return found_words

def search(grid: Grid, path: t.List[int], dictionary: set):
    # get all possible neighbor indices (unused in current word)
    neighbors = [l for l in grid.graph[path[-1]] if l not in path]
    print(path)

    # construct all candidate paths
    candidates = [path + [l] for l in neighbors]

    if len(path) < 2:
        # candidate_words must be 3 characters or longer
        return [], candidates
    else:
        # translate index paths to corresponding letter sequences
        candidate_words = [''.join([grid.letters[i] for i in cand_path]) for cand_path in candidates]

    return dictionary.union(candidate_words), candidates

