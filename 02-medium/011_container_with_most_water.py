class Solution:

    def maxArea(self, heights: list[int]) -> int:
        left, right = 0, len(heights) - 1
        maxArea = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            maxArea = max(maxArea, area)

            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1

        return maxArea


test_cases = [
    [1, 8, 6, 2, 5, 4, 8, 3, 7],
    [1, 1],
    [1, 7, 2, 5, 4, 7, 3, 6],
]

for test_case in test_cases:
    print(Solution().maxArea(test_case))
