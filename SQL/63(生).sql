select p1.id, p1.number, count(distinct p2.number) as rank
from passing_number as p1, passing_number as p2
where p1.number <= p2.number
group by p1.id
order by p1.number desc, p2.id


-- My Method 较优
select tt.number from
(select number, count(*) as `num`
from grade 
group by number) as tt
where tt.num >=3;

-- 对我的方法的进一步改进， 最优
select number from grade
group by number
having count(id) >= 3
