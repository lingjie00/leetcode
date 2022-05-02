WITH netTime AS
(
    SELECT
        event_day AS day,
        emp_id,
        (out_time - in_time) AS total_time
    FROM Employees
)

SELECT day, emp_id, SUM(total_time) AS total_time
FROM netTime
GROUP BY day, emp_id
