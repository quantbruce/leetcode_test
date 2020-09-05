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

-- 更具有拓展性的框架
select e.emp_no, s.salary, e.last_name, e.first_name
from employees e join salaries s
on e.emp_no = s.emp_no
and s.to_date = '9999-01-01'
and s.salary = (
    select s1.salary
    from salaries s1 join salaries s2
    on s1.salary <= s2.salary
    and s1.to_date = '9999-01-01' and s2.to_date = '9999-01-01'
    group by s1.salary
    having count(distinct s2.salary) = 2 # 这里等于几，排名就写前几的
);
