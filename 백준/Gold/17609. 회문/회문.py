'''
회문 판별


투 포인터로 해서
처음과 끝부터 비교
같으면 둘다 1씩 이동, 시작 인덱스 < 끝 인덱스 

최초에 만약 두개가 다르면 둘 중 하나 이동 후에 이동하지 않은 것과 같은지 판단
둘 중 하나라도 같은 것이 있으면 그대로 진행

유사 회문 check

인덱스가 1차이 날 때는

두 개가 다른지만 판단 처음 1회면 유사 회문임 ex. abta -> aba

abtcdcbta
abb
abta
한번 더 이런 것이 있으면 둘 다 아님 -> 2

abbab

abca
aabbcc
'''
import sys
input = sys.stdin.readline

T = int(input().rstrip())


for _ in range(T):
    string = input().rstrip()
    s_p,e_p = 0,len(string) - 1

    result = 0
    while s_p < e_p:
        if string[s_p] == string[e_p]:
            s_p += 1
            e_p -= 1
        else:
            if e_p - s_p == 1: # 짝수 마지막거 비교할 때는 서로 다른지만 비교, 다르면 유사회문
                s_p += 1
                e_p -= 1
                result = 1
            else:
                
                # 왼쪽 거 삭제 후 회문 비교
                temp = string[:s_p] + string[s_p+1:]
                #print(temp)
                if temp == temp[::-1]:
                    result = 1
                    break
                
                temp = string[:e_p] + string[e_p+1:]
                #print(temp)
                if temp == temp[::-1]:
                    result = 1
                    break
                result = 2
                break
    print(result)
