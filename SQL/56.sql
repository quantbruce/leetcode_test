select e.emp_no, de.dept_no, eb.btype, eb.received
from employees as e
inner join dept_emp as de
on e.emp_no = de.emp_no
left join emp_bonus as eb
on eb.emp_no = e.emp_no
