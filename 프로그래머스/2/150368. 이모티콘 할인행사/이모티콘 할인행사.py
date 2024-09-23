def calculate_sum(emoticons, percentage, users):
    # 각 이모티콘 마다 기준을 넘기면 총 매출에 포함
    total_sum = 0
    plus_user_cnt = 0
    for user_per, max_value in users:
        user_sum = 0
        for i in range(len(emoticons)):
            if percentage[i] >= user_per: # 할인율 이상되어야 구입
                user_sum  += emoticons[i]*(100-percentage[i])/100
        #print(user_sum, max_value)
        if user_sum >= max_value: # 기준치 이상이면 가입
            plus_user_cnt += 1
        else:
            total_sum += user_sum
    return plus_user_cnt, total_sum


def dfs(emoticons, level, discount_per_list, users):
    global max_user
    global max_total_sum
    if level == len(emoticons):
        user_cnt, total_sum = calculate_sum(emoticons, discount_per_list, users)
        if user_cnt > max_user: # 더 많은 유저 수
            max_user = user_cnt
            max_total_sum = total_sum
        elif user_cnt == max_user and total_sum > max_total_sum:
            max_total_sum = total_sum 
        return
    for discount_per in (10,20,30,40):
        discount_per_list[level] = discount_per
        dfs(emoticons, level+1, discount_per_list, users)

max_user = 0
max_total_sum = 0

def solution(users, emoticons):
    # 각 이모티콘 당 할인율에 대해 DFS
    dfs(emoticons, 0, [0]*len(emoticons), users)
    # print(max_user, int(max_total_sum))
    return [max_user, int(max_total_sum)]