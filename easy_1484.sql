SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(
        DISTINCT product ORDER BY product
    ) AS products
FROM
    Activities
GROUP BY
    sell_date
ORDER BY
    sell_date,
    GROUP_CONCAT(
        DISTINCT product ORDER BY product
    )
;

-- optimize by creating temp table
-- effectively applying DISTINCT only once
WITH distinct_table AS (
    SELECT DISTINCT
        sell_date,
        product
    FROM
        Activities
    ORDER BY
        sell_date,
        product
)

SELECT
    sell_date,
    COUNT(product) AS num_sold,
    GROUP_CONCAT(product ORDER BY product) AS products
FROM
    distinct_table
GROUP BY
    sell_date
