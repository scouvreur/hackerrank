SELECT visited_on,
       ROUND(AVG(time_spent) OVER (ORDER BY visited_on ASC RANGE INTERVAL 2 DAY PRECEDING), 4)
FROM traffic
JOIN users ON traffic.user_id = users.id
WHERE users.user_type = 'user'
ORDER BY visited_on ASC;
