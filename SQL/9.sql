select dm.dept_no, dm.emp_no, s.salary
from dept_manager as dm
inner join salaries as s
on dm.emp_no = s.emp_no
where dm.to_date = '9999-01-01'
and s.to_date = '9999-01-01'
