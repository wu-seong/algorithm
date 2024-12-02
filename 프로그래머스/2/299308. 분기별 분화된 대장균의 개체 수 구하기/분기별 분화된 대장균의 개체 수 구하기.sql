select concat((floor((month(DIFFERENTIATION_DATE) -1 )/ 3)) + 1, 'Q') QUARTER, count(*) ECOLI_COUNT from ECOLI_DATA
group by concat((floor((month(DIFFERENTIATION_DATE) -1) / 3)) + 1, 'Q')
order by QUARTER