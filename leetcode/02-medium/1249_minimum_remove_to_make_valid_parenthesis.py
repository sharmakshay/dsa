class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        toRemove = []

        for idx, c in enumerate(s):
            if c == "(" or c == ")":
                if len(toRemove) > 0:
                    if s[toRemove[-1]] == "(" and c == ")":
                        toRemove.pop()
                    else:
                        toRemove.append(idx)

                else:
                    toRemove.append(idx)

        new_str = ""
        for idx, c in enumerate(s):
            if idx not in toRemove:
                new_str += c

        return new_str


test_cases = [
    "lee(t(c)o)de)",
    "a)b(c)d",
    "))((",
    "(a(b(c)d)",
]

for test_case in test_cases:
    print(Solution().minRemoveToMakeValid(test_case))