--Which user tier do most Intercom customers fall into now?
with SQ1 AS ( 
	select t2.user_tier_name, count(distinct t1.customer_id) customer_cnt -- count distinct to avoid duplications caused by multiple products assigned to customer
	from f_subscription t1, d_user_tier t2 
	where
		t1.user_tier_id = t2.user_tier_id and
		t1.end_date = null -- select current tier states
	group by t2.user_tier_name
)
select user_tier_name, customer_cnt
from SQ1 
where 
	customer_cnt in (select max(customer_cnt) from SQ1);
	
-- How about 3 months ago?
with SQ1 AS ( 
	select t2.user_tier_name, count(distinct t1.customer_id) customer_cnt
	from f_subscription t1, d_user_tier t2 
	where
		t1.user_tier_id = t2.user_tier_id and
		start_date <= trunc(sysdate)-90 and --select historical data
		end_date >= trunc(sysdate)-90
	group by t2.user_tier_name
)
select user_tier_name, customer_cnt
from SQ1 
where 
	customer_cnt in (select max(customer_cnt) from SQ1);	
	
--How long has a customer had a certain product? 
select t2.customer_name, t3.product_name, trunc(sysdate) - t1.start_date product -- calculate number of days
from f_subscription t1, d_customer t2, d_product t3
where
	t1.customer_id = t2.custiomer_id and
	t1.product_id = t3.product_id and
	t1.end_date is null -- select current state

--Which products are most popular on each user tier?
with SQ1 AS ( 
	select t2.user_tier_name, t1.product_id, count(*) product_cnt
	from f_subscription t1, d_user_tier t2, d_product t3
	where
		t1.user_tier_id = t2.user_tier_id and
		t1.product_id = t3.product_id and
		t1.end_date is null
	group by t2.user_tier_name, t1.product_id
)
select user_tier_name, product_id 
from (
	select user_tier_name, product_id, row_number() over(partition by user_tier_name, product_id order by product_cnt desc) r -- ranking product counts per tier  
	from SQ1
) a
where	
	a.r = 1 --select the greater product count per tier

	