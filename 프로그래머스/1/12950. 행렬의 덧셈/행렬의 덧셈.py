def solution(arr1, arr2):
    answer = [[0 for j in range(len(arr1[i]))] for i in range(len(arr1))]
    for r in range(len(arr1)):
        for c in range(len(arr1[r])):
            answer[r][c] = arr1[r][c] + arr2[r][c]
        #print(answer)
    return answer