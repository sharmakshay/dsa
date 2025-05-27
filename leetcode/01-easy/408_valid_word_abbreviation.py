class Solution:
  def validWordAbbreviation(self, word: str, abbr: str) -> bool:
      a, w = 0, 0
      
      while a < len(abbr) and w < len(word):
          if abbr[a] == word[w]:
              a += 1
              w += 1
              continue
          
          if not abbr[a].isdigit() and abbr[a] != word[w]:
              return False
          
          if abbr[a] == '0':
              return False
          
          skip = ""
          while a < len(abbr) and abbr[a].isdigit():
              skip += abbr[a]
              a += 1
          w += int(skip)
      
      return a == len(abbr) and w == len(word)


test_cases = [
    ("internationalization", "i12iz4n"),
    ("abbreviation", "a10n"),
    ("internationalization", "i5a11o1"),
    ("apple", "a2e"),
    ("a", "01"),
    ("a", "1"),
    ("hi", "2"),
    ("hi", "hi1"),
]

for test_case in test_cases:
    print(Solution().validWordAbbreviation(test_case[0], test_case[1]))
