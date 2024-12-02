
select CI.item_id, CI.item_name, CI.rarity from ITEM_INFO CI
join ITEM_TREE IT
on CI.item_id = IT.item_id
join ITEM_INFO PI
on IT.parent_item_id = PI.item_id
where PI.rarity = 'RARE'
order by CI.item_id desc
    
