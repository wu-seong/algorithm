-- 코드를 작성해주세요
select II.item_id, II.item_name from ITEM_INFO II
inner join ITEM_TREE IT
on II.ITEM_ID = IT.ITEM_ID
where IT.parent_item_id is null
order by item_id