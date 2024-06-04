# Write your MySQL query statement below
 select MAX(num) As num
 from (   
    select num
    from MyNumbers 
    group by num
    having count(num) = 1
 ) As maxnumbers
