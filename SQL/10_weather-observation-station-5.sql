-- Question Link
-- https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true

SELECT CITY , LENGTH(CITY) AS tamanho
FROM STATION
ORDER BY LENGTH(CITY) ASC, CITY ASC
LIMIT 1;

SELECT CITY , LENGTH(CITY) AS tamanho
FROM STATION
ORDER BY LENGTH(CITY) DESC, CITY ASC
LIMIT 1;
