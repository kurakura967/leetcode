class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        val = self.cache.pop(key)
        self.cache[key] = val # 後方に追加することで最新のキーに更新する
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key) # 既に存在する場合は削除する
        else:
            # キャパシティを超えた場合は最初の要素を削除する
            if len(self.cache) == self.capacity:
                self.cache.pop(next(iter(self.cache))) # 最初の要素を削除する
        self.cache[key] = value # 後方に追加することで最新のキーに更新する


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)  # 1
    cache.put(3, 3)
    cache.get(2)  # -1
