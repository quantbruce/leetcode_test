select s1.emp_no, s1.salary, count(distinct s2.salary) as rank
from salaries s1, salaries s2
where s1.to_date = '9999-01-01' and s2.to_date = '9999-01-01'
and s1.salary <= s2.salary
group by s1.emp_no
order by s1.salary desc
