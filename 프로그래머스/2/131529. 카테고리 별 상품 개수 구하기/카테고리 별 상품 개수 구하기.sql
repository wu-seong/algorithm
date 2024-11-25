SELECT substring(product_code, 1, 2), count(substring(product_code, 1, 2)) from product
group by substring(product_code, 1, 2) 
order by substring(product_code, 1, 2) 

