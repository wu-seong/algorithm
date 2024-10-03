def solution(need, reward, n):
    # n의 개수가 need보다 작을 때 까지 반복
    # n은 need로 나눈 몫*reward 와 나머지의 합이다.
    cnt = 0
    while n >= need:
        cnt += (n//need) * reward
        n = ((n//need) * reward ) + (n%need)
    #print(cnt)
    return cnt