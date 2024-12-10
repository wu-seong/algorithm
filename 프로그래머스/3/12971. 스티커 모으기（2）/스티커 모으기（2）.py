'''
13, 12, -3, 17, -4, 17, 6, 2 

9 -> 11 -> 14 -> 10

인접한 건 어차피 둘 다 못 뜯음
1개만 있으면 1개 선택
2개 있으면 둘 중 큰 것 선택
3개가 있으면 3 중 큰 것 선택
4개가 있으면? (1,3) or (2,4) 선택
5개가 있으면? (1,3) or(2,4), (1,4)

1 - n
2 - n
3 - n 
4 - max(n + n-2, n-1 + n-3)

새 것 추가될 때 n + n-2 와 n-1 + 1

5 - max(n + n-2, n + n-3, n)


연속해서 선택할 순 없음
n + n-2  

'''

def solution(sticker):
    n = len(sticker)
    if n <= 3:
        return max(sticker)
        
    result1 = 0
    pre = sticker[0]
    ppre = sticker[0]
    for s in sticker[2:-1]:
        result1 = max(ppre + s, pre)
        ppre = pre
        pre = result1
    print(result1)
    
    result2 = 0
    pre = sticker[1]
    ppre = sticker[1]
    for s in sticker[3:]:
        result2 = max(ppre + s, pre)
        ppre = pre
        pre = result2
    
    result3 = 0
    pre = sticker[2]
    ppre = sticker[2]
    for s in sticker[4:]:
        result3 = max(ppre + s, pre)
        ppre = pre
        pre = result3
        
    print(result1, result2,result3)
    return max(result1, result2, result3)
    
    

