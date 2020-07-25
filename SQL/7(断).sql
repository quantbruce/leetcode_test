select emp_no, count(salary) as t
from salaries 
group by emp_no
having t > 15; # 或者写成 having count(salary) > 15 也是可以AC

