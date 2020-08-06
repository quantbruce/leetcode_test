###### 错误写法
select d.Name as Department, e.Name as Employee, max(e.Salary) as Salary # 这样写会导致有多人最高工资时，只出现一个人的名字。是不合题意的
from Employee as e                                                       # 不要一开始去锁定最高工资的人名字，而是要锁定最高工资，因为最高工资是唯一的
inner join Department as d
on e.DepartmentId = d.Id
group by e.DepartmentId


######方法1 官方解答
select d.Name as Department, e.Name as Employee, E.Salary
from Employee as e
inner join Department as d # 跟这个d表联立只是为了获得部门名
on e.DepartmentId = d.Id
where (e.DepartmentId, e.Salary) in  # （A, B） in 这种写法是亮点 
(
select DepartmentId, max(Salary)
from Employee
group by DepartmentId
)

https://leetcode-cn.com/problems/department-highest-salary/solution/bu-men-gong-zi-zui-gao-de-yuan-gong-by-leetcode/

