class TrieNode:
    def __init__(self,char):
        self.char = char
        self.is_end= False
        self.children={}

class Trie(object):
    def __init__(self):
        self.root = TrieNode 