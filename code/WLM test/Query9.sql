--truncate table mytime_china_personal_leave_gt_5_days;
set wlm_query_slot_count to 5;
insert into mytime_china_personal_leave_gt_5_days
select 
  personid,
  personnum,
  employmentstatus,
  username,
  legalname,
  englishname,
  hiredate,
  costcenter,
  locationcode,
  payrule,
  leave_type,
  leave_type_chinese,
  leave_start_dt,
  total_days,
  etl_insert_timestamp
from public.vw_mytime_china_personal_leave_gt_5_days;

--commit;
