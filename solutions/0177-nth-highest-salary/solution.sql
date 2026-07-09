CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set n=n-1;
  RETURN (
      select(select distinct salary from Employee order by salary DESC LIMIT N,1)

  );
END
