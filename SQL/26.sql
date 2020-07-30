select t1.emp_no as emp_no, t2.emp_no as manager_no,
       t1.salary as emp_salary, t2.salary as manager_salary
from
(select de.emp_no, s.salary, de.dept_no
from dept_emp as de
inner join salaries as s
on de.emp_no = s.emp_no
where s.to_date = '9999-01-01') as t1
inner join 
(select dm.emp_no, s.salary, dm.dept_no
from dept_manager as dm
inner join salaries as s
on dm.emp_no = s.emp_no
where s.to_date = '9999-01-01') as t2
on t1.dept_no = t2.dept_no
where t1.salary > t2.salary
