CREATE DATABASE capstone_sql;
USE capstone_sql;
CREATE TABLE students (
student_id INT PRIMARY KEY,
student_name VARCHAR(100),
city VARCHAR(50),
age INT
);
CREATE TABLE enrollments (
enrollment_id INT PRIMARY KEY,
student_id INT,
course_name VARCHAR(100),
trainer VARCHAR(100),
fee DECIMAL(10,2)
);
INSERT INTO students VALUES
(1,'Aarav Sharma','Hyderabad',22),
(2,'Priya Reddy','Bangalore',23),
(3,'Rahul Verma','Mumbai',24),
(4,'Sneha Kapoor',NULL,21),
(5,'Vikram Singh','Chennai',25),
(6,NULL,'Delhi',22);
INSERT INTO enrollments VALUES
(101,1,'MySQL','Abdullah Khan',5000),
(102,1,'Python','Abdullah Khan',7000),
(103,2,'Power BI','Kiran',6000),
(104,3,'Azure Data Factory','Sneha',8000),
(105,NULL,'Excel','Rohan',3000),
(106,8,'Databricks','Ananya',9000);

-- capstone exercises
-- 1
select s.student_name, e.course_name from students s
inner join enrollments e on s.student_id = e.student_id;

-- 2
select s.student_name, e.course_name from students s
left join enrollments e on s.student_id = e.student_id;

-- 3 
select s.student_name, e.course_name from students s
right join enrollments e on s.student_id = e.student_id;

-- 4
select s.student_name, e.course_name from students s left join enrollments e on s.student_id = e.student_id
union
select s.student_name, e.course_name from students s right join enrollments e on s.student_id = e.student_id;

-- 5 
select s.student_name, e.course_name from students s
cross join enrollments e;

-- 6 
select s.student_name, e.course_name from students s
join enrollments e on s.student_id = e.student_id
where s.city = 'Hyderabad';

-- 7 
select course_name, fee from enrollments 
where fee > 6000;

-- 8 
select student_id, count(course_name) as total_courses from enrollments
group by student_id;

-- 9
select student_id, sum(fee) as total_paid from enrollments
group by student_id;

-- 10 
select student_id, count(course_name) from enrollments 
group by student_id 
having count(course_name) > 1;

-- 11
select trainer, sum(fee) from enrollments 
group by trainer 
having sum(fee) > 10000;

-- 12 
select city, count(student_id) from students 
group by city 
having count(student_id) > 1;

-- 13
select s.student_name, s.city, sum(e.fee) as total_fee_paid
from students s
join enrollments e on s.student_id = e.student_id
group by s.student_name, s.city
having sum(e.fee) > 5000
order by total_fee_paid desc;
