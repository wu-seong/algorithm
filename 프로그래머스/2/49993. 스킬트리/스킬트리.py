def solution(skill, skill_trees):
    # 각 스킬의 인덱스를 저장
    # 스킬트리를 순회하면서
    # skill의 교집합만 남기기 ->BC CBD CB BD
    # 순서만 지켜지면 ok
    n = len(skill_trees)
    new_skill_trees = [] * n
    for skill_tree in skill_trees:
        temp = []
        for s in skill_tree:
            if s in skill:
                temp.append(s)
        new_skill_trees.append(temp)
    #print(new_skill_trees)
    # 새로운 스킬트리 순회하면서
    # skill의 순서에 맞는지 확인
    cnt = 0
    for skill_tree in new_skill_trees:
        for i in range(len(skill_tree)):
            if skill_tree[i] != skill[i]: # 하나라도 다르면 불가능
                can = False
                break
        else:
            cnt += 1
    #print(cnt)
    return cnt