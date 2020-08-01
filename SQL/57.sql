select e.* from employees as e where not exists
(select emp_no from dept_emp as de where e.emp_no=de.emp_no)


