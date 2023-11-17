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
        
        node.end = True # mark the last node as the end of a string
    
    # counts the number of strings with the prefix that is the string traced out by the node
    def dfs(self, node):
        if node.end:
            self.cnt += 1
        
        for child in node.children.values():
            self.dfs(child)
        
    def starts_with(self, prefix):
        node = self.root
        self.cnt = 0 # count number of strings with given prefix

        # confirm if the whole string is in the trie already
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        
        # dfs on the subtree of the prefix
        self.dfs(node)
        return self.cnt

trie = Trie()
N = int(input())
for i in range(N):
    s = input()
    print(trie.starts_with(s))
    trie.insert(s)
