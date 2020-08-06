CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  declare p INT; # declare关键字？？？？, 总是忘记加封号
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
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
      SET N:=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT 
            Salary
      FROM 
            Employee
      GROUP BY 
            Salary
      ORDER BY 
            Salary DESC
      LIMIT N, 1
  );
https://leetcode-cn.com/problems/nth-highest-salary/solution/mysql-zi-ding-yi-bian-liang-by-luanz/
