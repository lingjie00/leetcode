-- create count table
WITH tbl AS (
    SELECT
        actor_id,
        director_id,
        COUNT(1) AS counts
    FROM
        ActorDirector
    GROUP BY
        actor_id,
        director_id
)

SELECT
    actor_id,
    director_id
FROM
    tbl
WHERE
    counts > 2


-- alternatively using HAVING
SELECT
    actor_id,
    director_id
FROM
    ActorDirector
GROUP BY
    actor_id,
    director_id
HAVING
    COUNT(1) > 2
