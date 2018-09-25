--truncate table mytime_china_exceed_approach_overtime;
set wlm_query_slot_count to 5;
insert into mytime_china_exceed_approach_overtime
select 
	personid
,	personnum
,	employment_status
,	user_name
,	employee_name
,	legal_name
,	supervisor_name
,	supervisor_legal_name
,	hire_date
, null::date as termination_date
,	employee_type
,	department
,	locationcode
,	locationdescription
,	total_available_hours
,	standard_available_hours
,	actualhours
,	overall_residual_working_hours
,	occurred_ot
,	cwhs_cycle
,	etl_insert_timestamp
,	periodstart
,report_type_id
from public.vw_mytime_china_exceed_approach_overtime_mm
union all
select 
	personid
,	personnum
,	employment_status
,	user_name
,	employee_name
,	legal_name
,	supervisor_name
,	supervisor_legal_name
,	hire_date
, null as termination_date
,	employee_type
,	department
,	locationcode
,	locationdescription
,	total_available_hours
,	standard_available_hours
,	actualhours
,	overall_residual_working_hours
,	occurred_ot
,	cwhs_cycle
,	etl_insert_timestamp
,	periodstart
,report_type_id
from public.vw_mytime_china_exceed_approach_overtime_qq
union all
select 
	personid
,	personnum
,	employment_status
,	user_name
,	employee_name
,	legal_name
,	supervisor_name
,	supervisor_legal_name
,	hire_date
, null as termination_date
,	employee_type
,	department
,	locationcode
,	locationdescription
,	total_available_hours
,	standard_available_hours
,	actualhours
,	overall_residual_working_hours
,	occurred_ot
,	cwhs_cycle
,	etl_insert_timestamp
,	periodstart
,report_type_id
from public.vw_mytime_china_exceed_approach_overtime_sa
union all
select 
	personid
,	personnum
,	employment_status
,	user_name
,	employee_name
,	legal_name
,	supervisor_name
,	supervisor_legal_name
,	hire_date
, null as termination_date
,	employee_type
,	department
,	locationcode
,	locationdescription
,	total_available_hours
,	standard_available_hours
,	actualhours
,	overall_residual_working_hours
,	occurred_ot
,	cwhs_cycle
,	etl_insert_timestamp
,	periodstart
,report_type_id
from public.vw_mytime_china_exceed_approach_overtime_yy;

--COMMIT;
