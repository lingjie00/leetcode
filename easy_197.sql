-- approach: using ROW_NUMBER and match by the previous row
-- does not work because there are skipping dates

-- create a temporary table with row numbers
WITH tbl AS (
    SELECT
        *,
        ROW_NUMBER() OVER(ORDER BY recordDate) AS row_num,
        ROW_NUMBER() OVER(ORDER BY recordDate) - 1 AS row_num_m1
    FROM
        Weather
)

-- join the tables by row number and the lagged one number
SELECT
    t1.id AS id
FROM tbl AS t1
JOIN tbl AS t2
ON t1.row_num_m1 = t2.row_num
WHERE t1.temperature > t2.temperature

-- approach: use date manipulation
WITH tbl AS (
    SELECT
        id,
        recordDate,
        temperature,
        DATE_SUB(recordDate, INTERVAL 1 DAY) AS dayBefore
    FROM
        Weather
)
SELECT
    t1.id AS id
FROM tbl AS t1
JOIN tbl AS t2
ON t1.dayBefore = t2.recordDate
WHERE t1.temperature > t2.temperature
