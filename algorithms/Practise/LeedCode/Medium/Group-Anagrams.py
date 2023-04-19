import collections
import time
from typing import List, Any

"https://leetcode.com/problems/group-anagrams/description/"

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def time_taken(func):
    def inner_func(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Function : {func.__name__}")
        print(f"Finished in : {(end - start):.2f}s")
        return result

    return inner_func


class Solution:
    @time_taken
    def groupAnagrams1(self, strs):
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        # print(ans.values())

    @time_taken
    def groupAnagrams2(self, strs):
        dic = {}
        for s in strs:
            w = "".join(sorted(s))
            if w in dic:
                dic[w].append(s)
            else:
                dic[w] = [s]
        # print(dic.values())

    @time_taken
    def groupAnagrams3(self, strs: List[str]):
        final_result = []
        unique_list = set()
        for i in range(len(strs)):
            result = []
            if "".join(sorted(strs[i])) not in unique_list:
                unique_list.add("".join(sorted(strs[i])))
                result.append(strs[i])
                for j in range(i + 1, len(strs)):
                    if "".join(sorted(strs[i])) == "".join(sorted(strs[j])):
                        result.append(strs[j])
                final_result.append(result)
        # print(final_result)

    @time_taken
    def groupAnagrams4(self, _strs):
        d = {}
        for s in _strs:
            _f = ""
            for c in sorted(s):
                _f += str(s.count(c)) + c
            if _f in d:
                d[_f].append(s)
            else:
                d[_f] = [s]
        # print(d.values())


s = Solution()
s.groupAnagrams1(strs)
s.groupAnagrams2(strs)
# s.groupAnagrams3(strs)
s.groupAnagrams4(strs)
