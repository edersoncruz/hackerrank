-- Question Link
-- https://www.hackerrank.com/challenges/weather-observation-station-4/problem?isFullScreen=true

select(
    (select count(city)
from station)
-
    (select count(distinct city)
from station)

)
