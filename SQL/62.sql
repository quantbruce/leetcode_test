select number from
(select number, count(*) as num
from grade
group by number)
where num >= 3;


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
