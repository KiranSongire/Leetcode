#596
# Write your MySQL query statement below
select 
class
from Courses
group by class
HAVING count(class)>=5