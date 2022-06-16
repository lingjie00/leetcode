-- using SUBSTRING
SELECT
    user_id,
    CONCAT(
        UPPER(LEFT(name, 1)),
        LOWER(SUBSTRING(name, 2))
    ) AS name
FROM
    Users
ORDER BY
    user_id
;

-- using CHAR_LENGTH
SELECT
    user_id,
    CONCAT(
        UPPER(LEFT(name, 1)),
        LOWER(RIGHT(name, CHAR_LENGTH(name)-1))
    ) AS name
FROM
    Users
ORDER BY
    user_id
;

