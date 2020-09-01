select p1.id, p1.number, count(distinct p2.number) as rank
from passing_number as p1, passing_number as p2
where p1.number <= p2.number
group by p1.id
order by p1.number desc, p2.id


-- 窗口函数更酷！
select id, number,
dense_rank() over (order by number desc) as `rank`
from passing_number 
order by number  desc, id asc;
