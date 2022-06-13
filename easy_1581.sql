-- create a table containing the number of purchases per
-- visit id

WITH visit_tbl AS (
    SELECT
        visit_id,
        SUM(amount) AS amount
    FROM Transactions
    GROUP BY visit_id
),

-- join the number of purchases to the customer table

customer_tbl AS (
    SELECT
        c.customer_id,
        c.visit_id,
        v.amount
    FROM Visits AS c
    LEFT JOIN visit_tbl AS v
    ON c.visit_id = v.visit_id
)

SELECT
    customer_id,
    COUNT(customer_id) AS count_no_trans
FROM customer_tbl
WHERE amount IS NULL
GROUP BY customer_id
