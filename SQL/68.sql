select u.name u_n, c.name c_n, max(l.date)
from login l
join user u on l.user_id = u.id
join client c on l.client_id = c.id
group by l.user_id
order by u.name
