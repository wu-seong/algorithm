def solution(phone_book):
    dic = dict()
    
    phone_book.sort(key=lambda x : len(x))
    #print(phone_book)
    for p_num in phone_book: # 전화번호부 순회
        for i in range(len(p_num)): # 전화번호 순회 
            pre = p_num[:i+1:] # 접두어 만들기
            # print(pre)
            if pre in dic: # 이미 있는 접두어면 False
                return False
            if i == len(p_num)-1:
                dic[pre] = True # 없는 접두어면 저장
                #print(dic)
    answer = True
    return answer