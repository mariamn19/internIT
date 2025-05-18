# 🛡️ Database Administration

This chapter introduces interns to essential database administration tasks within the `internit_db` PostgreSQL database. Interns will learn how to manage user roles, optimize performance, and prepare data for dashboards and reports.

## 📚 Resources

- [What is a database administrator (DBA)? – Oracle India](https://www.oracle.com/in/database/what-is-a-database-administrator/)
- [Roles and Responsibilities of Database Administrator](https://data-flair.training/blogs/database-administrator-responsibilities/)
- [Database Life Cycle – Informatics](https://informatics.nic.in/database-life-cycle/)
- [The Most Popular Databases for 2022](https://db-engines.com/en/ranking)
- [Database Administrator Roles & Responsibilities in The Big Data Age – BMC Software](https://www.bmc.com/blogs/database-administrator-dba/)

## ✅ To Do List

- Create and assign roles with appropriate permissions.
- Use `EXPLAIN` to analyze query performance and suggest optimizations.
- Generate and export data for dashboards using Python and SQL.
- Document access control policies and performance tuning strategies.

## 🔐 Create DBA Roles

Create and manage roles with specific access rights to ensure secure and controlled data access. To create 'de_role' and grant access to 'trusted' schema and 'top_10_currencies' view use the code from 'src/role/grant_usage_schema.sql' and 'src/roles/grant_select_table.sql ' files.

## Optimize DB perofomance

Analyze and optimize SQL queries using PostgreSQL’s EXPLAIN and ANALYZE tools to understand query plans and improve performance. To check query execution performance use the code from 'src/roles/explain_query_execution.sql' file.

## Create Reports and Dashboard data

Generate data for dashboards and reports that support InternIT’s business goals, such as currency trends and transaction summaries. To create dashboard use the code from 'src/dashboard/internit_dashboard.py' file.
