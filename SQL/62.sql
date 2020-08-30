select number from
(select number, count(*) as num
from grade
group by number)
where num >= 3;
