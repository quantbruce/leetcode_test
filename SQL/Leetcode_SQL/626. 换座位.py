##########奇偶变位法
###很经典，而且该法效率还很高

select 
if(id&1=0,
    id -1,
    if(id=(select count(distinct id) from seat), id, id+1)) as id, # select count(distinct id) from seat这个语句要整体加括号，否则会报错
student from seat
order by id

https://leetcode-cn.com/problems/exchange-seats/solution/jian-dan-yi-dong-xiao-lu-ji-bai-suo-you-by-fan-lu-/



