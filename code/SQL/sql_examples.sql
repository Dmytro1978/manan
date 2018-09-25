--select n top number without window function
with test1 as (
  select 10 as id from dual
  union all
  select 20 from dual
  union all
  select 30 from dual
  union all
  select 40 from dual
  union all
  select 50 from dual
)
,test2 as (
select * from test1 order by id desc limit 2
)
select * from test2 order by id asc limit 1

--query that does not work in Hive (subquery in where clause):
--cte1
with t111 as (
select '1' as id, 'aaa' as name
union all
select '2', 'bbb'
)
--cte2
, t222 as ( 
select 3 as id, '22' as value, 1 as id1, sysdate - 3 as dt
union all
select 4, '33', 1, sysdate -2
union all
select 3, '44', 2, sysdate -5
union all
select 4, '55', 2, sysdate -6
)
-- actual script
select t1.*,t2.* 
from t111 t1,t222 t2 
where
  t2.id1 = t1.id and 
  t2.dt = (select max(dt) from t222 t3 where t3.id1 = t2.id1)  
  
--workaround
--cte1
with t111 as (
select '1' as id, 'aaa' as name
union all
select '2', 'bbb'
)
--cte2
, t222 as ( 
select 3 as id, '22' as value, 1 as id1, sysdate - 3 as dt
union all
select 4, '33', 1, sysdate -2
union all
select 3, '44', 2, sysdate -5
union all
select 4, '55', 2, sysdate -6
)
-- actual script
, sq as (
select id, value, id1, dt from (
  select id, value, id1, dt, row_number() over(partition by id1 order by dt desc) r from t222
  )a where a.r = 1
)
select t1.*,t2.* 
from t111 t1,sq t2 
where
  t2.id1 = t1.id 

select * from mytime_china_amzl_abs_exception limit 20


select t1.*,t2.* 
from t111 t1, t222 t2 
where t2.id1 > t1.id 

create table t111
(
  id string,
  name string
)

create table t222
(
  id string,
  value string,
  id1 string,
  dt date
)

--query that does not work in Hive (non-equi left join):
with sq1 as (
select 1 as id
union all
select 2
union all
select 3
union all
select 4
union all
select 5
),
sq2 as (
select 4 as id
union all
select 5
)
select t1.*, t2.*
from sq1 t1 left join sq2 t2 on t1.id < t2.id



-- a workaround for non-equi left join in Hive: 
with sq1 as (
select 1 as id
union all
select 2
union all
select 3
union all
select 4
union all
select 5
),
sq2 as (
select 4 as id
union all
select 5
),
sq3 as 
(select t1.id, t2.id as id2
from sq1 t1, sq2 t2 
where 
  t1.id < t2.id)
select t1.id, t3.id2
from sq1 t1 left join sq3 t3 on t1.id = t3.id
