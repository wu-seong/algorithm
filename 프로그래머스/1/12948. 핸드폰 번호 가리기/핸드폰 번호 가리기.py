def solution(p_num):
    blind_nums = p_num[-4::1]
    return '*'*(len(p_num)-4)  + blind_nums