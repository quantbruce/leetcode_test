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



