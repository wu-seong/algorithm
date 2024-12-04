# 입양을 간 동물 리스트 중 보호소 리스트에 없는 동물들
# animal_outs 테이블에 있는 동물들 중 animal_ins 테이블에 없는 동물들을 구하기
# animal_outs를 구하고 not in 조건을 통해 필터링 하기
SELECT animal_id, name
from animal_outs
where animal_id not in (select animal_id from animal_ins)
order by animal_id
