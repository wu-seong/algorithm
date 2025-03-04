'''
1 = 5/5 -> 2번 

5의 배수 = 5 + 5 +... 배수 N번

5의 제곱수 = 제곱 n번

5로 이루어진 수 = (1+10+100...)*5


먼저 더하기로만 고려해서 모든 수를 구하기 -> 수의 8배수까지 1~8
5 10 15 20 25 30 35 40 

곱하기도 고려해서 수를 구하기 -> 수의 8제곱수까지 1~8
5 25 125 625 3125 15625 83125 4015625 

수로만 이루어진 수를 구하기 -> 8자리까지 구하기 1~8
5 55 555 5555 55555 555555 5555555 55555555

1일 때 구하기 -> 5
2일 때 구하기 -> 5/5, 5+5, 5*5, 5(1+10)
3일 때 구하기 -> 1+5, 10+5, 25+5, 55+5 
              1-5, 10-5, 25-5, 55-5 
              5-1, 5-10, 5-25, 5-55
              1*5 10*5 25*5 5*5(1+10)
              1/5
겹치는 것 확인하기
음수인지 확인하기(뺄셈은 둘다 해보고 음수가 아닌것만)
나눗셈은 몫연산으로

'''

def solution(N, number):
    def make_num(level, set1, set2):
        temp_set = set()
        for s1 in set1:
            for s2 in set2:
                temp = s1 + s2
                if not temp in num_sets[level-1]:
                    temp_set.add(temp)
                temp = s1 * s2
                if not temp in num_sets[level-1]:
                    temp_set.add(temp)
                temp = abs(s1 - s2)
                if temp and not temp in num_sets[level-1]:
                    temp_set.add(temp)
                temp = s1 // s2 | s2 // s1
                if not temp in num_sets[level-1]:
                    temp_set.add(temp)
        same = int(str(N)*level)
        temp_set.add(same)
        return temp_set

            
    dp = [-1 for _ in range(32001)]
    num_sets = [set() for _ in range(9)]
    num_sets[1].add(N)
    
    # 1 -> x
    # 2 -> 11
    # 3 -> 12
    # 4 -> 13 22
    # ...
    # 8 -> 17 26 35 44
    #make_num(2, set([5]), set([5]))
    for i in range(2,9): 
        temp_set = set()
        for j in range(1,(i//2)+1):
            #print(i, 'ij:',j, i-j)
            temp_set.update(make_num(i, num_sets[j], num_sets[i-j]))
        #print(temp_set)
        num_sets[i] = temp_set
    for i in range(1,9):
        #print(i, num_sets[i])
        if number in num_sets[i]:
            return i
    return -1
  