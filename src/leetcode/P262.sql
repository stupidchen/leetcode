SELECT Request_at AS Day, ROUND(SUM(Status != "completed") / COUNT(*), 2) AS "Cancellation Rate"
FROM Trips
WHERE Client_Id not in (SELECT Users_Id FROM Users WHERE Banned = "Yes")
AND Driver_Id not in (SELECT Users_Id FROM Users WHERE Banned = "Yes")
AND Request_at >= "2013-10-01"
AND Request_at <= "2013-10-03"
GROUP BY Request_at
