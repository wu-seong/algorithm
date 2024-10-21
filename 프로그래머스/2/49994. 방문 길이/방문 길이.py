def solution(dirs):
    # 좌표평면에 방문한 길 기록하기
    # 만약 처음가는 길이면 카운팅 o 방문 추가
    # 가본 곳이면 카운팅 x 
    # 방문 표시는 튜플로 (s_y,s_x,d_y,d_x)
    # 도착지의 절댓값이 5이하이어야 함
    
    # dirs에서 하나씩 읽으면서 이동하기
    visited = set() #(start_y,start_x,)
    start = (0,0)
    move_list = [(1,0),(-1,0),(0,-1),(0,1)] #U,D,L,R
    dir_list = "UDLR"
    cnt = 0
    for d in dirs:
        y,x = start
        idx = dir_list.index(d)
        #print(y,x,move_list[idx])
        dy,dx = move_list[idx][0], move_list[idx][1]
        yy,xx = y+dy, x+dx
        #print("next:", yy,xx)
        # 도착지 인덱스 체크
        if (-5 <= yy and yy <= 5) and (-5 <= xx and xx <= 5):
            # 방문했던 곳인지 확인
            if not (y,x,yy,xx) in visited:
                cnt += 1
                visited.add((y,x,yy,xx))
                visited.add((yy,xx,y,x))
            start = (yy,xx)
    print(cnt)
    return cnt