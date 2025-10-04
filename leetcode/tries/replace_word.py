class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

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


    def replace(self, sentence):
        data = {}
        response = ""
        for word in sentence.split(" "):
            if word in data:
                response += f" {data[word]}"
                continue
            data[word] = None
            node = self.root
            string = ""
            for char in word:
                string += char
                if char not in node.children:
                    string = word
                if len(string) == len(word):
                    break
                if char in node.children:
                    if node.children[char].is_word:
                        data[word] = string
                        break
                    node = node.children[char]
            data[word] = string
            response += " " + string
        return response.strip()



        
wordDictionary = WordDictionary()
wordDictionary.addWord("qui")
wordDictionary.addWord("f")
wordDictionary.addWord("la")
wordDictionary.addWord("d")
assert wordDictionary.replace("the quick brown fox jumps over the lazy dog") == "the qui brown f jumps over the la d"