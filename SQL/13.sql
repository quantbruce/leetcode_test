select title, count(*) as t
from titles
group by title
having t >= 2;
