SELECT t1.name AS Employee
FROM Employee as t1
LEFT JOIN Employee as t2
    ON t1.managerId = t2.id
WHERE t1.salary > t2.salary;