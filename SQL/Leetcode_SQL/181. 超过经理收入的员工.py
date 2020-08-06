##########方法1 My Methods
# 考察了表内自连接

select e2.Name as Employee
from Employee as e1, Employee as e2
where e1.Id = e2.ManagerId
and e2.Salary > e1.Salary




