select e.date, 
round(sum(case e.type when 'completed' then 0 else 1 end)*1.0/count(e.type),3) as p    #sum()和case()别弄混了
from email e
join user u1 on (e.send_id=u1.id and u1.is_blacklist=0)
join user u2 on (e.receive_id=u2.id and u2.is_blacklist=0)
group by e.date order by e.date;
