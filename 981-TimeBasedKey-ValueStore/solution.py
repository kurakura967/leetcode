class TimeMap:

    def __init__(self):
        self.hash_map: dict[str, list[tuple[str, int]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = [(value, timestamp)]
        else:
            self.hash_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hash_map.get(key, [])
        l, r = 0, len(arr) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if arr[m][1] <= timestamp:
                res = arr[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


if __name__ == '__main__':
    obj = TimeMap()
    obj.set(key="foo", value="bar", timestamp=1)
    print(obj.get(key="foo", timestamp=1))  # bar
    print(obj.get(key="foo", timestamp=3))  # bar
