SELECT ROUND(SUM(tiv_2016)::decimal,2) AS tiv_2016
FROM Insurance i 
WHERE i.tiv_2015 IN (
    SELECT i2.tiv_2015 
    FROM insurance i2 
    WHERE i.pid != i2.pid
)
AND (i.lat, i.lon) NOT IN (
    SELECT lat, lon 
    FROM insurance i3 
    WHERE i.pid != i3.pid
);