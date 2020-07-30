select dp.dept_no, dp.dept_name, t.title, count(t.title) as count
from departments as dp
inner join dept_emp as de
on dp.dept_no = de.dept_no
inner join titles as t
on de.emp_no = t.emp_no
where de.to_date = '9999-01-01' and t.to_date = '9999-01-01'
group by dp.dept_no, t.title # 第二个分组条件写错成dp.dept_name去了
