--logged in iser (mdmytro) is in dev_group
select * from wlm_queue_state_vw;
select * from wlm_query_state_vw;

set query_group to etl_query;

select * from wlm_queue_state_vw;
select * from wlm_query_state_vw;

set wlm_query_slot_count to 5;

select * from wlm_queue_state_vw;
select * from wlm_query_state_vw;

reset query_group;

select * from wlm_queue_state_vw;
select * from wlm_query_state_vw;

set wlm_query_slot_count to 1;

select * from wlm_queue_state_vw;
select * from wlm_query_state_vw;
