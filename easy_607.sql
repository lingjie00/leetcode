--Approach: sequential logic
-- first filter the com_id of "RED"
WITH c AS (
    SELECT
        com_id
    FROM Company
    WHERE name = "RED"
),

-- then select orders belonging to the com_id
o AS (
    SELECT DISTINCT
        sales_id,
        order_id
    FROM Orders
    JOIN c
    USING(com_id)
)

-- lastly retrieve the names
SELECT DISTINCT
    name
FROM SalesPerson
LEFT JOIN o
USING(sales_id)
WHERE o.order_id IS NULL


-- Approach: optimize the previous logic
WITH tbl AS (
    SELECT
        o.sales_id,
        o.order_id
    FROM Company AS c
    JOIN Orders AS o
    USING(com_id)
    WHERE c.name = "RED"
)

SELECT DISTINCT
    name
FROM SalesPerson
LEFT JOIN tbl
USING(sales_id)
WHERE tbl.order_id IS NULL
