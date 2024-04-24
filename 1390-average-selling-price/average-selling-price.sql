-- Write your PostgreSQL query statement below
select p.product_id, ROUND(
        CASE 
            WHEN SUM(u.units) IS NULL OR SUM(u.units) = 0 THEN 0
            ELSE SUM(p.price * u.units) * 1.0 / SUM(u.units)
        END, 
        2
    ) AS average_price
from prices p
left join UnitsSold u on u.product_id = p.product_id and u.purchase_date BETWEEN p.start_date and p.end_date
group by p.product_id