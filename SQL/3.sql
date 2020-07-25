select dm.emp_no, s.salary, s.from_date, s.to_date, dm.dept_no
from salaries as s
inner join dept_manager as dm
on dm.emp_no = s.emp_no
where dm.to_date = '9999-01-01' and s.to_date = '9999-01-01'
order by s.emp_no asc
