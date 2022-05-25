import unittest
from typing import List
from Trie import Trie


my_trie = Trie()

my_trie.insert('ana')
my_trie.insert('ann')
my_trie.insert('anna')
my_trie.insert('abba')
my_trie.insert('banana')

assert my_trie.search('ann') == True
assert my_trie.search('anna') == True
assert my_trie.search('an') == False
assert my_trie.search('ban') == False

assert my_trie.startsWith('an') == True
assert my_trie.startsWith('na') == False

print(my_trie.list_all())
print(my_trie.find_all_starts_with('an'))
print(my_trie.find_all_starts_with('c'))
