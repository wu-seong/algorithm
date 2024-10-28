def solution(files):
    # head 모두 소문자로 바꾸기
    
    # head 기준 사전순 정렬
    # head가 같으면 number의 값으로 구분
    # 둘 다 같으면 순서 그대로
    
    new_files = []
    for file in files:
        print(file)
        for i,ch in enumerate(file):
            if ch.isdigit():
                head = file[:i]
                num_start = i
                break
        for i, ch in enumerate(file[num_start:]):
            if not ch.isdigit(): # 뒤에 숫자가 아닌게 나온 경우의 tail
                number = file[num_start:num_start+i]
                tail = file[num_start+i:]
                break
        else: # 뒤에 숫자만 있거나 아무것도 없는 경우
            number = file[num_start:]
            tail = ""
        new_files.append( (head, number, tail) )
    print(new_files)
    new_files.sort(key=lambda x: (x[0].lower(), int(x[1]) ) ) 
    result = [ h + n + t for h,n,t in new_files]
    print(result)
    return result
        
            
    