def solution(answers):
    a1 = 0
    a1_num = [1,2,3,4,5]
    a2 = 0
    a2_num = [2,1,2,3,2,4,2,5]
    a3 = 0
    a3_num = [3,3,1,1,2,2,4,4,5,5]
    cnt = [0]*3
    for i in range(len(answers)):
        a1 = a1_num[i%5]
        a2 = a2_num[i%8]
        a3 = a3_num[i%10]
        if a1 == answers[i]:
            cnt[0] += 1
        if a2 == answers[i]:
            cnt[1] += 1
        if a3 == answers[i]:
            cnt[2] += 1
    max_cnt = 0
    result = []
    print(cnt)
    for i in range(3):
        if cnt[i] > max_cnt:
            max_cnt = cnt[i]
            result = [i+1]
        elif cnt[i] == max_cnt:
            result.append(i+1)
    return result