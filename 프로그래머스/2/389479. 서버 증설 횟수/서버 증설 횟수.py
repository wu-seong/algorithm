'''
서버를 증설한 횟수
현재 게임 이용자 수와 증설된 서버의 수를 비교해서 증설해야하면 증설 횟수를 카운팅하고 증설하기

각 시간마다 players 수를 이전의 players 수에 더하기
합산 players가 현재 서버의 대수로 감당이 안되면 서버를 증설


꺼진 서버 반영

((전체 유저 수) - (현재 서버가 수용가능한 유저 수 = 서버의 수 * (m-1) ) = (잉여 유저 수) 

if 잉여 유저 수 > 0
    (잉여 유저 수 // m) + 1 만큼 서버 증설 및 카운팅 (k시간 뒤에 꺼질 것도 체크)


처음은 1대라고하고 m-1명까지 수용가능
 
'''
def solution(players, m, k):
    add_cnt = 0 # 증설 횟수
    s_cur_cnt = 1 # 현재 서버 수(1대는 꺼지지 않음)
    close_server = [0] * 24
    for i, p_cnt in enumerate(players):
        s_cur_cnt += close_server[i]
        
        remain_user = p_cnt - (s_cur_cnt*m) + 1
        if remain_user > 0:
            need_server = (remain_user//m)
            if remain_user % m != 0:
                need_server += 1
            add_cnt += need_server
            s_cur_cnt += need_server
            print('게임 이용자 수:', p_cnt, '수용해야하는 유저 수:', remain_user, '현재 서버 수', s_cur_cnt, '증설된 서버 수:', need_server)
            if i+k < 24:
                close_server[i+k] -= need_server
    print(add_cnt)
            
    return add_cnt
        
    
    