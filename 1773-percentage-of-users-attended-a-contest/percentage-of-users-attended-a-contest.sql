-- Write your PostgreSQL query statement below
select r.contest_id, round(count(*) * 100.0 / (select count(*) from Users),2) as percentage
from Register r
group by contest_id
order by percentage desc, contest_id
;