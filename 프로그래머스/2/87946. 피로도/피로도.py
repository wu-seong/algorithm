from copy import deepcopy
def adv(remain, dung, cnt):
    global max_cnt, visited
    # 모든 던전을 돌거나, 더 이상 진행할 수 있는 던전이 없으면 그만두기
    # 현재 남은 피로도와 남은 던전의 필요 필요도를 비교하여 있으면 재귀, 없으면 끝
    # 남은 던전이 없어도 끝
    end = True
    #print(remain, dung, cnt)
    for i in range(len(dung)):
        need, reduce = dung[i]
        if remain < need or i in visited: # 더 작거나 방문한 곳이면 pass
            continue
        else: # 크거나 같으면 탐험
            end = False
            visited.add(i)
            adv(remain-reduce, dung, cnt+1)
            visited.remove(i)
    # 더 작은게 아무것도 없으면 or 남은 던전이 없으면 끝
    if end:
        max_cnt = max(max_cnt, cnt)
    return
                
max_cnt = 0
visited = set()
def solution(k, dungeons):
    # 가장 높은 필요 피로도를 골랐을 때, 소모 피로도가 많을 수 있음
    # 가장 낮은 소모 피로도를 골랐을 때, 가장 높은 필요 피로도를 못할 수 있음
    # 그리디 x
    # k<5000, 던전 개수는 8, 완탐으로도 될듯
    # 8!
    adv(k, dungeons, 0)
    #print(max_cnt)
    return max_cnt

# 백트래킹 시에 리스트에는 변경을 주지 않고, 추가적인 방문 표시를 통해서 구별하기
# 리스트 변경 시에 이후에 진행할 탐색이 일관성이 사라질 수 있음 