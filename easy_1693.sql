SELECT
    date_id,
    make_name,
    COUNT(DISTINCT lead_id) AS unique_leads,
    COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name


-- optimize the codes
-- improve runtime but is harder to understand
WITH tbl1 AS (
    SELECT
    date_id,
    make_name,
    lead_id
    FROM DailySales
    GROUP BY 
    date_id,
    make_name,
    lead_id
),
tbl2 AS (
    SELECT
    date_id,
    make_name,
    partner_id
    FROM DailySales
    GROUP BY 
    date_id,
    make_name,
    partner_id
),
tbl3 AS (
    SELECT
    date_id,
    make_name,
    COUNT(lead_id) AS unique_leads
    FROM tbl1
    GROUP BY
    date_id,
    make_name
),
tbl4 AS (
    SELECT
    date_id,
    make_name,
    COUNT(partner_id) AS unique_partners
    FROM tbl2
    GROUP BY
    date_id,
    make_name
)

SELECT
t1.date_id AS date_id,
t1.make_name AS make_name,
t1.unique_leads AS unique_leads,
t2.unique_partners AS unique_partners
FROM tbl3 AS t1
JOIN tbl4 AS t2
USING(date_id, make_name)
