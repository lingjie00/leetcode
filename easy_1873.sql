SELECT
    employee_id,
    CASE
        WHEN employee_id % 2 = 1 AND LEFT(name, 1) != "M" THEN salary
        ELSE 0
    END AS bonus
FROM
    Employees
ORDER BY
    employee_id
;

-- alternative: use IF
SELECT
    employee_id,
    IF(
        employee_id % 2 = 1 AND LEFT(name, 1) != "M",
        salary,
        0
    ) AS bonus
FROM
    Employees
ORDER BY
    employee_id
;
