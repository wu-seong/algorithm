-- 코드를 입력하세요
SELECT member_id, member_name, gender, date_format(date_of_birth,'%Y-%m-%d') from MEMBER_PROFILE 
where month(date_of_birth) = '03' and gender = 'W' and TLNO is not null
order by member_id