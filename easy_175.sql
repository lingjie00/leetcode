SELECT
    p.firstName AS firstName,
    p.lastName AS lastName,
    a.city AS city,
    a.state AS state
FROM
    Person AS p
LEFT JOIN
    Address AS a
USING(personId)
;
