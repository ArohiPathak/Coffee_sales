SELECT hour(datetime) AS hour, round(sum(money), 2) AS total_money
FROM coffee
GROUP BY hour(datetime)
ORDER BY hour(datetime) asc;
