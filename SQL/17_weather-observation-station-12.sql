-- Question Link
-- https://www.hackerrank.com/challenges/weather-observation-station-12/problem?isFullScreen=true

SELECT DISTINCT CITY
FROM STATION
WHERE   CITY NOT REGEXP '^[AEIOUaeiou]'
    AND CITY NOT REGEXP '[AEIOUaeiou]$'
