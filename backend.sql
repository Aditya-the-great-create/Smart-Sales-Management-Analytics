create database FIFA_WC;

use FIFA_WC;

DROP TABLE Sales;

CREATE TABLE Sales (
    ID INT PRIMARY KEY,
    Customer VARCHAR(100),
    Product VARCHAR(100),
    Quantity INT,
    Price FLOAT
);

SELECT user FROM mysql.user;

select * from Sales;

describe sales;

SELECT DATABASE();

insert into Sales values (
1, "Nvidia", "H-100 Chips", 30, 1500
);

insert into Sales values (
2, "Lockheed Martin", "F-35 Lightning II", "30", 150000
);
insert into Sales values (
3, "Apple", "A-16 Chips", 100, 1000
);


ALTER USER 'root'@'localhost' 
IDENTIFIED WITH mysql_native_password 
BY 'your_pwd';
