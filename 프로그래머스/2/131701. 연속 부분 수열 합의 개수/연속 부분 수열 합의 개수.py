
def solution(elements):
    # 길이가 1~len(elements)까지인거 모두 구해서 카운팅하기
    # 결과값을 저장해서 이미 존재하면 카운팅에서 제외
    n = len(elements)
    elements.extend(elements)
    #print(elements)
    
    sums = set([])
    cnt = 0
    for length in range(1, n+1): # 길이
        for start in range(n): # 시작점
            temp = sum(elements[start:start+length])
            if not temp in sums:
                cnt += 1
                sums.add(temp)
    return cnt

# 시작점을 먼저 잡으면 이전 합에 더하여 더 효율적으로 구할 수 있음
        
    
