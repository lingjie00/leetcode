-- get purchase in 2019
WITH tbl AS (
    SELECT
        buyer_id AS user_id,
        COUNT(item_id) AS purchase
    FROM
        Orders
    WHERE
        YEAR(order_date) = "2019"
    GROUP BY
        buyer_id
)

SELECT
    u.user_id AS buyer_id,
    u.join_date AS join_date,
    CASE
        WHEN t1.purchase IS NULL THEN 0
        ELSE t1.purchase
    END AS orders_in_2019
FROM
    Users AS u
LEFT JOIN
    tbl AS t1
USING(user_id)
