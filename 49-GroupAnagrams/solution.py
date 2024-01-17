import collections
class Solution:
    # first solution(runtime: 9300 ms, memory: 20.96MB)
    def groupAnagrams1(self, strs: list[str]) -> list[list[str]]:

        if len(strs) == 0:
            return [[""]]

        if len(strs) == 1:
            return [strs]

        ans = []
        for i, s in enumerate(strs):

            tmp = [s]
            for t in strs[:i] + strs[i+1:]:

                if len(s) != len(t):
                    continue

                if sorted(s) == sorted(t):
                    tmp.append(t)

            ans.append(tmp)

        uniq_set = {tuple(sorted(a)) for a in ans}
        uniq_list = [list(u) for u in uniq_set]
        return uniq_list

    # second solution(runtime: 90 ms, memory: 20.58 MB)
    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 0:
            return [[""]]

        if len(strs) == 1:
            return [strs]

        map = collections.defaultdict(list)

        for s in strs:

            sorted_str = "".join(sorted(s))

            map[sorted_str].append(s)
        return list(map.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))   # [["bat"],["nat","tan"],["ate","eat","tea"]]
