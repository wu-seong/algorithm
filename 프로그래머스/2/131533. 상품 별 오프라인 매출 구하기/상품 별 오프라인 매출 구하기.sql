-- 코드를 입력하세요
SELECT p.product_code pcode, sum(sales_amount * p.price) sales from product p
inner join offline_sale os
ON p.product_id = os.product_id
group by pcode
order by sales desc, pcode