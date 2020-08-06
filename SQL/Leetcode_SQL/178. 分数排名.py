#####方法1
#为什么牛客的方法报错？？？
select count(distinct s2.Score) as `Rank`
from Scores as s1, Scores as s2
where s1.Id = s2.Id
and s1.Score <= s2.Score
group by s1.Id
order by s1.Score desc, s2.Id asc;


####方法2  窗口函数法
# Write your MySQL query statement below
select Score,
    dense_rank() over (order by Score desc) as `Rank`
from Scores
