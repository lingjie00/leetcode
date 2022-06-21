SELECT DISTINCT
    user_id,
    MAX(time_stamp) OVER(PARTITION BY user_id) AS last_stamp
FROM
    Logins
WHERE
    YEAR(time_stamp) = "2020"


-- alternatively
SELECT
    user_id,
    MAX(time_stamp) AS last_stamp
FROM (
    SELECT user_id, time_stamp
    FROM Logins
    WHERE YEAR(time_stamp) = "2020"
) AS tbl
GROUP BY
    user_id

-- creating a temp table is the fastest

WITH tbl AS (
    SELECT user_id, time_stamp
    FROM Logins
    WHERE YEAR(time_stamp) = "2020"
)

SELECT
    user_id,
    MAX(time_stamp) AS last_stamp
FROM
    tbl
GROUP BY
    user_id
