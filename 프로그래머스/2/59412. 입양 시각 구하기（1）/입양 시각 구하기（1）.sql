-- 코드를 입력하세요
SELECT hour(datetime) as hour, count(*) from animal_outs
where hour(datetime) < 20 and hour(datetime) >= 9
group by hour(datetime)
order by hour(datetime)