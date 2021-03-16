
'''
num_list = [-3,-2,-1,-2,-1]
num_list.sort()     #[-3, -2, -2, -1, -1]

cnt_max = 0         # cnt_max 초기화
most_nums = []      # most_nums 초기화

num_set = set(num_list)     # {-3, -2, -1} _ set
num_set_cnt = []            # num_set_cnt 초기화

list_num_set = list(num_set)    # -3, -2, -1 _ list
for num in list_num_set:        # num_set_cnt = [1, 2, 2]
    num_set_cnt.append(num_list.count(num))



cnt_max = max(num_set_cnt)              # cnt_max = 2
num_modes = num_set_cnt.count(cnt_max)  # num_modes = 2

for i in range(len(list_num_set)):      #range(3)
    if num_list.count(list_num_set[i]) == cnt_max:  # 
        most_nums.append(list_num_set[i])   #most_nums

if num_modes == 1:
    print(most_nums[0])
else:
    print(most_nums[1])
'''
N = 5
testcase1 = [1,3,8,2,-2]
testcase2 = [-1,-2,-3,-1,-2]
#셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

'''
testcase1의 경우
[1,3,8,2,-2] -> [-2,1,2,3,8] -> 빈도는 [1,1,1,1,1] -> max(빈도)=1 -> count(리스트[i]) 일치하는 리스트[i] 다 선택 -> 여러개면 두번째 작은 값. 하나면 그 값.
[-1,-2,-3,-1,-2] -> [-3,-2,-2,-1,-1] 빈도는 
1. 입력받은 리스트를 정렬한다.
2. 세트(집합)를 활용한다.
'''
'''
count_info = {
    1: 3,
    2: 2
}
print(count_info.keys())
print(count_info.values())
'''




def mode(n, num_list):

    cnt_max = 0
    most_nums = []

    num_list.sort()
    #num_set = set(num_list.sort())
    count_info = {}
    for i in range(n):
        if num_list[i] not in count_info.keys():
            count_info[num_list[i]] = num_list.count(num_list[i])
    #여기까지하면 dict에 오름차순의 숫자별 빈도를 담은 dict 담김

    cnt_max = max(count_info.values())

    for num in count_info.keys():
        if count_info[num] == cnt_max:
            most_nums.append(num)
    #most_nums.append(num) if num == cnt_max for num in count_info.keys() 

    if len(most_nums) > 1:
        return most_nums[1]
    else:
        return most_nums[0]

print(mode(N,testcase1))
print(mode(N,testcase2))

'''    

num_set_cnt = []

list_num_set = list(num_set)
for num in list_num_set:
    num_set_cnt.append(num_list.count(num))

cnt_max = max(num_set_cnt)
num_modes = num_set_cnt.count(cnt_max)

for i in range(len(list_num_set)):
    if num_list.count(list_num_set[i]) == cnt_max:
        most_nums.append(list_num_set[i])

if num_modes == 1:
    return most_nums[0]
else:
    return most_nums[1]
'''
