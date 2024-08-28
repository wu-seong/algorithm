def solution(new_id):
    new_id = new_id.lower()
    for c in new_id:
        if c.isalpha() or c.isdigit() or c == '-' or c == '_' or c == '.':
            continue
        new_id = new_id.replace(c, '')
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    if  len(new_id) != 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) != 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    if new_id == '':
        new_id = new_id + 'a'
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    if len(new_id) <= 2:
        new_id = new_id + new_id[-1]
    if len(new_id) <= 2:
        new_id = new_id + new_id[-1]
    answer = new_id
    print(answer)
    return answer
