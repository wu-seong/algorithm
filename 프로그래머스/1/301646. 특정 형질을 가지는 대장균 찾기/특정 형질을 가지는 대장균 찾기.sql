#이진수로 나타냈을 때 비트마스킹 하는법?

-- 코드를 작성해주세요

select count(*) COUNT
from ecoli_data
where (Genotype & 2 = 0) and (Genotype & 5 > 0)