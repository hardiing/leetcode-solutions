CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT MAX(salary) AS getNthHighestSalary
      FROM (
        SELECT salary, DENSE_RANK() OVER(ORDER BY salary DESC) AS sal_rank
        FROM Employee) t1
        WHERE sal_rank = N
        LIMIT 1
  );
END