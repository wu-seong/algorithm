WITH borrowing AS (
    SELECT car_id,
           IF(start_date <= '2022-10-16' AND end_date >= '2022-10-16',
              '대여중', '대여 가능') AS AVAILABILITY
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
)
SELECT car_id,
       MAX(AVAILABILITY) AS AVAILABILITY
FROM borrowing
GROUP BY car_id
ORDER BY car_id DESC;
