###方法1
select * from emp_v
intersect
select * from employees

###方法2
select e.* from employees as e, emp_v as ev
where e.emp_no = ev.emp_no
