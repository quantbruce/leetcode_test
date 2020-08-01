select * from employees as e
where e.emp_no in (
    select ev.emp_no from emp_v as ev
    where ev.emp_no = e.emp_no)
