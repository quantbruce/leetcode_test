SELECT distinct l1.Num as ConsecutiveNums
FROM
    Logs as l1,
    logs as l2,
    logs as l3
where 
    l1.Id = l2.Id - 1 
    and l2.Id = l3.Id - 1
    and l1.Num = l2.Num
    and l2.Num = l3.Num

https://leetcode-cn.com/problems/consecutive-numbers/solution/lian-xu-chu-xian-de-shu-zi-by-leetcode/


