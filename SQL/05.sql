select e.last_name, e.first_name, de.dept_no
from employees as e
left join dept_emp as de
on e.emp_no = de.emp_no
