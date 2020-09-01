-- 错误写法
update salaries set salary=salary*1.1 where emp_no in 
(select s.emp_no from salaries s inner join emp_bonus eb
 on s.emp_no = eb.emp_no and s.to_date = '9999-01-01');
 
 
-- 正确写法
update salaries set salary = salary * 1.1
where emp_no in (select emp_no from emp_bonus)
and to_date = '9999-01-01'
