-- Write your PostgreSQL query statement below
select unique_id, name
from employees
left join EmployeeUNI on employees.id = EmployeeUNI.id;