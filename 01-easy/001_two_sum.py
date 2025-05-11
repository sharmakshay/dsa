class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    track = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in track:
            return [track[diff], i]

        else:
            track[num] = i

    return []



test_cases = [
    ([2,7,11,15], 9),
    ([3,2,4], 6),
    ([3,3], 6),
    ([1,2,3,4,5,6,7,8,9,10], 15)
]

for test_case in test_cases:
    print(Solution().twoSum(test_case[0], test_case[1]))