class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
      groups = {}
      for word in strs:
          list_word = list(word)
          sorted_word_list = sorted(list_word)
          sorted_word = "".join(sorted_word_list)

          if sorted_word not in groups:
              groups[sorted_word] = [word]

          else:
              groups[sorted_word].append(word)

      groups_list = []
      for key, val in groups.items():
          groups_list.append(val)

      return groups_list


test_cases = [
    ["eat","tea","tan","ate","nat","bat"],
    [""],
    ["a"],
    ["", ""],
    ["act","pots","tops","cat","stop","hat"]
]

for test_case in test_cases:
    print(Solution().groupAnagrams(test_case))