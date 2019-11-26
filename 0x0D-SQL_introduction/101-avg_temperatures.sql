-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT `city`, SUM(`value`) / COUNT(*) AS "avg_temp" FROM temperatures GROUP BY `city` HAVING `avg_temp` > 0 ORDER BY `avg_temp` DESC;
