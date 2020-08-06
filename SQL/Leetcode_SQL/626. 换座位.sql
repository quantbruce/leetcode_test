##########奇偶变位法
###很经典，而且该法效率还很高

select 
if(id&1=0,
    id -1,
    if(id=(select count(distinct id) from seat), id, id+1)) as id, # select count(distinct id) from seat这个语句要整体加括号，否则会报错
student from seat
order by id

https://leetcode-cn.com/problems/exchange-seats/solution/jian-dan-yi-dong-xiao-lu-ji-bai-suo-you-by-fan-lu-/


########官方解答法
SELECT
    (CASE
        WHEN MOD(id, 2) != 0 AND counts != id THEN id + 1
        WHEN MOD(id, 2) != 0 AND counts = id THEN id
        ELSE id - 1
    END) AS id,
    student
FROM
    seat,
    (SELECT
        COUNT(*) AS counts
    FROM
        seat) AS seat_counts
ORDER BY id ASC;

# https://leetcode-cn.com/problems/exchange-seats/solution/huan-zuo-wei-by-leetcode/

