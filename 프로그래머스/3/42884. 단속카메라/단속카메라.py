'''
차량의 출발점과 끝점 사이에 최소 1개의 카메라가 있어야함
마지막 진출 시점에 카메라를 두기

진출 시점 기준으로 오름차순 정렬

다음 차의 진입 시점이 마지막 카메라 보다 앞이면 
해당 차의 진출 시점에 카메라 새로 두기
'''
def solution(routes):
    routes.sort(key = lambda x: x[1])
    #print(routes)
    
    last_camera = -30001
    cnt = 0
    for s,e in routes:
        if s > last_camera: # 카메라 밖에서 시작하면
            cnt += 1
            last_camera = e
    return cnt
            