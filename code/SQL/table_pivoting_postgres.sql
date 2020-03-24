-- table pivoting in Postgres

drop table if exists cust_info;
create table cust_info
(
	cust_id bigint not null,
	attr varchar(50) not null,
	value varchar(100) null,
	create_ts timestamp not null
);

insert into cust_info
select 100, 'First Name', 'Sam', current_timestamp
union all
select 100, 'Last Name', 'Jonhs', current_timestamp
union all
select 100, 'email', 'SamJohns@gmail.com', current_timestamp
union all
select 200, 'First Name', 'Anna', current_timestamp
union all
select 200, 'Last Name', 'Cohls', current_timestamp
union all
select 200, 'email', 'AnnaCohls@gmail.com', current_timestamp
union all
select 300, 'First Name', 'Ivan', current_timestamp
union all
select 300, 'Last Name', 'Evans', current_timestamp
union all
select 300, 'email', 'IvanEvans@gmail.com', current_timestamp
union all
select 100, 'email', 'SamJohns_new@gmail.com', current_timestamp + interval'5 seconds'
union all
select 300, 'Last Name', 'Evans II', current_timestamp + interval'10 seconds'
union all
select 400, 'First Name', 'Julia', current_timestamp
union all
select 400, 'Last Name', 'Roberts', current_timestamp;

-- 1.
-- pivoting without using special functions
with sq1 as (
	select cust_id, attr, value, row_number() over(partition by cust_id, attr order by create_ts desc) r
	from cust_info
)
, sq2 as (
	select cust_id, attr, value
	from sq1
	where
		r = 1
)
select distinct t1.cust_id, t2.value as first_name, t3.value as last_name, t4.value as email
from sq1 t1
	left join sq2 t2 on t1.cust_id = t2.cust_id and t2.attr = 'First Name'
	left join sq2 t3 on t1.cust_id = t3.cust_id and t3.attr = 'Last Name'
	left join sq2 t4 on t1.cust_id = t4.cust_id and t4.attr = 'email'
order by t1.cust_id;

-- 2.
-- pivoting using 'crosstab' function

-- create 'tablefunc' extention
-- ('crosstab' function is part of a PostgreSQL extension called 'tablefunc')
drop extension if exists tablefunc;
CREATE extension tablefunc;

-- create view 
drop view if exists cust_pivot_vw;
create view cust_pivot_vw as 
with sq1 as ( -- rank attribytes by creation time
	select cust_id, attr, value, row_number() over(partition by cust_id, attr order by create_ts desc) r
	from cust_info
)
select cust_id, attr, value
from sq1
where
	r = 1; -- only select latest attrutes

-- pivot table
select cust_id, first_name, last_name, email
from crosstab( 'select cust_id, attr, value from cust_pivot_vw') 
AS final_result(cust_id bigint, first_name varchar, last_name varchar, email varchar);




