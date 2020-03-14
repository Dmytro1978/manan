-- find number of active subscriptions in every month
-- the difficulty of counting of active subscriptions in every month is that a subscription period is defined by subscription start date and subscription 
-- end date and if the period is more than two months then months in between are not stored anythere. For example, the subscription is for Jan, Feb and Mar 
-- will be stored in the table as one record with date_start=2020-01-01 date_end=2020-03-31, thus Feb will not be indicated anythere. In this case the 
-- solution is to generate records which would represend every month in the subscription period. For example, for the subscription described above there 
-- will be 3 records: 1-Jan, 2-Feb, 3-Mar. In this case we can easily count them.

drop table if exists subscriptions;

create table subscriptions
as
select 1 as id, date'2020-01-01' as date_start, date'2020-03-04' as date_end
union all
select 2, date'2020-02-05' as date_start, date'2020-02-21' as date_end
union all
select 3, date'2020-02-10' as date_start, date'2020-03-27' as date_end
union all
select 4, date'2020-01-05' as date_start, date'2020-02-15' as date_end
union all
select 5, date'2020-01-05' as date_start, date'2020-01-31' as date_end
union all
select 6, date'2020-03-07' as date_start, date'2020-04-21' as date_end;

-- solution 1: using recursive CTE (Common Table Expression) 
-- works on most database engines
with recursive sq1 as(
	select id, date_start::date as date_start, date_end 
	from subscriptions
	union all
	select id, (date_start + interval'1 month')::date, date_end
	from sq1
	where
		date_start < date_end
),
sq2 as (
	select id, cast(extract(year from date_start) as varchar) || cast(extract(month from date_start) as varchar) as every_month_yyyymm
	from sq1
)
select sq2.every_month_yyyymm, count(s.id) 
from sq2, subscriptions s
where
	sq2.id = s.id and
	sq2.every_month_yyyymm between
		cast(extract(year from s.date_start) as varchar) || cast(extract(month from s.date_start) as varchar) and
		cast(extract(year from s.date_end) as varchar) || cast(extract(month from s.date_end) as varchar) 
group by sq2.every_month_yyyymm
order by every_month_yyyymm;

-- "20201"	"3"
-- "20202"	"4"
-- "20203"	"3"
-- "20204"	"1"

-- Solution 2: using generate_series() function 
-- works in Postgres only
with sq1 as (
    select min(date_start) date_start, max(date_end) date_end 
    from subscriptions
)
,sq2 as ( -- distribute (cartesian join) each subscription id across all months in the range between min(date_start) and max(date_end)
    select s.id, cast(extract(year from cc.every_month) as varchar)|| cast(extract(month from cc.every_month) as varchar) as every_month_yyyymm
    from (select generate_series((select date_start from sq1)::timestamp, (select date_end from sq1)::timestamp, '1 month') every_month) cc, subscriptions s
)
select sq2.every_month_yyyymm, count(s.id) --count only subscriptions which yyyyymm is between subscription's date_start and date_end
from sq2, subscriptions s
where
    sq2.id = s.id and
    every_month_yyyymm between  
        cast(extract(year from s.date_start) as varchar) || cast(extract(month from s.date_start) as varchar) and
        cast(extract(year from s.date_end) as varchar) || cast(extract(month from s.date_end) as varchar)
group by every_month_yyyymm;

-- "20201"	"3"
-- "20202"	"4"
-- "20203"	"3"
-- "20204"	"1"


