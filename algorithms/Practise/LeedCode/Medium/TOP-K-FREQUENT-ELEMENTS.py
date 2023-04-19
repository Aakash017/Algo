"https://leetcode.com/problems/top-k-frequent-elements/description/"


class Solution:
    def topKFrequent(self, nums, k: int):
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        new_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        print(new_d)
        result = []
        c = 0
        for i in new_d:
            if c < k:
                result.append(i[0])
                c += 1
            else:
                break
        return result

    def topKFrequent_optimal(self, nums, k: int):
        l = []
        for n in nums:
            l.insert(nums.count(n), [n])
        print(l)


s = Solution()
s.topKFrequent_optimal([1, 1, 1, 2, 2, 3], 3)
