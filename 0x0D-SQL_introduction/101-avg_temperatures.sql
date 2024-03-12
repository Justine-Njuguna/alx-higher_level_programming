-- Displays temp in Farenh of by city ordered in desc order.

SELECT `city`, AVG(`value`) AS `avg_temp`

FROM `temperatures`

GROUP BY `city`

ORDER BY `avg_temp` DESC;
