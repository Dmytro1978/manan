select j.emplid, j.deptid, dpt.descr, jc.descr, j.effdt, j.annual_rt, j.currency_cd, j.reg_region
from ps_job j, ps_jobcode_tbl jc, ps_dept_tbl dpt
where 
    emplid = '101465205' and
    jc.jobcode = j.jobcode and
    dpt.deptid = j.deptid and
    --dpt.eff_status = 'A' and 
    dpt.setid = 'USAID' and
    jc.effdt = (select max(jc1.effdt) from ps_jobcode_tbl jc1 where jc1.jobcode = jc.jobcode) and
    j.effseq = (select max(j1.effseq) from ps_job j1 where j.emplid = j1.emplid and j.effdt = j1.effdt) and
    dpt.effdt = (select max(dpt1.effdt) from ps_dept_tbl dpt1 where dpt1.deptid = dpt.deptid and dpt1.eff_status = 'A' and dpt1.setid = 'USAID')
order by j.effdt desc, j.effseq desc


select * from ps_job where emplid = '102152773' 

select * from ps_jobcode_tbl

select * from ps_job
where emplid = '101465205'
order by effdt desc, effseq desc

select * from ps_dept_tbl dpt
where --descr = 'AWS Professional Services' 
--and 
deptid = '4001' 
and 
eff_status = 'A' and 
setid = 'USAID' and 
effdt = (select max(dpt1.effdt) from ps_dept_tbl dpt1 where dpt1.deptid = '4001')