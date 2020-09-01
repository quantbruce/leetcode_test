select s2.emp_no, s2.from_date, (s2.salary-s1.salary) as salary_growth
from salaries s1, salaries s2
where salary_growth > 5000
and s1.emp_no = s2.emp_no
and (strftime('%Y', s2.to_date)-strftime('%Y', s1.to_date)=1 or  # 详解见笔记
    strftime('%Y', s2.from_date)-strftime('%Y', s1.from_date)=1)
order by salary_growth desc
