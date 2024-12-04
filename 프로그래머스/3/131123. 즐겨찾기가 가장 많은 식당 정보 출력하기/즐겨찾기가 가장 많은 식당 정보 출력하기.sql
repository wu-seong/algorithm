with max_per_food_type as (SELECT food_type, max(favorites) as max_favorites from rest_info
group by food_type
)
select ri.food_type, ri.rest_id, ri.rest_name, ri.favorites 
from REST_INFO ri
join max_per_food_type
on max_per_food_type.food_type = ri.food_type and
max_per_food_type.max_favorites = ri.favorites
order by ri.food_type desc
