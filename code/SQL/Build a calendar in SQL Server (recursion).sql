-- the code generates a set of dates from '2018-01-01' to '2018-01-22'
with theDates AS
(
  SELECT CAST('2018-01-01' AS datetime) AS theDate 
  UNION ALL 
  SELECT DATEADD(DAY,1,theDate)
  FROM theDates
  WHERE DATEADD(DAY,1,theDate) <= CAST('2018-01-22' AS datetime)
)
select * from thedates
option(maxrecursion 0)