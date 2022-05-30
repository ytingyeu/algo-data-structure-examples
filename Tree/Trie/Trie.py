from typing import Dict, List


class TrieNode:

    def __init__(self, new_char: str = ''):
        self._val: str = new_char
        self._children: Dict[str, TrieNode] = {}
        self._end_of_word: bool = False


class Trie:

    def __init__(self):
        # root node does not contain any letter
        self._root = TrieNode()

    def insert(self, word: str) -> None:

        curr_node: TrieNode = self._root

        for char in word:

            if char not in curr_node._children:
                curr_node._children[char] = TrieNode(char)

            curr_node = curr_node._children[char]

        curr_node._end_of_word = True

    def search(self, word: str) -> bool:
        curr_node = self._root

        for char in word:

            if char not in curr_node._children:
                return False

            curr_node = curr_node._children[char]

        return curr_node._end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr_node = self._root

        for char in prefix:

            if char not in curr_node._children:
                return False

            curr_node = curr_node._children[char]

        return True

    def _get_words(self, root: TrieNode):
        if not root:
            return []

        words = []

        if root._children:
            if root._end_of_word:
                l.append('')

            for child in root._children.values():
                for word in self._get_words(child):
                    words.append(child._val + word)

        else:
            words.append('')

        return words

    def list_all(self) -> List[str]:
        return self._get_words(self._root)

    def find_all_starts_with(self, prefix: str) -> List[str]:

        curr_node = self._root

        for char in prefix:

            if char not in curr_node._children:
                return []

            curr_node = curr_node._children[char]

        res = [(prefix + word) for word in self._get_words(curr_node)]

        return res
