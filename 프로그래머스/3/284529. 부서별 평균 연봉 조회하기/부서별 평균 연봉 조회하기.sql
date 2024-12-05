# dept_id 별로 sal 합 구해서 dept_id기준으로 조인하기
with avg_sal_per_dept as(
select dept_id, round(avg(sal)) avg_sal
from HR_EMPLOYEES
group by dept_id
)

select dept.dept_id, dept_name_en, avg_sal_per_dept.avg_sal AVG_SAL
from HR_DEPARTMENT dept
join avg_sal_per_dept
on dept.dept_id = avg_sal_per_dept.dept_id
order by AVG_SAL desc
