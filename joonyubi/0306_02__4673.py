# 0306_02__4673.py
# 셀프넘버(2021.03.06 15:39:00)

'''
기능 구현
0부터 10000까지 순차적으로 반복한다.
i번째 수에 대해서 해당 수보다 작은 수들에 대해 일정형식의 연산을 했을때 동일한 값이 안나오면 셀프넘버.
    일정 형식의 연산
    for self

    while True:
        i = i + i%10
        nonself_number.append(i)
        if int(i/10) == 0:
            break


모든 수는 생성자 or 셀프넘버
생성자 : 2 4 6 8 10 11 12 13 14 15 16 17 18 19 20
셀프넘버 : 1 3 5 7 9 20 ...
'''
nonself_number = []
self_number = []

# 전수검사를 위한 반복문
for (i=0; i <= 10000; i++):
    #할때까지 무한반복
    while True:
        i = i + i % 10
        if i <= 10000:
            if i not in nonself_number:
                self_number.append(i)
        nonself_number.append(i)
        if int(i/10) == 0:
            break

'''
# 원래의 수에 각 자리수를 더한다.
num + num%10 + int(num/10)%10 + int(num/10)%10


1   num
2   num%10  int(num/10)
3   (int(num/10))%10 int(int(num/10)/10)
4
5
6
7

for (i = 0; i <= 10000; i++):
    sum = 0
    num_history = []
    while True:
        sum = i + i%10

sum = 0

while sum <= 10000 :
    sum = sum + num
    num = int(num/10)


factors = []
while True:
    factors.append(num)


def selfnumber(num):
    total = 0
    while True:
        total = total + (num % 10)
        num = int(num/10)

        if num == 0:
            break
    return total

num = 0
total = 0
while True:

print("정상")


'''
문제
셀프 넘버는 1949년 인도 수학자 D.R. Kaprekar가 이름 붙였다. 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자. 예를 들어, d(75) = 75+7+5 = 87이다.

양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다.

예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57이다. 이런식으로 다음과 같은 수열을 만들 수 있다.

33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...

n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고, 39는 51의 생성자, 51은 57의 생성자이다. 생성자가 한 개보다 많은 경우도 있다. 예를 들어, 101은 생성자가 2개(91과 100) 있다.

생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있다. 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97

10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

입력
입력은 없다.

출력
10, 000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.

예제 입력 1
예제 출력 1
1
3
5
7
9
20
31
42
53
64
 |
 | < -- a lot more numbers
 |
9903
9914
9925
9927
9938
9949
9960
9971
9982
9993
'''
