def solution(m, musicinfos):
    '''
    멜로디를 통해 곡을 찾음
    제목, 끝난 시각, 악보
    
    음악은 처음부터 재생, 1분에 한음씩
    재생 시간 > 음악 시간 --> 반복 재생
    재생 시간 < 음악 시간 --> 음악이 중간이 짤린다.
    '''
    
    '''
    반복시간에 따라서 멜로디를 늘리거나 자른다
    CDEFGABCDEFGAB
    C,D,F,G,A의 #을 -> c,d,f,g,a로 바꾸기 
    '''
    def transfer_min(time_str):
        hour = int(time_str[:2])
        minuet = int(time_str[3:])
        return hour*60 + minuet
    m_list = []
    def transfer_m(mel, d, target = False):
        mel = mel.replace('C#','c')
        mel = mel.replace('B#','b')
        mel = mel.replace('D#','d')
        mel = mel.replace('E#','e')
        mel = mel.replace('F#','f')
        mel = mel.replace('G#','g')
        mel = mel.replace('A#','a')
        n = len(mel)
        if target:
            return mel
        if d <= n:
            return mel[:d]
        quo = d // n
        remainder = d % n
        return mel*quo + mel[:remainder]
    m = transfer_m(m, len(m), True)
    for m_str in musicinfos:
        start, end, title, melody = m_str.split(",")
        start = transfer_min(start)
        end = transfer_min(end)
        duration = end - start + 1
        m_list.append( (start, end, title, transfer_m(melody, duration) ) ) 
    print(m_list, m)
    '''
    곡이 m을 포함하는지를 체크
    모두 포함하지 않으면 None
    포함하면 그곡 저장
    '''
    result = []
    for m_info in m_list:
        melody = m_info[3]
        if m in melody:
            result.append(m_info)
    if not result:
        return "(None)"
    print("조건을 만족하는 곡:", result, m)
    '''
    여러개면
    각 곡 마다 재생시간 긴 것 구하기
    재생시간 가장 긴 것이 여러개이면
    musicinfos에 입력된 순서가 빠른 것으로
    '''
    max_duration = -1
    max_result = []
    for i in range(len(result)):
        start, end, title, melody = result[i]
        duration = end - start
        if max_duration < duration:
            max_duration = duration
            max_result = [title]
        elif max_duration == duration:
            max_result.append(title)
    #print("정답", max_result)
    return max_result[0]
 