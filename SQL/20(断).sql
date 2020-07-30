select
(select salary
from salaries
where emp_no = '10001'
and to_date = '9999-01-01')
-
(select salary
from salaries
where emp_no = '10001'
order by from_date asc
limit 1)
