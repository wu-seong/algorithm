SELECT distinct cr.car_id CAR_ID from CAR_RENTAL_COMPANY_CAR cr
join CAR_RENTAL_COMPANY_RENTAL_HISTORY rh
on cr.car_id = rh.car_id
where month(rh.start_date) = '10' and cr.car_type = '세단'
order by CAR_ID desc



