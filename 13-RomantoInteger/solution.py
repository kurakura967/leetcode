SETTINGS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:

    # first solution(runtime: 47 ms, memory: 17.32 MB)
    def romanToInt1(self, s: str) -> int:
        seen = []
        res = 0
        romans = list(s)
        for idx, roman in enumerate(romans):

            num = SETTINGS[roman]
            # 既に足した文字の場合はスキップ
            if idx in seen:
                continue
            # 最後の文字の場合はそのまま足す
            if idx == len(romans) - 1:
                res += num
                continue
            next_num = SETTINGS[romans[idx + 1]]
            # 次の文字が大きい場合は引く（ex: "IV"(=5(V)-1(I))）
            if num < next_num:
                res += next_num - num
                seen.append(idx + 1)
                continue

            res += num

        return res

    # second solution(runtime: 48 ms, memory: 17.49 MB)
    def romanToInt2(self, s: str) -> int:

        res = 0
        romans = list(s)

        for idx, roman in enumerate(romans):

            if idx < len(romans) - 1 and SETTINGS[roman] < SETTINGS[romans[idx + 1]]:
                res -= SETTINGS[roman]
                continue

            res += SETTINGS[roman]

        return res


if __name__ == '__main__':
    print(Solution().romanToInt1("III"))  # 3
    print(Solution().romanToInt2("III"))  # 3
