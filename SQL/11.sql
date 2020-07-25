select de.emp_no, dm.emp_no as manager_no
from dept_emp as de
inner join dept_manager as dm
on de.dept_no = dm.dept_no
where dm.to_date = '9999-01-01'
and de.emp_no <> dm.emp_no
