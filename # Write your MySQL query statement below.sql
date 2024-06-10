# Write your MySQL query statement below
select 
m.employee_id, 
m.name, 
count(e.employee_id) as reports_count, 
ROUND(AVG(e.age)) as average_age
from employees e join employees m 
on e.reports_to = m.employee_id
Group by m.employee_id
order by employee_id
