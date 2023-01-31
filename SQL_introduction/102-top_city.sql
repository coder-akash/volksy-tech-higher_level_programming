-- script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT TOP 3 city, AVG(value) as avg_temp
FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city
ORDER BY AVG(value) DESc;
