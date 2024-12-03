with out_animal as(
    select animal_id 
    from animal_outs
)
select name, datetime
from ANIMAL_INS
where animal_id not in (select animal_id from out_animal)
order by datetime
limit 3

