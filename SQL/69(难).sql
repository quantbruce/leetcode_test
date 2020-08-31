select
round(count (user_id)*1.0/(select count(distinct user_id) from login),3) as p
from login
where (user_id, date)
in (select user_id, date(min(date), '+1 day') from login group by user_id);
