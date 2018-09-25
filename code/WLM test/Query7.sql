--truncate table mytime_china_compulsive_restday_detail;
set wlm_query_slot_count to 5;
insert into mytime_china_compulsive_restday_detail
select 
     PersonID
    ,PersonNum
    ,EmploymentStatus
    ,UserName
    ,ChineseName
    ,EnglishName
    ,Termination_Date
    ,LocationCode
    ,CostCenter
    ,COMPANYHIREDTM
    ,Full_Paid
    ,Unpaid_Leave
    ,Prolong_Sick
    ,OT_Public_Holiday
    ,OT_Switch_Weekend
    ,Attendance_Days
    ,Compulsive_Rest_Taken
    ,Comp_Rest_Miss
    ,Comp_Rest_Taken
    ,year_month
    ,Eventdtm
    ,Paycode_Name
    ,Day_Info
    ,PayRule
    ,year
    ,month
    ,convert_timezone('US/Pacific', sysdate) as etl_insert_timestamp
from vw_mytime_china_compulsive_restday_detail;

--COMMIT;



