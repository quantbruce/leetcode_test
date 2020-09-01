select c.name, count(f.film_id) from
(select category_id, count(film_id) from      -- film_id 填入下面的括号才对！！！， 也即 count(film_id)>=5
film_category group by category_id having count(category_id)>=5) as cc, -- 不是找了之后再筛选>=5, 而是先筛选出>=5的这个群体，然后直接在里面再接着选
film as f, category as c, film_category as fc
where f.description like '%robot%'
and f.film_id = fc.film_id
and fc.category_id = c.category_id
and cc.category_id = fc.category_id 

