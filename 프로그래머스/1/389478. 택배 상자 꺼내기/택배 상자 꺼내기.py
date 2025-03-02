'''
n-1을 w로 나눈 몫 + 1 해서 배열의 길이가 w인 이차원배열 만들기
번호를 1부터 시작해서 n이 될 때 까지 True로 만들기
0 -> w-1 (다음이 W이면 y값 + 1)
w-1 -> 0 (다음이 0이면 y값 + 1)

상자 번호 받아서 본인과 그 위의 True인 값 꺼내기
'''
def solution(n, w, num):
    height = ((n-1) // w) + 1
    box = [[False for _ in range(w)] for _ in range(height)]
    
    i = 1
    y,x = 0,0
    while i <= n:
        while x <= w-1 and i <= n:
            box[y][x] = i
            if x == w-1:
                y += 1
                i += 1
                break
            x += 1
            i += 1

        while x >= 0 and i <= n:
            box[y][x] = i
            if x == 0:
                y += 1
                i += 1
                break
            x -= 1
            i += 1
        
    for b in box:
        print(b)
    
    result = 0
    for i in range(height):
        for j in range(w):
            if box[i][j] == num:
                while i < height and box[i][j]:
                    i += 1
                    result += 1
                print(result)
                return result
            
    
    
    