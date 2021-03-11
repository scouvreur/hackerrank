SELECT DISTINCT CITY
FROM STATION
WHERE LCASE(LEFT(CITY, 1)) NOT IN ('a', 'e', 'i', 'o', 'u')
   OR LCASE(RIGHT(CITY, 1)) NOT IN ('a', 'e', 'i', 'o', 'u');
