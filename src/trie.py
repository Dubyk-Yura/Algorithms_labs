class Node:
    def __init__(self):
        self.child = {}
        self.is_key = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, pattern: str):
        node = self.root
        for letter in pattern:
            if letter not in node.child:
                node.child[letter] = Node()
            node = node.child[letter]
        node.is_key = True

    def find_word(self, word: str):
        node = self.root
        for letter in word:
            if letter not in node.child:
                return False
            node = node.child[letter]
        return node.is_key

    def find_prefix(self, prefix: str):
        node = self.root
        for letter in prefix:
            if letter not in node.child:
                return False
            node = node.child[letter]
        return True


def build_trie(patterns: list[str]) -> Trie():
    trie_obj = Trie()
    for pattern in patterns:
        trie_obj.insert(pattern)
    return trie_obj
