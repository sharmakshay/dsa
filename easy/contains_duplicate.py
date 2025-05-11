class Solution:
  def hasDuplicate(self, nums: list[int]) -> bool:
      nums_dict = {}
      for num in nums:
          if num not in nums_dict:
              nums_dict[num] = 1
          else:
              return True

      return False


test_cases = [
    [1,2,3,1],
    [1,2,3,4],
    [1,1,1,3,3,4,3,2,4,2]
]

for test_case in test_cases:
    print(Solution().hasDuplicate(test_case))