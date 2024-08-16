def solution(array, commands):
    answer = []
    for c in commands:
        i,j,k = c
        s_array = array[i-1:j]
        s_array.sort()
        answer.append(s_array[k-1])
    return answer