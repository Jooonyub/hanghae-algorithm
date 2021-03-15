import sys

strings = []
i = 0
while True:
    strings[i] = str(sys.stdin.readline())
    if strings[i] == ".":
      break
    i += 1

for string in strings:
  print(string)