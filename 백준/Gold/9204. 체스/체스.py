'''
1. 이차원 배열에 좌표로 나타내기 
2. 둘 간의 맨해튼 거리가 홀수이면 불가능
3. 짝수이면 둘 간에 갈 수 있는 공통 경유지를 찾기
    0 이면 위치 그대로 
    처음 갈 수 있는 곳에 목적지가 있으면 
    그렇지 않으면
    모든 위치 중에서 겹치는 위치 후 목적지 위치
'''
T = int(input())
index = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
alpah = 'ABCDEFGH'

def can_go(y,x):
    can_list = set()
    i,j = y,x
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        can_list.add((i,j))
    i,j = y,x
    while i < 7 and j > 0:
        i += 1
        j -= 1
        can_list.add((i,j))
    i,j = y,x
    while i < 7 and j < 7:
        i += 1
        j += 1
        can_list.add((i,j))
    i,j = y,x
    while i > 0 and j < 7:
        i -= 1
        j += 1
        can_list.add((i,j))
    #print(can_list)
    return can_list


for _ in range(T):
    s_col, s_row, d_col, d_row = input().split(" ")
    s_col, d_col = index[s_col], index[d_col]
    s_row, d_row = 8 - int(s_row), 8 - int(d_row)

    #print(s_row, s_col, d_row, d_col)

    distance = abs(s_row - d_row) + abs(s_col - d_col)
    if distance % 2 == 1:
        print('Impossible') 
    elif distance == 0:
        print('0', alpah[s_col], 8 - s_row)
    else:
        next_set = can_go(s_row, s_col)
        if (d_row, d_col) in next_set:
            print('1', alpah[s_col], 8 - s_row, alpah[d_col], 8 - d_row)
        else:
            pre_set = can_go(d_row, d_col)
            
            bridge = next_set.intersection(pre_set)
            any = bridge.pop()
            print('2', alpah[s_col], 8 - s_row, alpah[any[1]], 8 - any[0] ,alpah[d_col], 8 - d_row)
