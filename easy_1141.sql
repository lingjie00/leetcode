WITH tbl AS (
    SELECT DISTINCT
        activity_date,
        user_id
    FROM Activity
    WHERE activity_date > DATE_SUB("2019-07-27", INTERVAL 30 DAY) AND
        activity_date <= "2019-07-27"
)

SELECT
    activity_date AS day,
    COUNT(user_id) AS active_users
FROM tbl
GROUP BY activity_date
;
