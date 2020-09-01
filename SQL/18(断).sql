select e.emp_no, max(s.salary), e.last_name, e.first_name
from employees as e
inner join salaries as s
on e.emp_no = s.emp_no
where s.to_date = '9999-01-01'
and s.salary not in (
      select max(salary) from salaries)

-- 这样写也是对的
select s.emp_no, max(s.salary), e.last_name, e.first_name
from salaries s
join employees e
on s.emp_no = e.emp_no
where s.to_date = '9999-01-01'
and s.salary <>
(select max(salary)
from salaries 
where to_date = '9999-01-01')

