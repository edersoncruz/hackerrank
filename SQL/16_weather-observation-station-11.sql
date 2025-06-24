-- Question Link
-- https://www.hackerrank.com/challenges/weather-observation-station-11/problem?isFullScreen=true

SELECT DISTINCT CITY
FROM STATION
WHERE   CITY NOT REGEXP '^[aeiouAEIOU]' 
    OR CITY NOT REGEXP '[aeiouAEIOU]$';
