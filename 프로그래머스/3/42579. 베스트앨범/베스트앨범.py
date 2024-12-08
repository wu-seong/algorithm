
'''
장르별로 가장 많이 재생된 노래 두개씩 찾기
장르를 먼저 수록
해당 장르 내에서 가장 많이 재생된 노래를 수록
같으면, 고유 번호 오름차순

각 장르별로 플레이 수 구하기 (10,000)
장르 내림차순 정렬하기


각 음악에 노래, 장르, id를 구한뒤에
차례로 정렬
'''
from collections import defaultdict

def solution(genres, plays):
    n = len(plays)
    musics = [ [] for _ in range(n)]
    for i in range(n):
        musics[i].append(i)
        musics[i].append(genres[i])
        musics[i].append(plays[i])
    #print(musics)
    # 장르 구하기
    score_cnt = defaultdict(int)
    cnt = defaultdict(int)
    for i, g, c in musics:
        score_cnt[g] += c
        #cnt[g] += 1
    genres = list(set(genres))
    genres.sort(key=lambda x: score_cnt[x], reverse=True)
    print(genres)
    musics.sort(key=lambda x: (genres.index(x[1]), -x[2], x[0] ) )
    
    pre_g = ''
    cnt = 0
    result = []
    for i, g, c in musics:
        if g == pre_g:
            cnt += 1
        else:
            pre_g = g
            cnt = 1
        if cnt <= 2:
            result.append(i)
    print(result)
    return result