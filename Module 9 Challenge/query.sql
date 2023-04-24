1 --List the employee number, last name, first name, sex, and salary of each employee (2 points)
SELECT e.emp_no, last_name, first_name, sex, salary
FROM employee e
	INNER JOIN salary s
		ON s.emp_no = e.emp_no;	
		
2 -- List the first name, last name, and hire date for the employees who were hired in 1986
SELECT first_name, last_name, hire_date
FROM employee where hire_date >= '1986-01-01' and hire_date <= '1986-12-31'
ORDER BY hire_date asc;

3 -- List the manager of each department along with their department number, department name, employee number, last name, and first name
SELECT d.dept_no, d.dept_name, e.emp_no,  e.last_name, e.first_name
FROM dept_manager dm
	INNER JOIN employee e 
		ON dm.emp_no = e.emp_no
	INNER JOIN department d
		ON dm.dept_no = d.dept_no; 

4 -- List the department number for each employee along with that employee’s employee number, last name, first name, and department name.
SELECT d.dept_no, d.dept_name, e.emp_no,  e.last_name, e.first_name
FROM dept_emp de
	INNER JOIN department d
		ON de.dept_no = d.dept_no
	INNER JOIN employee e 
	ON de.emp_no = e.emp_no;

5 -- List first name, last name, and sex of each employee whose first name is Hercules and whose last name begins with the letter B.
SELECT first_name, last_name, sex
FROM employee 
	WHERE first_name = 'Hercules' AND last_name LIKE 'B%';

6 -- List each employee in the Sales department, including their employee number, last name, and first name
SELECT 
SELECT emp_no, last_name, first_name
FROM public.employee
	WHERE emp_no IN
	(
		SELECT DISTINCT emp_no FROM public.dept_emp
		WHERE dept_no IN
		(
			SELECT dept_no FROM public.department WHERE 				dept_name = 'Sales'
		)
	);

SELECT emp_no, last_name, first_name
FROM public.employee
	WHERE emp_no IN
	(
		SELECT DISTINCT emp_no FROM public.dept_emp
		WHERE dept_no IN
		(
			SELECT dept_no FROM public.department WHERE dept_name = 'Sales'				
		)
	);

7 -- List each employee in the Sales and Development departments, including their employee number, last name, first name, and department name.
select e.emp_no, e.last_name, e.first_name, d.dept_name 
from employee e
	INNER JOIN dept_emp de
		ON de.emp_no = e.emp_no
	INNER JOIN department d
		ON d.dept_no = de.dept_no
	WHERE dept_name IN ('Sales', 'Development');

8 --List the frequency counts, in descending order, of all the employee last names (that is, how many employees share each last name) (4 points)
SELECT last_name, COUNT(last_name) AS frequency_count
FROM public.employee
	GROUP BY last_name
	ORDER BY frequency_count DESC;


