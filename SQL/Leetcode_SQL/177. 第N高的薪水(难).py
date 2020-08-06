CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  declare p INT; # declare关键字？？？？
  set p = N - 1;
  RETURN (
      # Write your MySQL query statement below.
        select 
        (select distinct Salary 
        from Employee
        order by Salary desc
        limit p,1)
  );
END

https://leetcode-cn.com/problems/nth-highest-salary/solution/177-di-ngao-de-xin-shui-by-little_bird/


#最优解答
https://leetcode-cn.com/problems/nth-highest-salary/solution/mysql-zi-ding-yi-bian-liang-by-luanz/
