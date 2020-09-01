select e1.first_name from 
    (select e2.first_name,
        (select count(*) from employees as e3
        where e2.first_name>=e3.first_name)
        as rowid from employees as e2) as e1 
where e1.rowid % 2 = 1



-- 为什么我尝试用窗口函数却不对，navicat可以通过，而牛客网上却通过不了
select tt.first_name
from
(select first_name,
row_number() over (order by first_name) as row_idx
from test_tab) as tt
where tt.row_idx%2=1;



