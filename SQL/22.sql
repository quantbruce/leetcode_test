select dp.dept_no, dp.dept_name, count(*) as sum
from departments as dp
inner join dept_emp as de
on dp.dept_no = de.dept_no
inner join salaries as s
on de.emp_no = s.emp_no
group by dp.dept_no
