from collections import defaultdict
def solution(survey, choices):
    # 성격 유형 저장
    types = ['RT','CF','JM','AN']
    # 각 캐릭터 마다 점수 저장하는 배열 만들기
    score = defaultdict(int)
    # 각 질문지 마다 비동의[0]와 동의[1] 캐릭터를 가져오기
    for i in range(len(survey)):
        d_agree = survey[i][0]
        agree = survey[i][1]
        if choices[i] >= 4:
            score[agree] += (choices[i] - 4)
        else:
            score[d_agree] += (4 - choices[i])
    # 답변을 확인하며 각 캐릭터에 해당하는 점수를 더하기
    # 4개의 각 지표 중 더 큰것을 선택하여 문자열 만들기
    # 똑같으면 사전순 더 빠른 것
    answer = ''
    for t in types:
        if score[t[0]] >= score[t[1]]:
            answer = answer + t[0]
        else:
            answer = answer + t[1]
    #print(score)
    return answer