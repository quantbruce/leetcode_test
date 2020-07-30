select e.last_name, e.first_name, dp.dept_name
from employees as e
left join dept_emp as de
on e.emp_no = de.emp_no
left join departments as dp  # left写错成inner
on de.dept_no = dp.dept_no
