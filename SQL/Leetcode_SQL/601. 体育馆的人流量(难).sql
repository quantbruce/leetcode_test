###这题思路比较经典，多看题解理解吃透

select distinct a.* # distinct 比较容易漏掉
from stadium a, stadium b, stadium c
where ((a.id=b.id-1 and b.id+1=c.id)
or (b.id=a.id-1 and a.id+1=c.id)
or (b.id=c.id-1 and c.id+1=a.id))
and a.people>=100 and b.people>=100 and c.people>=100
order by a.id

https://leetcode-cn.com/problems/human-traffic-of-stadium/solution/ti-yu-guan-de-ren-liu-liang-by-little_bird/

