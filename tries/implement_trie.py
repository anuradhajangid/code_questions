#https://leetcode.com/problems/implement-trie-prefix-tree/description/

class TrieNode:
    def __init__(self, value=None) -> None:
        self.value = value
        self.children = []
        self.is_word = False

    def getChild(self, value):
        for child in self.children:
            if value == child.value:
                return child

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            child =  node.getChild(char)
            if child:
                node = child
            else:
                temp = TrieNode(char)
                node.children.append(temp)
                node = temp
        node.is_word = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            child = node.getChild(char)
            if child:
                node = child
            else:
                return False
        return node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            child = node.getChild(char)
            if child:
                node = child
            else:
                return False
        return True
        

obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))