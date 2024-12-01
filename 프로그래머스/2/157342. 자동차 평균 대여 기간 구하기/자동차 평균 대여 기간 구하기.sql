-- 코드를 입력하세요
SELECT 
    car_id, 
    ROUND(AVG(DATEDIFF(end_date, start_date) + 1), 1) AS AVERAGE_DURATION
FROM 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY 
    car_id
HAVING 
    ROUND(AVG(DATEDIFF(end_date, start_date) + 1), 1) >= 7
ORDER BY 
    AVERAGE_DURATION DESC, 
    car_id DESC;