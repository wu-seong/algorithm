# 기간안에 대여횟수가 5회 이상인 자동차들 구하기
# car_id 기준으로 기간안의 대여 기록만 필터링해서 count5회 이상인 car_id 구하기
# 주어진 기간안에 car_id와 주어진 달 기준으로 묶어서 count하기
with popular_cars as(
select car_id
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where start_date between '2022-08-01' and '2022-10-31'
group by car_id
having count(*) >= 5
)
select month(start_date) MONTH, car_id, count(*)
from CAR_RENTAL_COMPANY_RENTAL_HISTORY rh
where rh.car_id in (select car_id from popular_cars)
and start_date between '2022-08-01' and '2022-10-31'
group by car_id, month(start_date)
having count(*) > 0
order by MONTH, car_id desc 
