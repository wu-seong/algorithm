def solution(s):
    # 문자열을 공백을 기준으로 나누어 숫자 배열로 저장
    l = list(map(int, s.split(" ")))
    # 숫자 배열에서 최솟값과 최댓값을 구한 뒤 숫자로 문자열로 저장 
    return str(min(l)) + " " + str(max(l))
    