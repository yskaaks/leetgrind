-- Write your PostgreSQL query statement below
with employee_id_with_number_of_department as (
    select employee_id, count(department_id) as number_of_department
    from Employee
    group by employee_id 
) 

select e.employee_id, department_id   
from Employee e
inner join employee_id_with_number_of_department ed on e.employee_id = ed.employee_id
and (number_of_department = 1 or primary_flag = 'Y');