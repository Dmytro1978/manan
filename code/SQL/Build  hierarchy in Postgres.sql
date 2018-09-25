--create table HIERARCHY_1
CREATE TABLE public.hierarchy_1
(
    id bigint NOT NULL,
    name character varying(200) NOT NULL,
    par_id bigint,
    CONSTRAINT hierarchy_1_pkey PRIMARY KEY (id)
);

--truncate table hierarchy_1
--insert data into table HIERARCHY
insert into hierarchy_1
select 1, 'BOSS', null
union all
select 2, 'Manager1', 1
union all
select 3, 'Employee1', 2
union all
select 4, 'Employee2', 2
union all
select 5, 'Employee3', 2
union all
select 6, 'Manager2', 1
union all
select 7, 'Employee4', 6
union all
select 8, 'Employee5', 6
union all
select 9, 'Employee6', 6
union all
select 10, 'Intern1', 8
union all
select 11, 'Intern2', 8
union all
select 12, 'Intern3', 8;
COMMIT;

--build levels for the entire hierarchy
WITH RECURSIVE levels AS (
   SELECT id, name, par_id, 1 AS level
   FROM   hierarchy_1
   WHERE  /*id = 1*/ name = 'BOSS'
   UNION  ALL
   SELECT t.id, t.name, t.par_id, c.level + 1
   FROM   levels      c
   JOIN   hierarchy_1 t ON t.par_id = c.id
   )
SELECT name, level
FROM  levels
ORDER  BY level;

--build levels starting from manager 1 
WITH RECURSIVE cte AS (
   SELECT id, name, 1 AS level
   FROM   hierarchy_1
   WHERE  /*id = 2*/ name = 'Manager1'
   UNION  ALL
   SELECT t.id, t.name, c.level + 1
   FROM   cte      c
   JOIN   hierarchy_1 t ON t.par_id = c.id
   )
SELECT name, level
FROM   cte
ORDER  BY level;

--build levels starting from manager 2
WITH RECURSIVE cte AS (
   SELECT id, name, 1 AS level
   FROM   hierarchy_1
   WHERE  /*id = 6*/ name = 'Manager2'
   UNION  ALL
   SELECT t.id, t.name, c.level + 1
   FROM   cte      c
   JOIN   hierarchy_1 t ON t.par_id = c.id
   )
SELECT name, level
FROM   cte
--where level <= 2 --choose dept level 
ORDER  BY level;

--show hierarchy of employees and their supervisors 
WITH RECURSIVE levels AS (
   SELECT id, name, par_id, 1 AS level
   FROM   hierarchy_1
   WHERE  /*id = 1*/ name = 'BOSS'
   UNION  ALL
   SELECT t.id, t.name, t.par_id, c.level + 1
   FROM   levels      c
   JOIN   hierarchy_1 t ON t.par_id = c.id
   )
SELECT t1.name as employee_name, t1.level as employee_level, t2.name as supervisor, t2.level supervisor_level
FROM  levels t1 left join levels t2 on t1.par_id = t2.id
ORDER  BY t1.level, t1.name nulls first, t2.name;

--show hierarchy of employees and their direct reports 
WITH RECURSIVE levels AS (
   SELECT id, name, par_id, 1 AS level
   FROM   hierarchy_1
   WHERE  /*id = 1*/ name = 'BOSS'
   UNION  ALL
   SELECT t.id, t.name, t.par_id, c.level + 1
   FROM   levels      c
   JOIN   hierarchy_1 t ON t.par_id = c.id
   )
SELECT t1.name as employee_name, t1.level as employee_level, t2.name as direct_report, t2.level as direct_report_report_level
FROM  levels t1 left join levels t2 on t2.par_id = t1.id
ORDER  BY t1.level, t1.name, t2.name nulls first;

--store the hierarchy with levels in a view
--drop view v_hierarchy_1;
create or replace view v_hierarchy_1 as
WITH RECURSIVE levels AS (
   SELECT id, name, par_id, 1 AS level
   FROM   hierarchy_1
   WHERE  /*id = 1*/ name = 'BOSS'
   UNION  ALL
   SELECT t.id, t.name, t.par_id, c.level + 1
   FROM   levels      c
   JOIN   hierarchy_1 t ON t.par_id = c.id
   )
SELECT id, name, par_id, level
FROM  levels
ORDER  BY level, name;

--select a sub-hierarchy for Manager2 (Employee5) with original levels
WITH RECURSIVE levels AS (
   SELECT id, name, par_id, level
   FROM   v_hierarchy_1
   WHERE  /*id = 1*/ name = 'Manager2' -- 'Employee5'
   UNION  ALL
   SELECT t.id, t.name, t.par_id, t.level 
   FROM   levels      c
   JOIN   v_hierarchy_1 t ON t.par_id = c.id
   )
SELECT id, name, level
FROM  levels
ORDER  BY level, name;


--dates generator
select cast('2018-02-20' as date) + generate_series  
FROM generate_series(0,20)



