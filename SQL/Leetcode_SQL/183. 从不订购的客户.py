###########My Methods
select C.Name as Customers
from Customers as c
where c.Id not in (
    select distinct CustomerId from Orders 
)

#########方法2
select C.Name as Customers
from Customers as c
left join Orders as o
on c.Id = o.CustomerId
where o.CustomerId  is null;

https://leetcode-cn.com/problems/customers-who-never-order/solution/tu-jie-sqlmian-shi-ti-cha-zhao-bu-zai-biao-li-de-s/

