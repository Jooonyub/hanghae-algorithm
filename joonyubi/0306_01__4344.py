#0306_01__4344.py
#평균은 넘겠지

case_num = int(input())
case_percentages=[]
case_result = []

def over_average(case_list):
    test_case = case_list
    student_number = test_case[0] #student_number는 정수
    student_scores = test_case[1:] #student_scores는 정수형 리스트
    average = sum(student_scores)/student_number #average는 플로트형 평균값(float)

    count = 0
    for student_score in student_scores:
        if student_score > average:
            count = count+1
    over_average = format((count/student_number)*100, '.3f')
    #print(f"{over_average}%")
    return f"{over_average}%"

for i in range(case_num):
    case_input = input().split()
    #case_input.split() #case_input는 정수형 리스트

    for j in range(len(case_input)):
        case_input[j] = int(case_input[j])
        #case_input[j] = case_input[int(j)]
    case_percentage = over_average(case_input)

    #case_percentages[i] = case_percentage
    case_percentages.append(case_percentage)

#print(case_pertentages)

for i in range(len(case_percentages)):
    print(case_percentages[i])






'''
#C = input()

#case = input()


#처음
#처음 입력은 테스트 케이스의 개수 C가 주어진다.
case_num = int(input('case_num:'))
case_percentages=[]
case_result = []

def over_average(case_list):
    test_case = case_list
    student_number = test_case[0] #student_number는 정수
    student_scores = test_case[1:] #student_scores는 정수형 리스트
    average = sum(student_scores)/student_number #average는 플로트형 평균값(float)

    count = 0
    for student_score in student_scores:
        if student_score > average:
            count = count+1
    over_average = format((count/student_number)*100, '.3f')
    #print(f"{over_average}%")
    return f"{over_average}%"

for i in range(case_num):
    case_input = input(f'case_input{i+1}:').split()
    #case_input.split() #case_input는 정수형 리스트

    for j in range(len(case_input)):
        case_input[j] = int(case_input[j])
        #case_input[j] = case_input[int(j)]
    case_percentage = over_average(case_input)

    #case_percentages[i] = case_percentage
    case_percentages.append(case_percentage)

#print(case_pertentages)

for i in range(len(case_percentages)):
    print(case_percentages[i])

'''



#두번째 입력부터는 각 테스트케이스마다 학생수, 각 학생의 점수가 주어진다.
'''
case_percentages = [] -> global 선언
#함수 생성(case_list를 입력값으로 넣어주면 over_average를 출력값으로 반환해줌)
def over_average(case_list):
    test_cases = case_list
    student_number = test_case[0] #student_number는 정수
    student_scores = test_case[1:] #student_scores는 정수형 리스트
    average = sum(student_scores)/student_number #average는 플로트형 평균값(float)

    count = 0
    for student_score in range(student_number):
        if student_score > average:
            count = count+1
    over_average = format((cnt/num)*100, '.3f')
    return over_average

case_percentages.append(over_average(case_list))


for case_percentage in range(case_percentages):
    print(case_percentage)



'''


'''부분부분 잘돌아가는 코드
test_cases=[]
for test_case in range(case_num):
test_case = int(input().split()) #test_case는 정수형 리스트

student_number = test_case[0] #student_number는 정수
student_scores = test_case[1:] #student_scores는 정수형 리스트
average = sum(student_scores)/student_number #average는 플로트형 평균값(float)

#마지막
#출력을 위한 list를 만들어, 각 케이스마다 for문을 통해 결과값을 출력할 수 있도록 한다.
case_percentages = []
for case_percentage in range(case_percentages):
    print(case_percentage)

count = 0
for student_score in range(student_number):
    if student_score > average:
        count = count+1
over_average = format((cnt/num)*100, '.3f')

#만약에 함수가 나왔다고 치면
case_percents = []
for case in range(case_num):
    case_percents.append(over_average())



case_percentover=[]
test_case=[]
for i in range(case_num):
    test_case[i] = []
    test_case[i] = int(input().split())
    case_list[i] = []
    
    for element in test_case[i]:
        case_list[i].append(element) #for문에서 돌아가는 case_list들에 대해 리스트로 만들기
    
    student_number = case_list[i][0]
    scores = case_list[i][1:]
    average = sum(scores)/student_number

    cnt = 0
    for score in scores:
        if score > average:
            cnt = cnt + 1
    over_average = format((cnt/num)*100, '.3f')
    
    case_percentover[i].append(over_average)

for i in range(case_num):
    print(case_percentover[i])

    
    
    #case[i] = []
    #case[i] = input().split()
'''
 
'''
생각 정리좀 하고 하자.
<입력>
첫줄은 테스트케이스 수
두번째줄부터는 각 테스트케이스의 수와 점수 나열

<출력>
각 테스트케이스의 평균점수 이상인 학생들의 비율(with for문)
'''


'''
case=input()
test_case=[]
for i in case:
    i = int(i)  #입력문자를 정수화하기
    test_case.append(i) #test_case라는 리스트에 각 열을 정수로 담기(첫번째 인자는 학생 수, 그 후로는 각각의 점수)

student_number = int(test_case[0])
scores = test_case[1:]
average = sum(scores)/num

cnt = 0
for score in scores:
    if score > average:
        cnt = cnt + 1
over_average = format((cnt/num)*100, '.3f')
print(f"{over_average}%")
'''
'''
문제
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

입력
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

예제 입력 1 
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
예제 출력 1 
40.000%
57.143%
33.333%
66.667%
55.556%
'''