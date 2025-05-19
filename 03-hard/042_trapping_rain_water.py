class Solution:
  def trap(self, height: list[int]) -> int:
      l, r = 0, len(height) - 1
      maxL, maxR = 0, 0
      caught = 0
      while l < r:
          if height[l] <= height[r]:
              maxL = max(maxL, height[l])
              caught += max(maxL - height[l], 0)
              l += 1

          else:
              maxR = max(maxR, height[r])
              caught += max(maxR - height[r], 0)
              r -= 1

      return caught


test_cases = [
    [0,2,0,3,1,0,1,3,2,1],
    [4,2,0,3,2,5],
    [0,1,0,2,1,0,1,3,2,1,2,1]
]

for test_case in test_cases:
    print(Solution().trap(test_case))