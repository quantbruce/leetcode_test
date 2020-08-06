####题目意思有点坑
#group by 只是对查询结果去重，并不是真的删除掉了重复记录
#delete from 在表加了别名后，要写成 delete 别名 from 这样

delete p1
from Person p1, Person p2
where p1.Email = p2.Email and p1.Id>p2.Id

https://leetcode-cn.com/problems/delete-duplicate-emails/solution/shan-chu-zhong-fu-de-dian-zi-you-xiang-by-leetcode/
