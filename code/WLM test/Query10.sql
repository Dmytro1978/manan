--truncate table mytime_china_timeoff_request_cal_days;
set wlm_query_slot_count to 5;
insert into mytime_china_timeoff_request_cal_days
select
  personid,
  personnum,
  employmentstatus,
  username,
  chinesename,
  englishname,
  hiredate,
  terminationdate,
  locationcode,
  costcenter,
  payrule,
  transationdate,
  timeoffexception,
  etl_insert_timestamp
from vw_mytime_china_timeoff_request_cal_days;

--COMMIT;
