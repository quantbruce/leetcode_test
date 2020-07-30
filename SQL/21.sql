select t1.emp_no, (t1.salary-t2.salary) as growth
from 
(select e.emp_no, s.salary
from employees as e
inner join salaries as s
on e.emp_no = s.emp_no
where s.to_date = '9999-01-01') as t1
inner join 
(select e.emp_no, s.salary
from employees as e
inner join salaries as s
on e.emp_no = s.emp_no
where s.from_date = e.hire_date) as t2
on t1.emp_no = t2.emp_no
order by growth asc
