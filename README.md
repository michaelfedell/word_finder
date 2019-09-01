# Word Finder

This project was developed in response to a programming challenge in which words must be mined from a grid of random letters. Words can be formed by traversing the grid one cell at a time moving only to adjacent cells (up/down, left/right or diagonal).

The implementation takes a simple word list dictionary and builds a trie (prefix tree) data structure to perform efficient word validation. This allows us to terminate a grid search early if the path does not have any valid children (current path is not a prefix in trie).

The implementation can be run via the main.py file.

```python
python main.py
```
