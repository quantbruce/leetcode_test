select e.emp_no
from employees as e
where e.emp_no not in (
    select emp_no from dept_manager
)
