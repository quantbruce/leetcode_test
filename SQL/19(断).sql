select e.last_name, e.first_name, dp.dept_name
from employees as e
left join dept_emp as de  # 有些员工没有部门编号dept_no, 有些有部门编号却又没有部门名。所以要用两个left join
on e.emp_no = de.emp_no
left join departments as dp  # left写错成inner
on de.dept_no = dp.dept_no



