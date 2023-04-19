"https://leetcode.com/problems/longest-consecutive-sequence/description/"


def longestConsecutive(nums) -> int:
    numSet = set(nums)
    longest = 0
    for n in nums:
        # Check if this is starting of sequence
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest
