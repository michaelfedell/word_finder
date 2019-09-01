import typing as t
from collections import defaultdict


class Grid:
    """Stores an arbitrary arrangement of letters in a 4x4 grid in a Graph with edges between adjacent cells."""
    def __init__(self, rows: t.List[t.List[str]]):
        """
        Initializes the Grid with dimensions, flattened contents, graph structure and dictionary trie.

        Args:
            rows: letters arranged in columns and rows

        """
        # Keep dimensions of grid and then flatten letter array
        self.R = len(rows)
        self.C = len(rows[0])
        self.letters = []
        self.graph = defaultdict(list)  # key for each letter index with list of neighbors as value

        for r, row in enumerate(rows):
            for c, letter in enumerate(row):
                i = r * self.R + c  # convert row,column to flat index
                self.letters.append(letter)  # add cell contents to flattened list
                neighbors = [x * self.R + y for x in range(r - 1, r + 2)  # adjacent rows
                             for y in range(c - 1, c + 2)  # adjacent columns
                             if 0 <= x < self.R  # avoid x-boundary
                             and 0 <= y < self.C]  # avoid y-boundary
                self.graph[i] = [c for c in neighbors if c != i]  # omit self from neighbors

