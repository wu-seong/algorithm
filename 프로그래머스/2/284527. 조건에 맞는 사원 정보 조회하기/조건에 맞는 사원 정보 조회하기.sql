-- 코드를 작성해주세요
select best.SCORE, ep.emp_no, ep.emp_name, ep.position, ep.email  from HR_EMPLOYEES as ep
join (
select e.emp_no as best_emp_no, sum(score) as SCORE from HR_employees e
join hr_grade g
on e.emp_no = g.emp_no
where year = 2022
group by e.emp_no, g.year
order by sum(score) desc
limit 1) as best
on best.best_emp_no = ep.emp_no
