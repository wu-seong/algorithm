from math import gcd
def solution(w,h):
    '''
    기울기가 3/2
    
    최대 공약수만큼 반복됨
    최대공약수로 나눈 몫 - 1
    '''
    gcd_value = gcd(w,h)
    return w*h - ((w//gcd_value + h//gcd_value - 1) * gcd_value)
    
    