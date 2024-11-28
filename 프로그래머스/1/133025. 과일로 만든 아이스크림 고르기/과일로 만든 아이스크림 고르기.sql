-- 코드를 입력하세요
SELECT first_half.FLAVOR from first_half
inner join icecream_info
on first_half.FLAVOR = icecream_info.FLAVOR
where icecream_info.INGREDIENT_TYPE = 'fruit_based'
group by first_half.FLAVOR
having sum(total_order) > 3000 
order by sum(total_order) desc