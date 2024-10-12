def solution(citations):
    # h = 1일때, 1이상인 citations를 count하기
    # h 이상인 citations를 count하기
    # 완탐 - 1000만
    # 역순 정렬시
    # 6,5,3,1,0
    # 5,4,3,3
    # [:h]로 잘라서 마지막 원소가 h이상이면 h갱신 아니면 끝
    # 모든 원소까지 이상이 없으면 해당 원소길이가 답
    citations.sort(reverse=True)
    h = 0
    l = len(citations)
    while True:
        h += 1
        if citations[:h][-1] < h or h > l :
            return h-1