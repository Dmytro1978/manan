-- Number of orders placed (for last 30 days)
select t2.day_code, t3.order_status_desc, COUNT(*) order_cnt
from f_order t1, l_date t2, l_order_status t3
where
    t1.day_key = t2.day_key and
    t2.day_code > SYSDATE - 30 and
    t3.order_status_key = t1.order_status_key and
    t3.order_status_desc =  'payment_processed'
group by t2.day_code, t3.order_status_desc
order by 1 asc;
    
-- Gross sales. Definition: total sales after coupons applied,  including sales tax, excluding shipping charge
-- total order's charge contains total sales, taxes coupons applied and shipping charge. We just need to exclude shipping charge to receive gross sales 
select t2.day_code, sum(t1.charge_amount - t4.shipping_charge) gross_sum
from f_order t1, l_date t2, l_order_status t3, f_shipment t4
where
    t4.day_key = t2.day_key and
    t2.day_code > SYSDATE - 30 and
    t4.order_key = t1.order_key and
    t3.order_status_key = t1.order_status_key and
    t3.order_status_desc = 'shipped'
group by t2.day_code;

--Net Sales. Definition: total sales minus cost of goods, minus returns,  including sales tax, excluding shipping charge
with v_returns as 
(   --since returns are stored as 1 row per unit first we have to aggregate them to item level
    select day_code, item_key, sum(amount_refunded) amount_refunded
    from f_return t1,l_date t2 
    where
        t1.day_key = t2.day_key and
        t2.day_code > sysdate -30   
    group by  day_code, item_key   
)
select t2.day_code, sum( (t4.sale_price - t5.cost)*t4.quantity_ordered + t1.tax_amount - t7.amount_refunded) as net_sales
from f_order t1, l_date t2, l_order_status t3, f_item t4, l_variant t5, v_returns t7
where
    t1.order_key = t4.order_key and
    t4.variant_key = t5.variant_key and
    t5.CURRENT_FLAG = 'Y' and
    t1.day_key = t2.day_key and
	t4.day_key = t1.day_key and
    t2.day_code > sysdate -30 and
    t7.item_key = t4.item_key and
    t2.day_code = t7.day_code and
    t2.day_code between t5.effective_start_date and t5.effective_end_date and
    t3.order_status_key = t1.order_status_key and
    t3.order_status_desc =  'payment_processed'
group by t2.day_code
order by 1 asc;     
  
--Margin per product (per size, per day)
select t6.product_desc, t5.size_, sum((t4.sale_price - t5.cost)/t4.sale_price) as margin
from l_date t2, l_order_status t3, f_item t4, l_variant t5, l_product t6
where
    t4.variant_key = t5.variant_key and
    t6.CURRENT_FLAG = 'Y' and
    t5.CURRENT_FLAG = 'Y' and
    t5.product_key = t6.product_key and
    t4.day_key = t2.day_key and
    t2.day_code between t5.effective_start_date and t5.effective_end_date and
    t6.product_key = t5.product_key 
group by t6.product_desc, t5.size_
order by 1 asc;


-- recent status of orders placed yesterday
select order_key, id, order_time, order_status_desc from (
    select t1.order_key, t1.id, t1.order_time, t3.order_status_desc,
    row_number() over (partition by t1.id order by t1.order_time) r
    from f_order t1, l_date t2, l_order_status t3
    where
        t1.day_key = t2.day_key and
        t2.day_code >= trunc(sysdate) - 1 and
        t3.order_status_key = t1.order_status_key
) a
where    
    a.r = 1;

--Time between different steps in order lifecycle (for last two days)
select a.id, a.order_status_desc, 
    extract(day from (a.order_time - a.prev_step_time) day to second) || 'd ' ||  
    extract(hour from (a.order_time - a.prev_step_time) day to second)  || 'h ' || 
    extract(minute from (a.order_time - a.prev_step_time) day to second)  || 'm ' || 
    extract(second from (a.order_time - a.prev_step_time) day to second)   || 's' as time_elapsed 
from (
    select t1.id, t3.order_status_desc, t1.order_time, lag(t1.order_time) over (order by t1.order_time asc) prev_step_time
    from f_order t1, l_date t2, l_order_status t3
    where
        t1.day_key = t2.day_key and
        t2.day_code >= trunc(sysdate) - 1 and
        t3.order_status_key = t1.order_status_key 
) a;

