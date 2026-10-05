-- Write your query below
select left_operand,operator,right_operand, case 
when operator = '>' then v1.value > v2.value 
when operator = '<' then v1.value < v2.value 
else v1.value = v2.value end as value 
from expressions
join variables as v1 on left_operand = v1.name
join variables as v2 on right_operand = v2.name;