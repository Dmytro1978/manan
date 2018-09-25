select * from public.wlm_queue_state_vw

select * from public.wlm_query_state_vw

set query_group to etl_query;
reset query_group

set wlm_query_slot_count to 3;
reset wlm_query_slot_count;

select * from pg_user 

select * from pg_group




