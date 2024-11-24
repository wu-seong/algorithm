-- 코드를 입력하세요
SELECT max(price) into @max_price from food_product;
select * from food_product
where price = @max_price
