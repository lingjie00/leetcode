-- create AGG table
WITH tbl AS (
    SELECT
        user_id AS id,
        SUM(distance) AS distance
    FROM
        Rides
    GROUP BY
        user_id
)

SELECT
    u.name AS name,
    CASE
        WHEN r.distance IS NULL THEN 0
        ELSE r.distance
    END AS travelled_distance
FROM
    Users AS u
LEFT JOIN
    tbl AS r
USING(id)
ORDER BY
    r.distance DESC, u.name
