class Solution:
  def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
      """
      Do not return anything, modify nums1 in-place instead.
      """
      p1 = m-1
      p2 = n-1
      pCurr = len(nums1) - 1

      while p2 >= 0:
          curr = nums1[pCurr]
          num1 = nums1[p1]
          num2 = nums2[p2]

          if num1 > num2 and p1 >= 0:
              nums1[pCurr] = num1
              nums1[p1] = curr
              p1-=1

          else:
              nums1[pCurr] = num2
              nums2[p2] = curr
              p2-=1

          pCurr -= 1


test_cases = [
    ([1,2,3,0,0,0], 3, [2,5,6], 3),
    ([1], 1, [], 0),
    ([0], 0, [1], 1),
    ([1,2,4,5,6,0], 5, [3], 1),
    ([4,5,6,0,0,0], 3, [1,2,3], 3),
    ([4,0,0,0,0,0], 1, [1,2,3,5,6], 5),
    ([1,2,3,0,0,0], 3, [4,5,6], 3),
]

for test_case in test_cases:
    print(Solution().merge(*test_case))
