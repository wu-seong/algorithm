# 업그레이드 할 수 없다 -> 본인을 부모로 가지는 레코드가 1개도 없다.
# 부모를 조인시켜서 존재하는 부모 item_id 구하기
# 해당 id에 포함이 되지 않는 것들을 고르기

with parent_item as(
select distinct it.parent_item_id
from ITEM_INFO ii
join ITEM_TREE it
on ii.item_id = it.item_id
group by it.parent_item_id
)

#select parent_item_id from parent_item
select ii.item_id ITEM_ID, ii.item_name ITEM_NAME, ii.rarity RARITY
from ITEM_INFO ii
where ii.item_id not in (select parent_item_id from parent_item where parent_item_id is not null)
order by ii.item_id desc