create database FIFA_WC;

use FIFA_WC;

create table Sales(
ID int primary key,
Customer varchar(100),
Quantity int,
Price int,
Category varchar(30),
Discount varchar(10),
Date varchar(20)
);

SELECT user FROM mysql.user;

select * from Sales;

insert into Sales values (
1, "Nvidia", 30, 1500, "Semiconductor", "10%", "2025-04-07"
);

insert into Sales values (
2, "Lockheed Martin", 30, 150000, "Jets", "20%", "2024-04-07"
);
insert into Sales values (
3, "Apple", 100, 1000, "Crystal Glass Display", "10%", "2026-04-07"
);

create table Product (
Prod_ID int primary key,
Product varchar(10000),
Serial_No int,
Price decimal(20, 2)
);

insert into Product values(
1, "Blackwell H-100", 136700100, 2500.20);

select * from Product;

ALTER USER 'root'@'localhost' 
IDENTIFIED WITH mysql_native_password 
BY 'yourSQLpwd';
