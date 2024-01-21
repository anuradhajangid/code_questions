#https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if not char in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if not char in node.children:
                return False
            node = node.children[char]
        return node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if not char in node.children:
                return False
            node = node.children[char]
        return True


class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if not char in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word) -> bool:
        node = self.root
        return WordDictionary._searchRecursively(node, word, 0)


    def _searchRecursively(node, word, index):
        if index == len(word):
            if node.is_word == True:
                return True
            return False
        if word[index] == ".":
            for child in node.children.values():
                if WordDictionary._searchRecursively(child, word, index + 1):
                    return True
        else:
            if word[index] in node.children:
                return WordDictionary._searchRecursively(node.children[word[index]], word, index + 1)
            else:
                return False
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
assert wordDictionary.search("pad") == False
assert wordDictionary.search("bad") == True
assert wordDictionary.search(".ad") == True
assert wordDictionary.search("b..") == True