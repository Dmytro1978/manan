--truncate table mytime_china_compulsive_restday_summary;
set wlm_query_slot_count to 5;
insert into mytime_china_compulsive_restday_summary
select 
  personid,
  personnum,
  username,
  employmentstatus,
  chinesename,
  englishname,
  city,
  locationcode,
  repdate,
  costcenter,
  rest_times_taken,
  miss_rest_times,
  scheduled_rest_times,
  repyear,
  etl_insert_timestamp
from vw_mytime_china_compulsive_restday_summary;

--COMMIT;
