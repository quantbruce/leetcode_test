select e.emp_no, e.first_name, e.last_name, b.btype, s.salary,
(case b.btype
when 1 then s.salary*0.1
when 2 then s.salary*0.2
else s.salary*0.3 end) as bonus
from employees e inner join emp_bonus as b on e.emp_no = b.emp_no
inner join salaries s on e.emp_no = s.emp_no and s.to_date='9999-01-01'
