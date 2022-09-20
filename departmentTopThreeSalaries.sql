SELECT dept.name AS Department, emp.name AS Employee, salary AS Salary
FROM Employee emp LEFT JOIN Department dept
ON emp.departmentId = dept.id
WHERE
(SELECT COUNT(DISTINCT salary) FROM Employee t1
      WHERE t1.departmentId = dept.id AND t1.salary >= emp.salary) <= 3
      AND dept.name IS NOT null
ORDER BY dept.id DESC;