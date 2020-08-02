# Write your MySQL query statement below
select max(Salary) as SecondHighestSalary  #易错点，需要考虑到表格只有一行的情形
from Employee
where Salary not in (
    select max(Salary) from Employee)
