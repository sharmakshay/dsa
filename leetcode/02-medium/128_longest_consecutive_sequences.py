class Solution:

    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        streak = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                length = 0
                while (num + length) in nums_set:
                    length += 1
                streak = max(length, streak)

        return streak


test_cases = [
    [100, 4, 200, 1, 3, 2],
    [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
    [1, 2, 0, 1],
]

for test_case in test_cases:
    print(Solution().longestConsecutive(test_case))