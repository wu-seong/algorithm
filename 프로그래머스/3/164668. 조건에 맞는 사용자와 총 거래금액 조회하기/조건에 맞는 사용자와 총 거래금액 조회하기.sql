# 거래 내역에서 사람 기준으로 총 금액을 구하기 (완료된 상태의)
# 거래내역과 사람의 정보는 분리되어 있으니 조인
SELECT u.user_id, u.nickname, sum(price) TOTAL_SALES
from used_goods_user u
join USED_GOODS_BOARD b
on u.user_id = b.writer_id
where b.status = 'DONE'
group by u.user_id
having sum(price) >= 700000
order by TOTAL_SALES
