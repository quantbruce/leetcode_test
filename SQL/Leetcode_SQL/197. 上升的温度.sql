########坑点
要注意的坑爹事情是 Mysql 和 SQL Serve之间 datediff函数有微小却严重的区别 Mysql的是datediff(被减数, 减数) 
SQL Serve的datediff(时间单位, 减数, 被减数) 这两个不仅MySQL没有时间单位，而且做差的减数被减数位置相反 之前做的时候没注意，
用datediff(day, x1, x2)做了半天.. 不仅day不该加，删掉之后还发现筛选结果为空..

###理解题意：相当于查询今天温度比昨天有升高的所有满足该条件的今天温度的Id

######错误写法
select Id
from Weather
where Temperature > (
    select Temperature from Weather
    where RecordDate
)


select w2.Id
from Weather w1, Weather w2
where datediff(w2.RecordDate, w1.RecordDate) = 1
and w2.Temperature > w1.Temperature

###评论区高赞
https://leetcode-cn.com/problems/rising-temperature/solution/shang-sheng-de-wen-du-by-leetcode/
