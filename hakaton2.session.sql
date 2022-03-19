-- 1
-- SELECT first_name, last_name from employees;
-- 2
-- select DISTINCT department_id from employees;
-- 3
-- SELECT * from employees ORDER by first_name DESC;
-- 4
-- SELECT first_name, last_name from employees ORDER by salary ASC;
-- 5
-- SELECT count(DISTINCT employee_id) count_employees from employees;
-- 6
-- SELECT first_name, last_name, salary from employees
-- where salary not BETWEEN 10000.00 and 15000.00;
-- 7
-- SELECT first_name, last_name from employees 
-- where hire_date BETWEEN '1987-01-01' and '1987-12-31'
-- 8
-- SELECT last_name, j.JOB_TITLE, salary from employees empl
-- inner join jobs j on j.job_id = empl.job_id
-- where j.job_id in ('IT_PROG', 'ST_CLERK', 'SH_CLERK')
-- and empl.salary not in(4500.00, 10000.00, 15000.00);
-- 9
-- SELECT last_name from employees
-- where last_name in('BLACK', 'Sckot', 'King', 'Ford');
-- 10
-- select sum(salary) salary from employees;
-- 11
-- select min(salary) min_salary from employees;
-- 12
-- select avg(salary) avg_salary from employees;
-- 13
-- select job_id, count(EMPLOYEE_ID) from employees
-- GROUP by job_id
-- 14
-- select avg(salary) avg_salary from employees
-- where job_id <> 'IT_PROG'
-- -15
-- SELECT l.LOCATION_ID, l.STREET_ADDRESS, l.CITY, l.STATE_PROVINCE,
-- c.COUNTRY_NAME
-- from employees empl
-- INNER JOIN departments d on d.DEPARTMENT_ID = empl.DEPARTMENT_ID
-- INNER JOIN locations l on d.LOCATION_ID = l.LOCATION_ID
-- INNER JOIN countries c on c.COUNTRY_ID = l.COUNTRY_ID
-- ;
--16
-- select d.Department_name, empl.last_name, empl.first_name from employees empl
-- inner join departments d on empl.department_id = d.department_id;
--17
-- select empl.last_name, empl.MANAGER_ID, man_empl.last_name from employees empl
-- inner join employees man_empl on man_empl.EMPLOYEE_ID = empl.MANAGER_ID;
--18
-- SELECT 
--     JOB_TITLE,
    
--     end_date - start_date
-- from job_history job
-- inner join jobs j on j.job_id = job.job_id
-- where department_id = 90
-- ;
--19
-- select d.department_name, empl.first_name, l.city from departments d
-- inner join employees empl on d.MANAGER_ID = empl.EMPLOYEE_ID
-- inner join locations l on l.LOCATION_ID = d.LOCATION_ID;
--20
select EXTRACT(year, from timestamp jh.start_date)
from departments d
inner join employees empl on d.MANAGER_ID = empl.EMPLOYEE_ID
inner join job_history jh on jh.EMPLOYEE_ID = empl.EMPLOYEE_ID


