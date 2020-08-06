#######My Method
select tab.Email
from (
select Email, count(Email) as cnt
from Person
group by Email) as tab
where cnt <> 1
