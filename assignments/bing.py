"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  Resources:
  PyRival Repo: Trie tree

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.end = False
        self.children = {} # map of character to node

        # let each node store the number of strings with the prefix at the node
        self.counter = 0 

class Trie():
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
            node.counter += 1 # every time we see the same char, count++
        node.end = True # mark the last node as the end of a string
        
    def starts_with(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children: # new string
                return 0
            node = node.children[char]
        return node.counter

trie = Trie()
N = int(input())
for i in range(N):
    s = input()
    print(trie.starts_with(s))
    trie.insert(s)
