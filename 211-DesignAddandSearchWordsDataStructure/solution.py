
class Node:
    def __init__(self):
        self.children = {}
        self.word = False

# Problem that could not be answered correctly
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = Node()
            cur = cur.children[w]
        cur.word = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        return dfs(0, self.root)


if __name__ == '__main__':
    word = "bad"
    obj = WordDictionary()
    obj.addWord(word)
    param_2 = obj.search(word)
