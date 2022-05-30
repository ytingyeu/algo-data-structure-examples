import unittest
from Trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self) -> None:
        self.my_trie = Trie()
        self.my_trie.insert('ana')
        self.my_trie.insert('ann')
        self.my_trie.insert('anna')
        self.my_trie.insert('abba')
        self.my_trie.insert('banana')
        return super().setUp()

    def test_search(self):
        self.assertTrue(self.my_trie.search('ann'))
        self.assertTrue(self.my_trie.search('anna'))
        self.assertFalse(self.my_trie.search('an'))
        self.assertFalse(self.my_trie.search('ban'))

    def test_startWith(self):
        self.assertTrue(self.my_trie.startsWith('an'))
        self.assertFalse(self.my_trie.startsWith('na'))

    def test_list_all(self):
        expect = ['ana', 'ann', 'anna', 'abba', 'banana']
        self.assertCountEqual(self.my_trie.list_all(), expect)

    def test_find_all_starts_with(self):
        expect = ['ana', 'ann', 'anna']
        self.assertCountEqual(self.my_trie.find_all_starts_with('an'), expect)

        self.assertCountEqual(self.my_trie.find_all_starts_with('anc'), [])
        self.assertCountEqual(self.my_trie.find_all_starts_with('c'), [])


unittest.main()
