select e.date, 
round(sum(case e.type when 'completed' then 0 else 1 end)*1.0/count(e.type),3) as p    -- sum()和case()别弄混了, count()返回的是整数(个数) 
from email e
join user u1 on (e.send_id=u1.id and u1.is_blacklist=0)
join user u2 on (e.receive_id=u2.id and u2.is_blacklist=0)
group by e.date order by e.date;


-- SUM是对符合条件的记录的数值列求和
-- COUNT 是对查询中符合条件的结果(或记录)的个数
https://blog.csdn.net/AnneQiQi/article/details/51984937
