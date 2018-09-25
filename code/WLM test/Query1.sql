--truncate table mytime_china_agencyaccrual;
set wlm_query_slot_count to 5;
insert into mytime_china_agencyaccrual
select
  personid,
  personnum,
  employee_name,
  department,
  date_joined,
  start_to_be_eligible,
  yearly_granted_al,
  vested_al,
  al_taken_jan,
  al_taken_feb,
  al_taken_mar,
  al_taken_apr,
  al_taken_may,
  al_taken_jun,
  al_taken_jul,
  al_taken_aug,
  al_taken_sep,
  al_taken_oct,
  al_taken_nov,
  al_taken_dec,
  al_taken_todate,
  legal_name,
  locationcode,
  payrule,
  year,
  total_al_taken,
  balance_vested,
  data_up_to_date,
  etl_insert_timestamp
from  vw_mytime_china_agencyaccrual;
--set wlm_query_slot_count to 1;
--COMMIT;
