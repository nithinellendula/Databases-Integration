**Project Title: Multi-Database Data Transfer Automation using Python**

**Objective:**
Developed a Python script that automates data transfer between three different relational database management systems (RDBMS): MySQL, PostgreSQL, and Oracle. The script dynamically connects to the selected source and destination databases, fetches data from a table, and inserts it into the corresponding table in the destination database.

**Project Overview:**
- **Databases Involved:**
  - MySQL (student table with preloaded data)
  - PostgreSQL (employee table with preloaded data)
  - Oracle (user_table with preloaded data)

- **Common Tables in Each Database:**
  - `student(sid, sname, saddress, marks)`
  - `employee(eid, ename, eaddress, salary)`
  - `user_table(u_id, uname, uaddress, user_contact)`

**Key Features:**
- Supports three database types: MySQL, PostgreSQL, and Oracle
- Dynamic source and destination configuration using user input
- Data fetching from the source database using parameterized SELECT queries
- Data insertion into the destination using parameterized INSERT queries with support for Oracle placeholder syntax
- Logs each row being inserted for debug/traceability
- Shows transferred data after completion for verification
- Handles database connection and operation errors gracefully

**Tools and Technologies:**
- Python 3
- `mysql-connector-python`
- `cx_Oracle`
- `psycopg2`
- VS Code (IDE)

**Sample Workflow:**
1. User runs the script
2. Inputs source and destination database types (e.g., source: mysql, destination: oracle)
3. Inputs the table name to be transferred (e.g., student)
4. Script fetches data from the specified source table
5. Script inserts data into the matching destination table
6. Final output prints inserted rows from destination

**Example Use Cases:**
- Migrating data between legacy systems
- Consolidating distributed data for reporting
- Syncing data across dev/test/staging environments

**Error Handling:**
- Catches and logs database-specific errors (e.g., connection failures, SQL syntax errors)
- Validates database type inputs
- Ensures connection and cursor cleanup with `finally` blocks

**Challenges Solved:**
- Dynamic handling of three different database APIs
- Managing data type and syntax compatibility
- Ensuring atomic operations with commits and rollbacks

**Next Steps:**
- Add GUI or CLI argument support for automation
- Implement data validation before insert
- Extend to support schema migration and column mapping
- Add logging to a file instead of console

---

**GitHub Repository:** https://github.com/nithinellendula/Databases-Integration.git
**Status:** Functional, tested across MySQL, PostgreSQL, and Oracle on localhost

**Author:** Nithin Ellendula