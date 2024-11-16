def solution(k, d):
    '''
    1 인경우
    
    각 x지점 마다 찍을 수 있는 y의 개수를 구하기
    
    원방에 x를 통해 y를 구한뒤에 해당 값의 소숫점을 제거하기 k개로 나눈 몫 + 1
    '''
    def get_y(x, d):
        # x2 + y2 = d2
        return (d**2 - x**2)**0.5
    result = 0
    for i in range(0, d+1, k):
        #print(i, int(get_y(i, d))//k + 1)
        result += int(get_y(i, d))//k + 1
    print(result)
    return result
    