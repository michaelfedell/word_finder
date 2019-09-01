import typing as t
import time


class TrieNode(object):
    """Nodes use a list of pointers which point to other nodes if path continues."""
    def __init__(self, n_alpha: int):
        """
        Create a new empty node for Trie (null pointers for letters in alphabet)

        Args:
            n_alpha: Number of letters in available alphabet

        """
        # will have a key for each potential next letter
        self.children: t.List[t.Union[None, TrieNode]] = [None] * n_alpha
        self.isWord = False  # indicates if the path to this node represents a valid word


class Trie(object):
    """
    Trie is a search tree built for quick lookups of words and prefixes.

    References:
        https://en.wikipedia.org/wiki/Trie

    """
    def __init__(self, alphabet: t.Dict[str, int]):
        """
        Create the Trie with available alphabet.

        Alphabet is passed to limit the size of the Trie. Size in memory is dependent on length of longest
        word in tree (m), and size of alphabet (n); thus O(m*n).

        Searching for words is very fast as an O(1) lookup is made to check for valid child for each
        character in search key; thus total search time is O(m) for word of length m (unless early stop).

        Inserts are equivalent to searches but instead of terminating when no child is available for a
        sought letter, a new node is created for that letter and traversal continues; O(m) insert speed

        Args:
            alphabet: alphabet should map the potential characters in the available alphabet to their
                      respective index for efficient lookup

        """
        self.alphabet = alphabet
        self.n_alpha = len(alphabet)
        self.root = TrieNode(self.n_alpha)

    def insert(self, new_word: str):
        """
        Insert a new word into the Trie. May be subset or superset of existing words or completely new.

        Args:
            new_word: full word to insert in the Trie. Will add between 0 and m nodes for word of length m

        Raises:
            ValueError: if word contains letters which are not part of available alphabet.

        """
        node = self.root  # current node in trie
        for level in range(len(new_word)):  # traverse word one char at a time
            char = self.alphabet.get(new_word[level])  # get index for particular char
            if char is None:
                raise ValueError(f'Character {new_word[level]} is not in available alphabet')
            if not node.children[char]:
                # add a node for this char if not already present at this level
                node.children[char] = TrieNode(self.n_alpha)
            node = node.children[char]  # move to the proper node in trie's next level
        node.isWord = True  # mark that this node terminates a valid word

    def search(self, key: str) -> t.Tuple[bool, bool]:
        """
        Search the Trie to determine if a key is a valid word or the prefix of some valid word.

        Args:
            key: prefix to search for (may be full word or substring)

        Raises:
            ValueError: if word contains letters which are not part of available alphabet.

        Returns:
            key is valid word, key is prefix to other valid words

        """
        if not set(key).issubset(self.alphabet):
            raise ValueError(f'{key} contains characters which are not in available alphabet')
        node = self.root  # current node in trie
        for level in range(len(key)):  # traverse word one char at a time
            char = self.alphabet.get(key[level])  # get index for particular char
            if not node.children[char]:
                return False, False  # branch dies before end of key
            node = node.children[char]  # move to the proper node in trie's next level
        # Interested in whether the searched key is a word itself AND if it has any children
        return node is not None and node.isWord, any(node.children)


