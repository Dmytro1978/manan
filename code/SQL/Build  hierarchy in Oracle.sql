
create table hierarchy_1
(
    id number(18) not null primary key,
    name varchar2(200) not null,
    par_id number(18) null
);

--truncate table hierarchy_1;

--insert data into table HIERARCHY
insert into hierarchy_1
select 1, 'BOSS', null from dual
union all
select 2, 'Manager1', 1 from dual
union all
select 3, 'Employee1', 2 from dual
union all
select 4, 'Employee2', 2 from dual
union all
select 5, 'Employee3', 2 from dual
union all
select 6, 'Manager2', 1 from dual
union all
select 7, 'Employee4', 6 from dual
union all
select 8, 'Employee5', 6 from dual
union all
select 9, 'Employee6', 6 from dual
union all
select 10, 'Intern1', 8 from dual
union all
select 11, 'Intern2', 8 from dual
union all
select 12, 'Intern3', 8 from dual;
COMMIT;


--select a sub-hierarchy for Manager2 (Employee5) with levels
select id, name, level
from v_hierarchy_1
start with name = 'Manager2' --try 'Employee5'
connect by prior id = par_id
order by level, name;

-- create a view that selects full  hierarchy with levels
create view v_hierarchy_1 as
select id, name, par_id, level as level_
from hierarchy_1 
start with id  = 1
connect by prior id = par_id
order by level, name;

--select a sub-hierarchy for Manager2 (Employee5) with original levels
select id, name, level_
from v_hierarchy_1
start with name = 'Manager2' --try 'Employee5'
connect by prior id = par_id
order by level_, name;

--date generator
select to_date('1969-12-31','yyyy-mm-dd') + level as dt 
from dual
connect by level < 100;
