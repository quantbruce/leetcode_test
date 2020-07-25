select emp_no, count(salary) as t
from salaries 
group by emp_no
having t > 15;

