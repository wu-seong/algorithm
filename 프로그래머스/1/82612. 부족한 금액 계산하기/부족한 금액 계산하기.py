def solution(price, money, count):
    # 놀이기구의 총 금액을 계산( n(n+1)/2 * 가격)
    total_price = price * ( (count*(count+1))/2 )
    return 0 if money >= total_price else total_price - money