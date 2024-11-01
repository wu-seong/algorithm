from collections import deque
def all_same(arr): # arr를 받아서 같은 수인지 판단
    global result
    num_set = set()
    length = len(arr)
    for i in range(length):
        num_set.update(set(arr[i]))
    if len(num_set) == 1:
        return True
    else:
        return False

def slice_arr(arr):
    i = len(arr)//2
    if i == 0: # 쪼갤 수 없으면 원본 그대로 반환
        return arr
    arr_top = arr[:i]
    arr_bottom = arr[i:]
    arr1 = []
    for j in range(i):
        arr1.append(arr_top[j][:i])
    arr2 = []
    for j in range(i):
        arr2.append(arr_top[j][i:])
    
    arr3 = []
    for j in range(i):
        arr3.append(arr_bottom[j][:i])
    arr4 = []
    for j in range(i):
        arr4.append(arr_bottom[j][i:])
    return [arr1,arr2,arr3,arr4]
    
result = [0,0]
n = 0
def solution(arr):
    global n
    # 처음행의 개수만큼이 n
    # n이 모두 같은지를 판단
    # 하나라도 다르면 4개부분으로 쪼개기 n==1 까지 쪼개기를 반복
    # n == 1이면 더이상 쪼개지 않고 카운팅만
    # 모두 같다면 해당 수를 카운팅    
    n = len(arr)
    
    # i = n -> 1까지 작아지면서 배열을 쪼개고 같은지를 판단 같다면 카운팅
    # 쪼개기 이전에 처음부터 같은지도 판단
    if all_same(arr):
        result[arr[0][0]] += 1
        return result
    i = n
    queue = deque()
    queue.append(arr)
    while queue:
        # queue에서 arr 꺼내오기
        cur_arr = queue.popleft()
        if len(cur_arr) == 1: # 1이면 더이상 쪼개지 않고 카운팅
            result[cur_arr[0][0]] += 1
            continue
        # 배열을 쪼개고 같은지를 판단
        sliced_arr_list = slice_arr(cur_arr)
        #print(sliced_arr_list)
        for sliced_arr in sliced_arr_list:
            if all_same(sliced_arr):
                result[sliced_arr[0][0]] += 1
            else:
                queue.append(sliced_arr)
    return result

# 반복문 재귀문에서 반복적으로 접근하는 리스트에 대해서 수정사항이 있는지 없는지를 생각하기
# 수정사항이 있다면 얕은 복사를 사용하기 어려울 수 있다. 
        
        
        
    
      