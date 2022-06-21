SELECT
    id,
    MAX(CASE WHEN month = "Jan" THEN Revenue END) AS Jan_Revenue,
    MAX(CASE WHEN month = "Feb" THEN Revenue END) AS Feb_Revenue,
    MAX(CASE WHEN month = "Mar" THEN Revenue END) AS Mar_Revenue,
    MAX(CASE WHEN month = "Apr" THEN Revenue END) AS Apr_Revenue,
    MAX(CASE WHEN month = "May" THEN Revenue END) AS May_Revenue,
    MAX(CASE WHEN month = "Jun" THEN Revenue END) AS Jun_Revenue,
    MAX(CASE WHEN month = "Jul" THEN Revenue END) AS Jul_Revenue,
    MAX(CASE WHEN month = "Aug" THEN Revenue END) AS Aug_Revenue,
    MAX(CASE WHEN month = "Sep" THEN Revenue END) AS Sep_Revenue,
    MAX(CASE WHEN month = "Oct" THEN Revenue END) AS Oct_Revenue,
    MAX(CASE WHEN month = "Nov" THEN Revenue END) AS Nov_Revenue,
    MAX(CASE WHEN month = "Dec" THEN Revenue END) AS Dec_Revenue
FROM
    Department
GROUP BY
    id

-- using SUM
SELECT
    id,
    SUM(CASE WHEN month = "Jan" THEN Revenue END) AS Jan_Revenue,
    SUM(CASE WHEN month = "Feb" THEN Revenue END) AS Feb_Revenue,
    SUM(CASE WHEN month = "Mar" THEN Revenue END) AS Mar_Revenue,
    SUM(CASE WHEN month = "Apr" THEN Revenue END) AS Apr_Revenue,
    SUM(CASE WHEN month = "May" THEN Revenue END) AS May_Revenue,
    SUM(CASE WHEN month = "Jun" THEN Revenue END) AS Jun_Revenue,
    SUM(CASE WHEN month = "Jul" THEN Revenue END) AS Jul_Revenue,
    SUM(CASE WHEN month = "Aug" THEN Revenue END) AS Aug_Revenue,
    SUM(CASE WHEN month = "Sep" THEN Revenue END) AS Sep_Revenue,
    SUM(CASE WHEN month = "Oct" THEN Revenue END) AS Oct_Revenue,
    SUM(CASE WHEN month = "Nov" THEN Revenue END) AS Nov_Revenue,
    SUM(CASE WHEN month = "Dec" THEN Revenue END) AS Dec_Revenue
FROM
    Department
GROUP BY
    id
