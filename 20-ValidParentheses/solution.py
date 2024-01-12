class Solution:
    # first solution(runtime: 27 ms, memory: 17.47 MB)
    def isValid1(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        if len(s) == 1:
            return False

        open_brackets = brackets.values()
        if s[0] not in open_brackets:
            return False

        tmp_open_brackets = []
        for char in s:
            if char in open_brackets:
                # 一番最初に追加する
                tmp_open_brackets.insert(0, char)
                continue

            # 閉じカッコに対応する開きカッコがない場合はFalse
            if not tmp_open_brackets:
                return False
            # 閉じカッコに対応する開きカッコが違う場合はFalse
            if brackets.get(char) != tmp_open_brackets[0]:
                return False
            # 閉じカッコに対応する開きカッコがある場合はスタックから削除する
            tmp_open_brackets.pop(0)

        return len(tmp_open_brackets) == 0

    # second solution(runtime: 30 ms, memory: 17.41 MB)
    def isValid2(self, s: str) -> bool:

        brackets = {'(':')', '{':'}','[':']'}
        stack = []
        for char in s:

            # 開きカッコの場合
            if char in brackets:
                stack.append(char)

            # 閉じカッコの場合
            elif len(stack) == 0 or brackets[stack.pop()] != char:
                return False

        return len(stack) == 0


if __name__ == '__main__':
    print(Solution().isValid2("()"))  # True
    print(Solution().isValid2("()[]{}"))  # True
    print(Solution().isValid2("(]"))  # False
    print(Solution().isValid2("{[]}"))  # True
    print(Solution().isValid2("(])"))  # False
    print(Solution().isValid2("(){}}{"))  # False
