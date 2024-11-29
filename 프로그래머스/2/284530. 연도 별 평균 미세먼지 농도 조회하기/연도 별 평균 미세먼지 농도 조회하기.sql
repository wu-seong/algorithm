-- 코드를 작성해주세요
select year(YM) as YEAR, round(avg(PM_val1), 2) as 'PM10', round(avg(PM_Val2), 2) as 'PM2.5' from AIR_POLLUTION
where location2 = '수원'
group by year(YM)
order by year(YM)