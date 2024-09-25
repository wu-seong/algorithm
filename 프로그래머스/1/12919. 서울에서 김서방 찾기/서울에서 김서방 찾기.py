def solution(seoul):
    # string 배열 순회하면서 'Kim' 찾아서 인덱스 저장하기
    for index, name in enumerate(seoul):
        if name == 'Kim':
            return "김서방은 " + str(index) + "에 있다"