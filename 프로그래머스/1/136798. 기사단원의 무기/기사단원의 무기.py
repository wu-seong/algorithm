def get_divisor_cnt(num):
    d_list = []
    for i in range(1,int(num**0.5)+1):
        if num % i == 0:
            d_list.append(i)
            d_list.append(num//i)
    return len(set(d_list))
def solution(number, limit, power):
    # 각 number마다 약수의 개수를 구한다
    # 개수가 > limit 이면 power로 교체한다.
    cnt = 0
    for i in range(1,number+1):
        d_cnt = get_divisor_cnt(i)
        cnt += d_cnt if d_cnt <= limit else power
        #print(cnt)
    return cnt