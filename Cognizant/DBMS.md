# 🗄️ Database Management System (DBMS) Notes for Cognizant

> **Target:** Cognizant GenC / GenC Next, TCS, Infosys, Accenture, Capgemini, Wipro

---

# 1. What is DBMS?

A **Database Management System (DBMS)** is software used to create, store, retrieve, update, and manage data efficiently.

### Examples
- MySQL
- PostgreSQL
- Oracle
- SQL Server
- SQLite

---

# 2. Advantages of DBMS

- Reduces Data Redundancy
- Improves Data Security
- Data Consistency
- Backup & Recovery
- Concurrent Access
- Data Sharing

---

# 3. DBMS vs File System ⭐⭐⭐⭐⭐

| DBMS | File System |
|------|-------------|
| Data stored in tables | Data stored in files |
| Less redundancy | More redundancy |
| Better security | Less security |
| Supports transactions | No transactions |
| Easy backup | Difficult backup |

---

# 4. What is RDBMS?

**RDBMS (Relational DBMS)** stores data in the form of tables and maintains relationships using keys.

Examples:
- MySQL
- PostgreSQL
- Oracle

---

# DBMS vs RDBMS

| DBMS | RDBMS |
|------|--------|
| No relation required | Tables are related |
| Limited security | Better security |
| May not support keys | Supports Primary & Foreign Keys |

---

# 5. Database Schema

Schema is the logical structure of the database.

Example

```
Student

ID
Name
Age
Department
```

---

# 6. Instance

The actual data stored in the database at a specific moment.

---

# 7. Keys ⭐⭐⭐⭐⭐

## Primary Key

- Uniquely identifies each record.
- Cannot be NULL.
- Only one Primary Key per table.

Example

```
StudentID
```

---

## Foreign Key

Creates a relationship between two tables.

Example

```
Student.DepartmentID
```

---

## Candidate Key

A column that can become the Primary Key.

---

## Alternate Key

Candidate Key not chosen as Primary Key.

---

## Composite Key

Combination of multiple columns.

Example

```
(StudentID, CourseID)
```

---

## Super Key

Any set of columns that uniquely identifies a row.

---

# 8. Constraints

- PRIMARY KEY
- FOREIGN KEY
- UNIQUE
- NOT NULL
- CHECK
- DEFAULT

---

# 9. ER Diagram

ER = Entity Relationship Diagram

Components

- Entity
- Attribute
- Relationship

Example

```
Student ---- Enrolls ---- Course
```

---

# 10. Normalization ⭐⭐⭐⭐⭐

Normalization removes redundancy and improves consistency.

---

## 1NF

Rules

- Atomic values
- No repeating groups

---

## 2NF

Requirements

- Must satisfy 1NF
- No Partial Dependency

---

## 3NF

Requirements

- Must satisfy 2NF
- No Transitive Dependency

---

## BCNF

Every determinant must be a candidate key.

---

# Normal Forms Summary

| Form | Removes |
|------|----------|
| 1NF | Repeating groups |
| 2NF | Partial dependency |
| 3NF | Transitive dependency |
| BCNF | Candidate key violations |

---

# 11. ACID Properties ⭐⭐⭐⭐⭐

ACID ensures reliable transactions.

## Atomicity

Transaction happens completely or not at all.

---

## Consistency

Database remains valid before and after a transaction.

---

## Isolation

Multiple transactions do not interfere with each other.

---

## Durability

Committed data remains safe even after a crash.

---

# 12. Transaction

A transaction is a sequence of database operations executed as a single unit.

Example

```
Transfer ₹100

Debit A
Credit B
Commit
```

---

# Transaction States

- Active
- Partially Committed
- Committed
- Failed
- Aborted

---

# 13. Commit

Saves changes permanently.

```sql
COMMIT;
```

---

# 14. Rollback

Undoes changes.

```sql
ROLLBACK;
```

---

# 15. Savepoint

Creates a checkpoint inside a transaction.

```sql
SAVEPOINT sp1;
```

---

# 16. Index ⭐⭐⭐⭐⭐

An index speeds up data retrieval.

Advantages

- Faster SELECT queries

Disadvantages

- Slower INSERT, UPDATE, DELETE

---

# Types of Index

- Clustered Index
- Non-Clustered Index

---

# 17. View

A virtual table created using a SQL query.

```sql
CREATE VIEW EmpView AS
SELECT Name, Salary
FROM Employee;
```

---

# 18. Stored Procedure

A precompiled collection of SQL statements stored in the database.

Advantages

- Faster execution
- Reusable
- Secure

---

# 19. Trigger

A trigger automatically executes when an event occurs.

Events

- INSERT
- UPDATE
- DELETE

---

# 20. SQL Joins ⭐⭐⭐⭐⭐

---

## INNER JOIN

Returns matching rows.

```sql
SELECT *
FROM Student
INNER JOIN Department
ON Student.DeptID = Department.ID;
```

---

## LEFT JOIN

Returns all rows from the left table.

---

## RIGHT JOIN

