class Solution:

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for key, val in count.items():
            freq[val].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            arr = freq[i]
            for val in arr:
                res.append(val)

                if len(res) == k:
                    return res

        return res


test_cases = [([1, 1, 1, 2, 2, 3], 2), ([1], 1), ([1, 2], 2),
              ([1, 2, 2, 3, 3, 3], 2), ([1, 2, 2, 2, 3, 3, 3], 3)]

for test_case in test_cases:
    print(Solution().topKFrequent(test_case[0], test_case[1]))
