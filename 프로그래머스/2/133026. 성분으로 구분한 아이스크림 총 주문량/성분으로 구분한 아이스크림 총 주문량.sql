-- 코드를 입력하세요
SELECT ii.ingredient_type, sum(fh.total_order) as TOTAL_ORDER from first_half as fh
inner join icecream_info as ii
on fh.flavor = ii.flavor
group by ii.ingredient_type
order by TOTAL_ORDER;

