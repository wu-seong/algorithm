# 물고기 타입별로 평균 구해서 33이상인 것만 구하기
# 구한 물고기 종류만 필터링 해서 물고기 종류별 수, 최대 길이, 물고기 출력
# 10cm이하는 (null은) 10으로 취급하기

with big_fish_type as(
select fish_type
from FISH_INFO
group by fish_type
having avg(ifnull(length, 10)) >= 33
)

select count(*) FISH_COUNT, max(ifnull(length, 10)) MAX_LENGTH, FISH_TYPE
from fish_info
where fish_type in (select big_fish_type.fish_type from big_fish_type)
group by FISH_TYPE
order by fish_type