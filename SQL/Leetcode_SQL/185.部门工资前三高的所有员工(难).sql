### 解题思路:先对Employee表进行部门分组工资排名，再关联Department表查询部门名称，再使用WHERE筛选出排名小于等于3的数据（也就是每个部门排名前3的工资）。


select B.Name as Department, A.Name as Employee, A.Salary
from
(select DepartmentId, Name ,Salary,
dense_rank() over (partition by DepartmentId order by Salary desc) as ranking  # 这几个列名的先后顺序总是容易写错，多练习下
from Employee) as A
inner join Department as B
on A.DepartmentId = B.Id
where ranking <=3

#评论区高赞
https://leetcode-cn.com/problems/department-top-three-salaries/solution/bu-men-gong-zi-qian-san-gao-de-yuan-gong-by-leetco/
