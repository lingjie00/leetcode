WITH tbl AS (
    SELECT
        stock_name,
        operation,
        CASE
            WHEN operation = "Sell" THEN SUM(price)
            WHEN operation = "Buy" THEN -SUM(price)
        END AS earning
    FROM
        Stocks
    GROUP BY
        stock_name,
        operation
)

SELECT
    stock_name,
    SUM(earning) AS capital_gain_loss
FROM
    tbl
GROUP BY
    stock_name
