#####秒杀题，做一遍即可

select cinema.*
from cinema
where description <> 'boring'
and id &1 <> 0
order by rating desc
