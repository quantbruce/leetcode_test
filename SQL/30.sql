select f.title, f.description
from (
    select category_id
    from category as c
    where c.name like '%Action%') as cc
, film as f, film_category as fc
where f.film_id = fc.film_id
and fc.category_id = cc.category_id
