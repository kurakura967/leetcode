# first solution(runtime: 466 ms, memory: 20.28 MB)
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # リストの一番先頭に追加する
        self.stack.insert(0, val)

    def pop(self) -> None:
        # リストの一番先頭を削除する
        self.stack.pop(0)

    def top(self) -> int:
        # リストの一番先頭を取得する
        return self.stack[0]

    def getMin(self) -> int:
        # リストの最小値を取得する
        # min(list)はO(n)なのでlistの長さが長くなると遅くなる
        return min(self.stack)


# second solution(runtime: 44 ms, memory: 20.42 MB)
class MinStack2:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            val = min(self.min_stack[-1], val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # O(1)で最小値を取得することが出来る
        return self.min_stack[-1]


if __name__ == '__main__':
    minStack = MinStack()

    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # -3
    minStack.pop()
    print(minStack.top())  # 0
    print(minStack.getMin())  # -2
