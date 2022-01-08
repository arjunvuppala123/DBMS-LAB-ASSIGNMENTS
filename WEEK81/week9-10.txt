CREATE TABLE EMPLOYEE(
empid int not null primary key,
name varchar(255),
phone_no varchar(20),
email varchar(20),
Dno int);

CREATE TABLE Department(
dno int not null primary key,
dnumber varchar(255),
no_of_emp int,
loc varchar(255));

create or replace function add_count() returns trigger as
$$
begin
update Department set no_of_emp = no_of_emp+1 where dno=new.dno;
return new;
end;
$$
language plpgsql;

create trigger add_num
  after insert on employee
  for each row
  execute procedure add_count();

create or replace function del_count() returns trigger as
$$
begin
 update Department set no_of_emp = no_of_emp-1 where dno=old.dno;
 return new;
end;
$$
language plpgsql;

create trigger del_num
  after delete on employee
  for each row
  execute procedure del_count();

create table order_summary(
order_id int,
no_of_items int,
unit_price int);

create table order_item(
item_id int not null primary key,
name varchar(255),
qty int,
unit_price int);

create or replace function add_ctr() returns trigger as
$$
begin
update order_summary set no_of_items = no_of_items+1 where order_id=new.order_id;
return new;
end;
$$
language plpgsql;


create trigger add_ctr
  after insert on order_item
  for each row
  execute procedure add_ctr();

create or replace function del_ctr() returns trigger as
$$
begin
 update order_summary set no_of_items = no_of_items-1 where order_id=old.order_id;
 return new;
end;
$$
language plpgsql;

create trigger del_ctr
  after delete on order_item
  for each row
  execute procedure del_ctr();