Returns all rows from the right table.

---

## FULL OUTER JOIN

Returns all matching and non-matching rows.

---

## SELF JOIN

A table joined with itself.

---

# Join Comparison

| Join | Result |
|-------|--------|
| INNER | Matching rows |
| LEFT | All left + matching |
| RIGHT | All right + matching |
| FULL | All rows |

---

# 21. SQL Clauses

- SELECT
- FROM
- WHERE
- GROUP BY
- HAVING
- ORDER BY
- LIMIT

---

# 22. Aggregate Functions

- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()

---

# 23. GROUP BY

Groups rows having the same values.

```sql
SELECT DeptID, COUNT(*)
FROM Employee
GROUP BY DeptID;
```

---

# 24. HAVING

Filters grouped data.

```sql
SELECT DeptID, COUNT(*)
FROM Employee
GROUP BY DeptID
HAVING COUNT(*) > 5;
```

---

# 25. DELETE vs TRUNCATE vs DROP ⭐⭐⭐⭐⭐

| DELETE | TRUNCATE | DROP |
|----------|-----------|------|
| Removes selected rows | Removes all rows | Deletes table |
| WHERE allowed | WHERE not allowed | Table removed |
| Can rollback | Usually cannot rollback* | Cannot rollback |

\* Depends on the database system and transaction settings.

---

# 26. WHERE vs HAVING

| WHERE | HAVING |
|---------|---------|
| Filters rows | Filters groups |
| Before GROUP BY | After GROUP BY |
| Cannot use aggregate functions directly | Can use aggregate functions |

---

# 27. UNION vs UNION ALL

| UNION | UNION ALL |
|----------|------------|
| Removes duplicates | Keeps duplicates |
| Slower | Faster |

---

# 28. Subquery

A query inside another query.

Example

```sql
SELECT Name
FROM Employee
WHERE Salary >
(
SELECT AVG(Salary)
FROM Employee
);
```

---

# 29. CTE (Common Table Expression)

Makes complex queries easier to read.

```sql
WITH Temp AS
(
SELECT *
FROM Employee
)
SELECT *
FROM Temp;
```

---

# 30. Window Functions

- ROW_NUMBER()
- RANK()
- DENSE_RANK()

Example

```sql
SELECT Name,
Salary,
RANK() OVER (ORDER BY Salary DESC)
FROM Employee;
```

---

# Common SQL Interview Questions

### Second Highest Salary

```sql
SELECT MAX(Salary)
FROM Employee
WHERE Salary <
(
SELECT MAX(Salary)
FROM Employee
);
```

---

### Nth Highest Salary

Use `DENSE_RANK()` or nested subqueries.

---

### Duplicate Records

```sql
SELECT Name, COUNT(*)
FROM Employee
GROUP BY Name
HAVING COUNT(*) > 1;
```

---

### Employees Above Average Salary

```sql
SELECT *
FROM Employee
WHERE Salary >
(
SELECT AVG(Salary)
FROM Employee
);
```

---

# Frequently Asked Interview Questions

### Q1. What is DBMS?

A DBMS is software used to store, manage, and retrieve data efficiently.

---

### Q2. Difference between DBMS and RDBMS?

DBMS stores data, while RDBMS stores related data in tables using keys.

---

### Q3. What is a Primary Key?

A Primary Key uniquely identifies each row and cannot contain NULL values.

---

### Q4. What is a Foreign Key?

A Foreign Key links one table to another by referencing a Primary Key.

---

### Q5. What are ACID properties?

- Atomicity
- Consistency
- Isolation
- Durability

---

### Q6. Difference between DELETE, TRUNCATE, and DROP?

- **DELETE:** Removes selected rows.
- **TRUNCATE:** Removes all rows but keeps the table.
- **DROP:** Removes the entire table.

---

### Q7. What is Normalization?

Normalization organizes data to reduce redundancy and improve consistency.

---

### Q8. Difference between WHERE and HAVING?

- **WHERE:** Filters rows before grouping.
- **HAVING:** Filters groups after `GROUP BY`.

---

### Q9. What is an Index?

An Index improves query performance by allowing faster data retrieval.

---

### Q10. Difference between INNER JOIN and LEFT JOIN?

- **INNER JOIN:** Returns only matching rows.
- **LEFT JOIN:** Returns all rows from the left table and matching rows from the right.

---

# ⭐ Most Important Topics for Cognizant

- DBMS vs RDBMS
- Keys (Primary, Foreign, Candidate, Composite)
- Constraints
- Normalization (1NF, 2NF, 3NF, BCNF)
- ACID Properties
- Transactions
- COMMIT, ROLLBACK, SAVEPOINT
- Indexing
- Views
- Stored Procedures
- Triggers
- SQL Joins
- Aggregate Functions
- GROUP BY & HAVING
- WHERE vs HAVING
- DELETE vs TRUNCATE vs DROP
- UNION vs UNION ALL
- Subqueries
- CTE
- Window Functions
- Frequently Asked SQL Coding Questions