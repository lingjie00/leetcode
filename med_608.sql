-- Three types of nodes
-- Root: no parents (p_id is null)
-- Leaf: no child
-- inner: neither of both

SELECT DISTINCT
    tbl.id,
    CASE
        WHEN tbl.p_id IS NULL THEN "Root"
        WHEN tbl.c_id IS NULL THEN "Leaf"
        ELSE "Inner"
    END AS type
FROM (
    SELECT
        t1.id AS id,
        t1.p_id AS p_id,
        t2.id AS c_id
    FROM Tree AS t1
    LEFT JOIN Tree AS t2
    ON t1.id = t2.p_id
) AS tbl
ORDER BY tbl.id
;
