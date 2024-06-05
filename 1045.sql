# Write your MySQL query statement below
select customer_id
from Customer
GROUP BY customer_id
HAVING COUNT(distinct product_key) = (select count(product_key) from Product)