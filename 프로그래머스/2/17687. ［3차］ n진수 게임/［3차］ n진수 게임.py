'''
최대 1000개만 말하면 되고 참가하는 인원이 100 이니
100* 1000 = 10만 그냥 시뮬레이션 돌려서 다 구하면 될듯

최대 구해야 할 순서를 먼저 구하고
미리 구할 숫자의 개수가 1 -> 내순서
2 - 내 순서 + 게임 참가 인원
 = (t-1)*m + p
그 순서까지 n진법에 따라 시뮬레이션 돌리기
p로 나머지 연산후에 m으로 나누어 떨어질 때 마다 result에 추가하기

n진법 이니 n에 따라서 시뮬레이션 돌릴 숫자가 달라짐
10진법이면 이대로 구하고 str으로 바꿔서 하나씩 말하게하기
n진법일 때 다음 숫자 구하기:
10 
10 
n으로 나눈 나머지 -> 0 앞에 붙이기 0
n으로 나눈 몫 = 5
n으로 나눈 나머지 -> 1 앞에 붙이기 10
n으로 나눈 몫 = 2
n으로 나눈 나머지 -> 0 앞에 붙이기 010
n으로 나눈 몫 = 1 
이전에 구한 몫이 n보다 작으면 그대로 몫 가져다 붙이면 끝
앞에 붙이기 1010

n이 만약 10을 넘으면?
n으로 나눈 나머지에 따라 'ABCDEF' 붙이기



'''    
def solution(n, t, m, p):
    def to_n(num):
        temp = []
        while num >= n: 
            temp.append(num % n)
            num = num // n
        temp.append(num)
        temp = temp[::-1]
        return temp
    
    # 변환된 숫자의 길이를 구하고 가져다 붙이기 ((t-1)*m + p) 까지 
    i = 0
    all = []
    while len(all) <= (t-1)*m + p:
        all.extend(to_n(i))
        i += 1
    # m으로 나눈 나머지가 p인것만 구하기
    result = []
    # 1번째 ~ m * (t-1) + p 번째 까지
    123456
    for i in range(len(all)):
        if i % m == p-1:
            result.append(all[i])
    #print(all)
    result = list(map(str, result))
    #print(result)
    # 11진수 이상 변환
    n_dict = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    for i, v in enumerate(result):
        if v in n_dict:
            result[i] = n_dict[v]
    #print(result[:t])
    
    return "".join(result[:t])
    
    
    
    
        
            
    
    