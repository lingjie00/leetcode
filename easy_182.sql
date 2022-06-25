-- create a count table
WITH tbl AS (
    SELECT
        email,
        COUNT(1) AS counts
    FROM
        Person
    GROUP BY
        email
)

SELECT
    email
FROM
    tbl
WHERE
    counts > 1
