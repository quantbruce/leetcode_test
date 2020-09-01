select s1.emp_no, s1.salary, count(distinct s2.salary) as rank
from salaries s1, salaries s2
where s1.to_date = '9999-01-01' and s2.to_date = '9999-01-01'
and s1.salary <= s2.salary
group by s1.emp_no
order by s1.salary desc


-- 写成窗口函数，简单明了的多
select emp_no, salary,
dense_rank() over (order by salary desc) as `rank`
from salaries 
where to_date = '9999-01-01' -- 这里写了order by emp_no 反而会报错

-- 窗口函数也可以另写成这样
 select emp_no,salary,
dense_rank() over w as 'rank'
from salaries
where to_date='9999-01-01'
WINDOW w as (order by salary desc)

