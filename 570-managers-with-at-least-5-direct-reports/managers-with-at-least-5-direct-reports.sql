-- Write your PostgreSQL query statement below
select name 
from employee as t1
join (select managerid
from employee
group by managerid
having count(managerid) >= 5) as t2 on t1.id = t2.managerid;
