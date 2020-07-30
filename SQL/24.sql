select de.dept_no, de.emp_no, s.salary
from dept_emp as de
inner join salaries as s
on s.emp_no = de.emp_no
where de.emp_no not in (
    select emp_no from dept_manager)
and s.to_date = '9999-01-01'
