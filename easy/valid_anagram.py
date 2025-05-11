class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        letter_count = {}
        for c in s:
            if c in letter_count:
                letter_count[c] += 1
            else:
                letter_count[c] = 1

        for c in t:
            if c in letter_count:
                letter_count[c] -= 1

                if letter_count[c] == 0:
                    letter_count.pop(c)

            else:
                return False

        if not (letter_count):
            return True

        return False


test_cases = [
    ("anagram", "nagaram"),
    ("rat", "car"),
    ("a", "ab"),
    ("racecar","carrace")
]

for test_case in test_cases:
    print(Solution().isAnagram(test_case[0], test_case[1]))