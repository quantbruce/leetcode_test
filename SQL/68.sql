select u.name u_n, c.name c_n, max(l.date)
from login l
join user u on l.user_id = u.id
join client c on l.client_id = c.id
group by l.user_id
order by u.name

-- 【心得】
-- 分组之后，再取一条记录(最大或最小)， 此时选择group by + max or min
-- 分组之后，再去前几条，或后几条记录时，有限考虑窗口函数！


