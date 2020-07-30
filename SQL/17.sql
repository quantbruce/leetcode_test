select emp_no, max(salary)
from salaries
where emp_no not in (
    select emp_no 
    from salaries
    order by salary desc
    limit 1)

