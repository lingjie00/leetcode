SELECT
    e.employee_id AS employee_id
FROM
    Employees AS e
FULL JOIN
    Salaries AS s
ON e.employee_id = s.employee_id
WHERE
    e.name IS NULL
    OR
    s.salary IS NULL
ORDER BY e.employee_id
;

-- using UNION

SELECT
    e.employee_id
FROM Employees AS e
LEFT JOIN
    Salaries AS s
USING(employee_id)
WHERE s.salary IS NULL

UNION

SELECT
    s.employee_id
FROM Salaries AS s
LEFT JOIN
    Employees AS e
USING(employee_id)
WHERE e.name IS NULL

ORDER BY employee_id

;
