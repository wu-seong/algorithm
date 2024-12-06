# parentID 기준으로 카운팅하기, 여기에 ID가 있는 것들은 그대로 하고 아니면 0
with have_child as(
select parent_ID ID, count(*) CHILD_COUNT
from ECOLI_DATA
group by parent_ID
having parent_ID is not null
order by ID
)

select ed.id, ifnull(have_child.CHILD_COUNT, 0) CHILD_COUNT
from ECOLI_DATA ed
left join have_child
on ed.id = have_child.ID

# -> 다른 테이블에서 필터링을 거친 id를 left join을 통해 병합할 수 있다