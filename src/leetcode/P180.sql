SELECT DISTINCT a.Num AS ConsecutiveNums FROM Logs a
WHERE (SELECT COUNT(*) FROM Logs b WHERE b.Id IN (a.Id + 1, a.Id + 2) AND b.Num = a.Num) >= 2