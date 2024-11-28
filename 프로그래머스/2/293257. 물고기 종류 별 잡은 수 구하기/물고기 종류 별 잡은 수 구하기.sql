-- 코드를 작성해주세요
select count(*) as fish_count, FISH_NAME_INFO.fish_name from fish_info
join FISH_NAME_INFO
on fish_info.fish_type = FISH_NAME_INFO.fish_type
group by FISH_NAME_INFO.fish_name
order by fish_count desc