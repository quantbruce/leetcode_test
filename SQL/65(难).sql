select g1.id, l.name, g1.score
from grade g1 
inner join language l
on g1.language_id = l.id
where (
    select count(distinct g2.score)
    from grade g2 
    where g1.score <= g2.score
    and g1.language_id = g2.language_id) <=2  # 这种写法少见，留意下！！
order by l.name, g1.score desc, g1.id



###使用了窗口函数 dense_rank()

select g.id, l.name, g.score
from (select *, 
      dense_rank() over(partition by language_id order by score desc) as rank 
      from grade) g, 
      language l
where g.language_id = l.id and g.rank <= 2
order by l.name asc, g.score desc, g.id asc
