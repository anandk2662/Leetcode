CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
        select salary from (
            select
            salary,
            DENSE_RANK() OVER ( ORDER BY salary DESC) as saldescend
            from employee
        )
         as ranked_table
        where saldescend = N
        limit 1
  );
END