-- Write your query below
select users.name, COALESCE(sum(rides.distance), 0) as travelled_distance from users left join rides on users.id = rides.user_id
group by rides.user_id, users.name 
order by travelled_distance DESC, users.name ASC;
