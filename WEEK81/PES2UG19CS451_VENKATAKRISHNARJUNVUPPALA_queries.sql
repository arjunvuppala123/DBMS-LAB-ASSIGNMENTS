select lname,fname
from employee
where (select count(*)
from dependent
where ssn=essn)>=2;

select e.fname,e.lname
from employee as e
where e.ssn in (select essn
from dependent
where e.fname = dependent_name and e.gender = gender);

select fname,lname
from employee
where salary > (select salary from employee where dno=5 and salary=40000);

select fname,lname
from employee
where not exists (select * from dependent where ssn=essn);

select fname,lname
from employee
where exists (select * from dependent where ssn=essn) and exists (select * from department where ssn=mgr_ssn);

select e.fname,e.lname,e.address
from employee e
join department d on d.dnumber = e.dno
where d.dname = 'Research';