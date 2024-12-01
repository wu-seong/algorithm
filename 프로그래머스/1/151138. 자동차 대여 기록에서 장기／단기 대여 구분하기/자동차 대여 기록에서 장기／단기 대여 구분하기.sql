-- 코드를 입력하세요
SELECT history_id, car_id, date_format(start_date, '%Y-%m-%d'), date_format(end_date, '%Y-%m-%d'), if(DATEDIFF(end_date, start_date) + 1 >= 30, '장기 대여', '단기 대여') RENT_TYPE 
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where start_date between '2022-09-01' and '2022-09-30'
order by history_id desc