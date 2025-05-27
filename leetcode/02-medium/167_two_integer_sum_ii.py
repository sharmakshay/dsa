class Solution:

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        goal = None
        pointerA = 0
        pointerB = len(numbers) - 1

        while goal != target:
            goal = numbers[pointerA] + numbers[pointerB]

            if goal < target:
                pointerA += 1

            elif goal > target:
                pointerB -= 1

        return [pointerA + 1, pointerB + 1]


test_cases = [
    ([2, 7, 11, 15], 9),
    ([2, 3, 4], 6),
    ([-1, 0], -1),
]

for test_case in test_cases:
    print(Solution().twoSum(test_case[0], test_case[1]))
