select max(date) as d
from login
group by user_id
order by user_id
