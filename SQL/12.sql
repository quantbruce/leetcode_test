select de.dept_no, de.emp_no, max(s.salary)
from dept_emp as de
inner join salaries as s
on de.emp_no = s.emp_no
where de.to_date = '9999-01-01' and s.to_date = '9999-01-01'
group by de.dept_no
