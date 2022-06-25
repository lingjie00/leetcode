-- create table storing signed price
WITH tbl AS (
    SELECT
        stock_name,
        CASE
            WHEN operation = "Buy" THEN -price
            WHEN operation = "Sell" THEN price
        END AS price
    FROM
        Stocks
)

SELECT
    stock_name,
    SUM(price) AS capital_gain_loss
FROM
    tbl
GROUP BY
    stock_name

-- alternatively in one call
SELECT
    stock_name,
    SUM(
        CASE
            WHEN operation = "Buy" THEN -price
            ELSE price
        END
    ) AS capital_gain_loss
FROM
    Stocks
GROUP BY
    stock_name
