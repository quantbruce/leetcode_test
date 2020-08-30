select p.*, t.content
from person as p
left outer join task as t
on p.id = t.person_id
order by p.id 
