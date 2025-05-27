class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + ":" + word

        return encoded_string

    def decode(self, s: str) -> list[str]:
        i = 0
        res = []
        while i < len(s):
            word_len = ""
            j = i
            while s[j] != ":":
                word_len += str(s[j])
                j += 1

            word = ""
            j += 1
            end_pos = j + int(word_len)
            while j < end_pos:
                word += s[j]
                j += 1

            i = j
            res.append(word)

        return res

test_cases = [
    ["lint","code","love","you"], 
    ["we", "say", ":", "yes"],
    ["we", "say", "(),sd.s*[]^%l;'-==13fsdfvbsdf')"]]

for test_case in test_cases:
    encoded_string = Solution().encode(test_case)
    print(Solution().decode(encoded_string))