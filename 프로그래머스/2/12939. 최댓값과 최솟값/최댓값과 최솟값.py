def solution(s):
    # 문자열은 각각 숫자로 바꾸어 리스트로 저장하기
    num_list = list(map(int, s.split(" ")))
    # 최댓값 최솟값 찾기
    max_num = max(num_list)
    min_num = min(num_list)
    # 최댓값 최솟값 문자열로 담기
    return " ".join(map(str,[min_num, max_num]))