class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False


# Problem that could not be answered correctly
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = Node()  # {"a": Node()} -> {"a": {"p": Node()}} -> {"a": {"p": {"p": Node()}}} -> {"a": {"p": {"p": {"l": Node()}}} -> {"a": {"p": {"p": {"l": {"e": Node()}}}}
            cur = cur.children[w]
        cur.isEnd = True  # {"a": {"p": {"p": {"l": {"e": {"isEnd": True}}}}}

    def search(self, word: str) -> bool:

        cur = self.root
        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for p in prefix:
            if p not in cur.children:
                return False
            cur = cur.children[p]
        return True


if __name__ == '__main__':
    # Your Trie object will be instantiated and called as such:
    word = "apple"
    obj = Trie()
    obj.insert(word)
    print(obj.search(word))  # True
