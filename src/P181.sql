select A.Name as Employee from Employee A, Employee B where A.managerId = B.Id and A.Salary > B.Salary