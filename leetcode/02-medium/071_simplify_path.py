class Solution:
  def simplifyPath(self, path: str) -> str:
      path_arr = path.split("/")
      canonical_path = []

      for elem in path_arr:
          if elem == "/" or elem == "." or elem == "":
              pass

          elif elem == "..":
              if len(canonical_path) > 0:
                  canonical_path.pop()

          else:
              canonical_path.append(elem)


      return "/" + "/".join(canonical_path)

test_cases = [
    "/home/",
    "/../",
    "/home//foo/",
    "/.../a/../b/c/../d/./",
]

for test_case in test_cases:
    print(Solution().simplifyPath(test_case))