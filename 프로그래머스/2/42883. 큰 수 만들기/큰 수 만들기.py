def solution(number, k):
    # 완탐도 가능하긴할듯?
    # 뒤에 숫자가 앞보다 크면 앞 숫자를 지운다.
    # -> 현재 숫자가 앞의 숫자보다 크면 앞의 숫자들을 연속해서 지운다.
    # -> 내림차순으로 진행이 될 경우 stack에 계속 넣는다
    # -> 그러면서 stack의 마지막 값을 비교하면서 더 작으면 지운다.
    # k가 다 소진되거나 모든 수를 탐색하면 그만둔다.
    number = list(number)
    stack = []
    for digit in number:
        while k > 0 and stack and digit > stack[-1]: # 앞에 더 작은 수가 있다면 다 꺼내기
            k -= 1
            stack.pop()
        stack.append(digit) # 현재 수 넣기        
    # 남은건 뒤에서 부터 자르기
    if k > 0: 
        stack = stack[:-k]
        return "".join(stack)
    return "".join(stack)
# 배열 중간에 삭제해야 하는 경우 스택을 이용하면 더 간단해짐
# 삭제하기 이전까지 스택에 저장하고 삭제할 것은 pop을 이용해서 삭제
# 연속된 삭제를 하기에 좋음