#https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.search_words = []

class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for i in  range(len(word)):
            if not word[i] in node.children:
                node.children[word[i]] = TrieNode()
            node.search_words.append(word[i:])
            node = node.children[word[i]]

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
    
    def searchSuggestion(self,word):
        result = []
        node = self.root
        for i in range(len(word)):
            if word[i] in node.children:
                result.append([word[:i+1] + sword for sword in node.children[word[i]].search_words[:3]])
                node = node.children[word[i]]
            else:
                result.append([] for _ in range(len(word[i:])))
                break
        return result


def search_suggestion(words, search_word):
    wordDictionary = WordDictionary()
    words.sort()
    for word in words:
        wordDictionary.addWord(word)
    print(wordDictionary.searchSuggestion(search_word))


search_suggestion(["razer","blade","knife","cutter","games"], "games")