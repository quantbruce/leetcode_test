create table if not exists actor(
    actor_id smallint(5) not null,
    first_name varchar(45) not null,
    last_name varchar(45) not null,
    last_update timestamp not null default(datetime('now', 'localtime')),
    primary key(actor_id))
