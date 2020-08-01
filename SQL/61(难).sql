select e1.first_name from 
    (select e2.first_name,
        (select count(*) from employees as e3
        where e2.first_name>=e3.first_name)
        as rowid from employees as e2) as e1 
where e1.rowid % 2 = 1
