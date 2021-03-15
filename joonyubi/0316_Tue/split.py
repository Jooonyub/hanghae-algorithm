
import sys
r = sys.stdin.readline


string = r()
string1 = string.strip()
string2 = string.split()

print(string)
print(string1)
print(string2)


if string1 == "pop":
    print("잘됨")
else:
    print("뭔가 문제")

if string2 == "pop":
    print("잘됨")
else:
    print("뭔가 문제")
'''
command, num = map(str, string.split())

print(f"command : {command}, num : {num}")
print(type(command))
print(type(num))
'''