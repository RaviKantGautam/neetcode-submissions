-- Write your query below
SELECT pp.first_name, pp.last_name, addr.city, addr.state from person as pp left join address as addr
on pp.person_id = addr.person_id;
