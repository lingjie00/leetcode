UPDATE
    Salary
SET
    sex = CASE WHEN sex = "m" THEN "f" ELSE "m" END
;

-- using IF
UPDATE
    Salary
SET
    sex = IF(sex = "m", "f", "m")
;
