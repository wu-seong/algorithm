def to_binary(num_str):
    num = int(num_str)
    result = ""
    while num != 1:
        result = str(num % 2) + result
        num = num//2
    result = str(num) + result
    return result
def solution(s):
    cnt_zero = 0
    cnt_transform = 0
    result = s
    # 0 카운팅 및 제거
    # 길이 저장 및 이진수 변환
    # "1"이 될 때 까지 반복
    while result != "1":
        cnt_zero += result.count("0")
        result = result.replace("0","")
        #print(result)
        result = to_binary(len(result))
        cnt_transform += 1
    return ([cnt_transform, cnt_zero])