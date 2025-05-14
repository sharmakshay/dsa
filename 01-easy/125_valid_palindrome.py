class Solution:

    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()

        for i in range(0, len(new_str) // 2):
            start_pointer = i
            end_pointer = len(new_str) - i - 1

            if new_str[start_pointer] != new_str[end_pointer]:
                return False

        return True

test_cases = ["A man, a plan, a canal: Panama", "race a car", " ", "a", "ab", "abba"]

for test_case in test_cases:
    print(Solution().isPalindrome(test_case))
