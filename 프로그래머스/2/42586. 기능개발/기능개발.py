from collections import deque
def solution(progresses, speeds):
    # 각 배포 마다 몇 개의 기능이 완성되는지
    # 각 일 마다 작업의 진도율을 판단하기 100*100
    # 각 일마다 progresses + speeds를 더하여 100넘으면 complete상태
    # 순서대로 순회하며 앞의 기능이 100 넘으면 pop하기
    # 그대로 이어가서 complete에 해당 인덱스가 있으면 pop
    # complete에 없을 때 까지 pop
    # 그 일 마다 pop한 개수 카운팅 하여 저장
    # empty되면 끝
    result = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        cnt = 0
        for i in range(len(progresses)): # 진도율 계산
            progresses[i] += speeds[i]
        for i in range(len(progresses)): # 시뮬
            if progresses[i] >= 100:
                cnt += 1
            else:
                break
        for i in range(cnt):
            progresses.popleft()
            speeds.popleft()
        if cnt > 0:
            result.append(cnt)
        #print(result)
    return result