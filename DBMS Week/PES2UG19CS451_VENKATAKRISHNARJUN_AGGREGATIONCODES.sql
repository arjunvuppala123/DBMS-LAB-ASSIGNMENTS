Select fname as First_Name, lname as Last_Name,
salary as Old_Salary, 1.1*salary as New_Salary
From Employee E, Works_On W, Project P
Where E.ssn = W.essn and W.pno = P.pnumber
and P.pname='ProductX';

SELECT SUM (SALARY), MAX (SALARY), MIN (SALARY), AVG (SALARY)
FROM EMPLOYEE, DEPARTMENT
WHERE DNO = DNUMBER AND DNAME = 'Research';

select count(distinct salary) from employee;

SELECT LNAME, FNAME
FROM EMPLOYEE
WHERE (SELECT COUNT (*)
FROM DEPENDENT
WHERE SSN = ESSN) >= 2;

SELECT DNO, COUNT (*), AVG (SALARY)
FROM EMPLOYEE
GROUP BY DNO;


SELECT LNAME FROM EMPLOYEE WHERE SALARY >= 10000 +
( SELECT MIN(SALARY) FROM EMPLOYEE)

SELECT LNAME FROM EMPLOYEE WHERE DNO =
( SELECT DNO FROM EMPLOYEE WHERE SALARY =
( SELECT MAX(SALARY) FROM EMPLOYEE) )


select count(ssn) from employee where salary>=40000;

