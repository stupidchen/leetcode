SELECT d.Name AS Department, c.Name as Employee, c.Salary AS Salary
FROM (
    SELECT a.Name AS Name, a.DepartmentId AS DepartmentId, a.Salary AS Salary
    FROM Employee a
    INNER JOIN
        (SELECT DepartmentId, MAX(Salary) AS Salary FROM Employee GROUP BY DepartmentId) b
        ON a.DepartmentId = b.DepartmentId AND a.Salary = b.Salary
    ) c
INNER JOIN Department d
ON c.DepartmentId = d.Id