(SELECT DISTINCT PNUMBER 
FROM PROJECT, DEPARTMENT, EMPLOYEE 
WHERE DNUM = DNUMBER AND mgr_ssn = SSN AND LNAME = 'Smith')
UNION
(SELECT DISTINCT PNUMBER FROM PROJECT, WORKS_ON, 
EMPLOYEE 
WHERE PNUMBER = PNO AND ESSN = SSN AND LNAME = 'Smith');

select fname,lname
from employee
where not exists (select * from dependent where ssn=essn);

select ssn from employee where dno=5
union select super_ssn from employee
where dno=5;

select pnumber from project where dnum=5
intersect
select pno from works_on where essn='123456789';

select ssn
from employee
where dno=5
except
(select dlocation from dept_locations where dlocation='bellaire');

select fname from employee
intersect
select dependent_name from dependent;
