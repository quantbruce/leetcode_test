
select Request_at as 'Day', round(avg(Status!='completed'),2) as 'Cancellation Rate'  # 体会avg()的妙用
from trips t inner join Users u1
on (t.Client_id = u1.Users_id and u1.Banned = 'No' )
inner join Users u2
on (t.Driver_Id = u2.Users_Id and u2.Banned = 'No')
where 
    Request_at between '2013-10-01' and '2013-10-03'
group by Request_at


# https://leetcode-cn.com/problems/trips-and-users/solution/ci-ti-bu-nan-wei-fu-za-er-by-luanz/
