select second_login.date, round(ifnull(second_login.second_login_num *1.0/ first_login.first_num,0),3)
from (select login.date,ifnull(n1.new_num,0) as second_login_num
from login 
left join 
(select l1.date,count(distinct l1.user_id) as new_num
from login l1
join login l2 on l1.user_id=l2.user_id and l2.date=date((l1.date),'+1 day') 
where l1.date =
(select min(date) from login where user_id=l1.user_id)
group by l1.date) n1
on login.date = n1.date
group by login.date) second_login
 
join 
 
(select login.date,ifnull(n1.new_num,0) as first_num
from login 
left join 
(select l1.date,count(distinct l1.user_id) as new_num
from login l1
where l1.date =
(select min(date) from login where user_id=l1.user_id)
group by l1.date) n1
on login.date = n1.date
group by login.date) first_login
 
on second_login.date=first_login.date
