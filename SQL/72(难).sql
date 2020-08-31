select user.name u_n, client.name c_n, login.date, p1.ps_num
from login
join (
select user_id, date, sum(number) over (partition by user_id order by date) ps_num
from passing_number) p1
on login.user_id = p1.user_id and login.date = p1.date
join user on login.user_id = user.id
join client on login.client_id = client.id
order by login.date, user.name
