WITH tbl AS (
    SELECT
        customer_number,
        COUNT(1) AS orders
    FROM
        Orders
    GROUP BY
        customer_number
)

SELECT
    customer_number
FROM
    tbl
ORDER BY
    orders DESC
LIMIT 1
