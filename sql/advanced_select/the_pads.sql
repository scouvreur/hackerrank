SELECT
    CONCAT(NAME, "(", LEFT(OCCUPATION, 1), ")")
FROM
    OCCUPATIONS
ORDER BY
    1 ASC
;

SELECT
    CONCAT("There are a total of ", tab.count, " ", LCASE(tab.OCCUPATION), "s.")
FROM (
    SELECT
        OCCUPATION,
        COUNT(*) AS count,
        CONCAT("There are a total of ", COUNT(*), " ", LCASE(OCCUPATION), "s.")
    FROM
        OCCUPATIONS
    GROUP BY
        OCCUPATION
    ORDER BY
        2 ASC,
        1 ASC
) tab
;
