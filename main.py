import os

print("NeetCode 150 ...")
leetcode_dir = "leetcode"
for folder in os.listdir(leetcode_dir):
  print(folder)
  for file in os.listdir(f"{leetcode_dir}/{folder}"):
    if file.endswith(".py"):
      print(f"{folder}.{file[:-3]}")
      __import__(f"{leetcode_dir}.{folder}.{file[:-3]}")