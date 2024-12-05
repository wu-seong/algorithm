from heapq import heappop, heappush, heapify
'''
처음에 A,B 정렬시키기
큰것부터 보고 만약 B에서 것보다 큰 것이 없다면 

1 3 5 7 11 26 28
2 6 6 8 12 25 35 

둘 다 최대heap으로 만들고

A에서 pop 하면서 A >= B이면 min 갱신 (앞에서 빼기)
A < B 이면 B에서도 pop


'''
def solution(A, B):
    A = [-a for a in A]
    B = [-b for b in B]
    heapify(A)
    heapify(B)
    result = 0
    while A:
        a = -heappop(A)
        #print(a,-B[0])
        if a < -B[0] : 
            result += 1
            heappop(B)
    print(result)
    return result