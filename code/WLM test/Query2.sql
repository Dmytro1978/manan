--truncate table mytime_china_amzl_abs_exception;
set wlm_query_slot_count to 5;
insert into mytime_china_amzl_abs_exception
select 
   personid
  ,personnum
  ,username
  ,city
  ,locationcode
  ,null as payrule
  ,repdate
  ,numpackages
  ,attendancepaycode
  ,absenceexception
  ,shiftcomment
  ,commentnotes
  ,etl_insert_timestamp
  ,chinesename
  ,username
from vw_mytime_china_amzl_absence_exception;

--COMMIT;
