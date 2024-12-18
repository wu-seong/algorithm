'''
2 하나이면 1로 시작하는 펄스 수열
2 3 뒤에 같은 부호가 나오니 둘 중 하나를 선택 해야함
3 > 2 이므로 -2 3
-6이 들어오면 앞의 3과 다른 부호이니

부분합?

1로 시작하는 펄스 수열 전체에 곱하기
연속된 부분 수열 중 가장 합이 큰 것 찾기

2 5 -5 2 5 4 6 10
1 -7 5 -3 9

1 -6 -1 -4 5

가장 큰 게 더 앞에있고 가장 작은게 더 뒤에 있는 경우
1234 -4-5
... 10 6 -11

dp
9 7 5 


부분합 구해서 가장 큰 값 - 가장 작은 값? or 0

-1로 시작..
'''
def solution(sequence):
    n = len(sequence)
    pers1 = [sequence[i] if i % 2 else -sequence[i] for i in range(n)]
    pers2 = [-sequence[i] if i % 2 else sequence[i] for i in range(n)]
    sum1, sum2 = [0 for _ in range(n)], [0 for _ in range(n)]
    sum1[0], sum2[0] = pers1[0], pers2[0]
    #print(pers1, pers2)
    for i in range(1, n):
        sum1[i] += pers1[i] + sum1[i-1] 
        sum2[i] += pers2[i] + sum2[i-1]
    #print(sum1, sum2)
    max1, max2 = (-1e5,-1), (-1e5,-1)
    min1, min2 = (1e5,-1), (1e5,-1)
    for i in range(n):
        if sum1[i] >= max1[0]:
            max1 = (sum1[i], i)
        if sum1[i] < min1[0]:
            min1 = (sum1[i], i)
        if sum2[i] >= max2[0]:
            max2 = (sum2[i], i)
        if sum2[i] < min2[0]:
            min2 = (sum2[i], i)
    #print(max1, min1)
    # 만약 max가 더 앞이면 그냥 max만, 더 뒤면 max - min(음수일 때)
    result1 = max1[0] if max1[1] < min1[1] else max1[0] - min(min1[0], 0)
    result2 = max2[0] if max2[1] < min2[1] else max2[0] - min(min2[0], 0)
    return max(result1, result2)