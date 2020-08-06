###方法1 
select class
from courses
group by class
having count(distinct student) >= 5 # 我漏写了distinct

https://leetcode-cn.com/problems/classes-more-than-5-students/solution/chao-guo-5ming-xue-sheng-de-ke-by-leetcode/


###方法二 子查询


