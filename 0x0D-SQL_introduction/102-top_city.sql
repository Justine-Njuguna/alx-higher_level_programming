-- display the top 3 of temps of cities between July and Aug.

SELECT `city`, AVG(`value`) AS `avg_temp`

FROM `temperatures`

WHERE `month` = 7 OR `month` = 8

GROUP BY `city`

ORDER BY `avg_temp` DESC

LIMIT 3;
