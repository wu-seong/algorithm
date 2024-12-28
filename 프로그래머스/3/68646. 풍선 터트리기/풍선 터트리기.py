'''
최후까지 풍선이 남으려면?
만약 항상 번호가 큰 것만을 터뜨린다면?
가장 작은 것이 남게된다.

만약 그런데 번호가 더 작은 것을 한번 터뜨릴 수 있다면?

1 2 3 4 5
첫번째 보다 큰 것이 살아 있을 때 터뜨린다면
2 3 4 5 -> 2

두번째 큰 것이 살아 있을 때
만약 1과 2사이에
n과 n+1번째 숫자 사이의 숫자들은 살아남을 수 없음
n+2의 숫자를 획득하기 위해선 n+1을 n과 비교하여야 하는데 그 사이에 n+2가 있다면 그것이 불가능함
1 6 4 3 2 5

오른쪽에서 가장 작은 것 까지 중 최솟값인 얘들은 모두 가능
왼쪽에서 가장 작은 것 까지 중 최솟값인 얘들도 가능

1. 최솟값 위치 찾기
2. 왼쪽에서 쵯소값 위치까지 범위 넓히며 최솟값 갱신하고 갱신한 것 리스트에 추가
3. 오른쪽도 똑같이 반복

'''
def solution(a):
    n = len(a)
    min_value = min(a)
    min_index = a.index(min_value)
    
    min_result = 1e9 + 1
    result = []
    for i in range(min_index):
        if a[i] < min_result:
            result.append(a[i])
            min_result = a[i]
    
    min_result = 1e9 + 1
    for i in range(n-1, min_index, -1):
        if a[i] < min_result:
            result.append(a[i])
            min_result = a[i]
    #print(result)
    return len(result)+1
   