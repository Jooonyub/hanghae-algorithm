#0312_01_1316.py
#그룹 단어 체커

import sys
r = sys.stdin.readline

N = int(r())

#연속해서 나오지 않는 기출력 문자는 다시 나와서는 안된다.
#연속되어있느냐 그렇지 않느냐 여부가 중요할듯..

def dup_avoid(word):
    #chars = word.split()
    used_char = []
    #previous_char = None
    for i in range(len(word)):            #단어의 각 글자를 나타내는 반복문
        if word[i] not in used_char:      #처음보는 문자이면 used_char에 추가
            used_char.append(word[i])
            continue
        else:                                #기존에 나타났던 문자라면?
            if i != 0 and word[i] != used_char[-1]:    #직전의 문자와 다르면 false 반환
                return False
        #previous_char = word[i]
    return True

cnt = 0
for i in range(N):                  #횟수에 대한 반복문
    caseword = r()
    if dup_avoid(caseword):
        cnt += 1

print(cnt)

'''
문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.

예제 입력 1 
3
happy
new
year
예제 출력 1 
3
예제 입력 2 
4
aba
abab
abcabc
a
예제 출력 2 
1
'''