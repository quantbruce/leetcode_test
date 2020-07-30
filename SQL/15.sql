select *
from employees 
where emp_no & 1 <> 0
and last_name <> 'Mary'
order by hire_date desc
