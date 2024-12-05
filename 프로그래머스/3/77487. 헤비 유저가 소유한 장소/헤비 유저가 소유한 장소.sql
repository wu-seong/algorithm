# id별로 묶어서 count가 2인 host_id만 추출
# places중 host_id안에 속한 것들만 가져오기
with heavy_user as(
select host_id
from places
group by host_id
having count(*) >= 2)

select places.ID, places.NAME, places.HOST_ID
from places
join heavy_user
on heavy_user.host_id = places.host_id

