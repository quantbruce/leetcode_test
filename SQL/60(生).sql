select s1.emp_no, s1.salary, 
(select sum(s2.salary) from salaries as s2
where s1.emp_no >= s2.emp_no and s2.to_date='9999-01-01') as running_total
from salaries as s1 where s1.to_date = '9999-01-01' 


-- 也可以用窗口函数写，感觉更加简洁一些
select emp_no, salary,
sum(salary) over (order by emp_no asc) as 'running_total'
from salaries where to_date = '9999-01-01'


