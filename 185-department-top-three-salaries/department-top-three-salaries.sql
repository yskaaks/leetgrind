-- Write your PostgreSQL query statement below
select d.name as Department, e.name as Employee, e.salary as salary
from Employee e
join Department d on d.id = e.departmentId
where salary in (
    select distinct e2.salary
    from Employee e2
    join Department d2 on d2.id = e2.departmentId
    where d.id = d2.id
    order by e2.salary desc
    limit 3
);