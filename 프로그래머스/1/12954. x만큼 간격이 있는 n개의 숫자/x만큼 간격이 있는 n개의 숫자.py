def solution(x, n):
    answer = []
    if x > 0:
        end = (x*n)+1
    elif x == 0:
        return [0]*n
    else:
        end = (x*n)-1
    for i in range(x,end,x):
        answer.append(i)
    return answer