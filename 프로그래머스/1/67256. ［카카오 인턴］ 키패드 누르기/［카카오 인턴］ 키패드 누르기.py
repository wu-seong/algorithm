def solution(numbers, hand):
    """
    왼손 엄지와 오른손 엄지의 현재 위치를 4*3 배열에 나타내기
    시작점은 L = (3,0) R = (3,2)
    
    숫자배열을 순회하면서 각 숫자를 배열에 나타내기
    ex) 1 = (0,0)
    
    숫자가 1,4,7인 경우 = 왼손 엄지
    3,6,9인 경우 = 오른손 엄지
    중간인 경우 
    = 숫자와 현재 L,R의 거리를 계산해서 더 가까운 손을 이동시키고 표시하기
    
    거리가 같을 경우에는 hand에 표시된 손가락을 이용
    """
    
    def get_distance(a,b):
        start_y, start_x = a
        end_y, end_x = b
        return abs(end_y - start_y) + abs(end_x - start_x)
    coordinate = {} 
    for i in range(3):
        for j in range(3):
            coordinate[i*3 + j+1] = (i,j)
    coordinate['*'] = (3,0)
    coordinate[0] = (3,1)
    coordinate['#'] = (3,2)
    l_hand, r_hand = (3,0), (3,2)
    l_side, r_side = (1,4,7), (3,6,9)
    result = []
    for number in numbers:
        number_coordinate = coordinate[number]
        if number in l_side:
            l_hand = number_coordinate
            result.append('L')
        elif number in r_side:
            r_hand = number_coordinate
            result.append('R')
        else:
            l_distance = get_distance(l_hand, number_coordinate)
            r_distance = get_distance(r_hand, number_coordinate)
            if l_distance == r_distance:
                if hand =="right":
                    r_hand = number_coordinate
                    result.append('R')
                else:
                    l_hand = number_coordinate
                    result.append('L')
            elif  l_distance < r_distance:
                l_hand = number_coordinate
                result.append('L')
            else:
                r_hand = number_coordinate
                result.append('R')   
    return "".join(result)
        
                    
        
            
    
    
    