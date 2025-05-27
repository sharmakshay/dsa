class Solution:
  def threeSum(self, nums: list[int]) -> list[list[int]]:
      res = {}
      for idx, x in enumerate(nums):
          target = x * -1
          look_up = set()

          for idy, y in enumerate(nums):
              if idx == idy:
                  continue
              diff = target - y

              if diff in look_up:
                  key = sorted([x, y, diff])
                  res[tuple(key)] = 1

              else:
                  look_up.add(y)


      final = [list(x) for x in res.keys()]

      return final

test_cases = [
    [-1,0,1,2,-1,-4],
    [0,1,1],
    [0,0,0],
    [0,0,0,0]
]

for test_case in test_cases:
    print(Solution().threeSum(test_case))