WITH tbl AS (
    SELECT
        product_id,
        MIN(sale_date >= "2019-01-01" AND sale_date <= "2019-03-31") AS checks
    FROM
        Sales
    GROUP BY
        product_id
)

SELECT
    p.product_id,
    p.product_name
FROM
    Product AS p
LEFT JOIN
    tbl AS t1
USING(product_id)
WHERE
    t1.checks = 1
