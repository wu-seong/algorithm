-- 코드를 입력하세요
SELECT MCDP_CD as '진료과코드', count(apnt_ymd) as '5월예약건수' from appointment
where date_format(apnt_ymd, '%m') = 5
group by MCDP_CD
order by count(apnt_ymd), MCDP_CD