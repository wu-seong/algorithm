
select name, datetime
from ANIMAL_INS
where animal_id not in (select animal_id from animal_outs)
order by datetime
limit 3