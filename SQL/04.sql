select e.last_name, e.first_name, de.dept_no
from employees as e
inner join dept_emp as de
on e.emp_no = de.emp_no;
