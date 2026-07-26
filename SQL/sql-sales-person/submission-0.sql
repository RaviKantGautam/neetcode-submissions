-- Write your query below
select sp.name from sales_person as sp where sp.sales_id not in (
select ord.sales_id from orders as ord
inner join company as cp on ord.com_id = cp.com_id
where cp.name = 'CRIMSON'
)