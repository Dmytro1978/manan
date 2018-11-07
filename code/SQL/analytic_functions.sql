with sq1 as 
(
	select 200 as id, 'asset1' as asset_name
	union all
	select 200, 'asset2' as asset_name
	union all
	select 200, 'asset3' as asset_name
	union all
	select 300, 'asset1' as asset_name
	union all
	select 300, 'asset2' as asset_name
	union all
	select 400, 'asset1' as asset_name
	union all
	select 400, 'asset2' as asset_name
	union all
	select 400, 'asset3' as asset_name
	union all
	select 400, 'asset3' as asset_name
	union all
	select 400, 'asset4' as asset_name
)
select id, asset_name, 
row_number() over (partition by id),
rank() over (order by id asc),
dense_rank() over (order by id asc)
from sq1