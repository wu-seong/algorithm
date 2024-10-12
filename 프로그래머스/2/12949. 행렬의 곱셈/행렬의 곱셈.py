def solution(arr1, arr2):
    result = [ [0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    #1행과 1열의 곱의 합이 1행 1열의 원소가 됨
    #1행과 2열의 곱의 합이 1행 2열의 원소가 됨
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            row1 = arr1[i]
            col2 = []
            for row2 in arr2:
                col2.append(row2[j])
            sum = 0
            for k in range(len(arr2)):
                sum += row1[k]*col2[k]
            result[i][j] = sum
    #print(result)
    return result
                
            
        
        
                
    