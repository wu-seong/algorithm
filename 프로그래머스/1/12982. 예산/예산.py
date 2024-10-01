def solution(d, budget):
    # 오름 차순으로 정렬 후 
    d.sort()
    # 순서대로 예산에서 빼면서 카운팅, 예산보다 크면 그만두기
    cnt = 0
    for need in d:
        if need <= budget:
            cnt += 1
            budget -= need
        else:
            break
    return cnt
    