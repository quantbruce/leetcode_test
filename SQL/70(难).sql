select login.date, ifnull(n1.new_num,0) as new
from login
left join
(select l1.date, count(distinct l1.user_id) as new_num
from login l1
where l1.date =
(select min(date) from login where user_id=l1.user_id)
group by l1.date) as n1
on login.date = n1.date
group by login.date order by login.date
