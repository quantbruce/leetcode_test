select c.name, count(f.film_id) from
(select category_id, count(film_id) from
film_category group by category_id having count(category_id)>=5) as cc,
film as f, category as c, film_category as fc
where f.description like '%robot%'
and f.film_id = fc.film_id
and fc.category_id = c.category_id
and cc.category_id = fc.category_id
