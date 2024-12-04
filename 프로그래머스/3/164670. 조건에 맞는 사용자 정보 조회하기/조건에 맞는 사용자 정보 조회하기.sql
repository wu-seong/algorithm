# user id별로 묶은다음 having을 통해 count >= 3 인 user_id만 남기기
# 그다음 해당 유저 아이디를 통해 조인해서 유저 정보 얻기
with active_user as(
select writer_id
from USED_GOODS_BOARD
group by writer_id
having count(*) >= 3
)
SELECT usr.user_id USER_ID, usr.nickname NICKNAME,
concat(usr.city, ' ', usr.STREET_ADDRESS1, ' ', usr.STREET_ADDRESS2) 전체주소,
concat(substring(usr.tlno,1,3), '-'
       ,substring(usr.tlno,4,4), '-'
       ,substring(usr.tlno,8,4)) 전화번호
from USED_GOODS_USER usr
join active_user
on active_user.writer_id = usr.user_id
order by usr.user_id desc