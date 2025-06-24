-- Question Link
-- https://www.hackerrank.com/challenges/weather-observation-station-8/problem?isFullScreen=true

SELECT DISTINCT CITY
FROM STATION
WHERE 
    city REGEXP '^[AEIOUaeiou]'     
AND city REGEXP '[AEIOUaeiou]$';    
