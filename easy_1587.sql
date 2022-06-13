-- compute the sum of the account

WITH account AS (
    SELECT
        account,
        SUM(amount) AS balance
    FROM Transactions
    GROUP BY account
    HAVING SUM(amount) > 10000
)

-- merge the account with user name
SELECT
    u.name AS name,
    a.balance AS balance
FROM Users AS u
INNER JOIN account AS a
ON u.account = a.account
