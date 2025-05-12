class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(0, len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


test_cases = [
    [1, 2, 3, 4], 
    [-1, 1, 0, -3, 3],
    [0, 1, 99, 100, 0]
]

for test_case in test_cases:
    print(Solution().productExceptSelf(test_case))