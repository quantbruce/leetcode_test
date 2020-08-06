select B.Name as Department, A.Name as Employee, A.Salary
from
(select DepartmentId, Name ,Salary,
dense_rank() over (partition by DepartmentId order by Salary desc) as ranking
from Employee) as A
inner join Department as B
on A.DepartmentId = B.Id
where ranking <=3

#评论区高赞
https://leetcode-cn.com/problems/department-top-three-salaries/solution/bu-men-gong-zi-qian-san-gao-de-yuan-gong-by-leetco/
