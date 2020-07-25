select distinct(salary)
from salaries
where to_date = '9999-01-01'
order by salary desc
