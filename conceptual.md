### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
It's a relational database management system using SQL.


- What is the difference between SQL and PostgreSQL?
- SQL is a database management language not a rlational database system. PostgrSQL is a relational database managemnt system that has a variety of features to allow you to manage databases in applications.

- In `psql`, how do you connect to a database?
- psql -d *database name*

- What is the difference between `HAVING` and `WHERE`?
- WHERE is used to select individual rows to decide whether or not they meet the selected criteria. HAVING is used to apply conditions to grouped results.

- What is the difference between an `INNER` and `OUTER` join?
- Inner joins join tables based on matching data existing on both tables. Outer joins return all rows from one table
- and matching rows from the other table. And tif they don't have have a match, the row will show NULL values

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
-Left Outer join return all rows from the left table and only matching ones from the right one.
-Right Outer join return all rows from the right table and only matching ones from the left one.


- What is an ORM? What do they do?
- ORMS allow you to work with database data using object oriented programming with classes and objects. 

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
AJAX is asynchronous and can be used to create responsive user interfaces and change information on the browser. Requests is used to get information from servers, update servers, and used in back end development.


- What is CSRF? What is the purpose of the CSRF token?
- Cross Site Request Forgery Token is used to secure websites from attackers trying to make unauthorized or malicious requests from outside the site. A CSRF token is generated when a user logs in and is checked when the user submits a form or makes a request to make sure the request isn't being made from an unknown or unwanted source.

- What is the purpose of `form.hidden_tag()`?
A function in a WTForms form that allows you to include data that needs to be sent with the form but that should not be visible to the user. USed to include a field ontaining a CSRF token.