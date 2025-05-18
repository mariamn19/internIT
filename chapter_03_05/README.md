# Data Governance

This chapter introduces interns to the principles and practices of data governance, focusing on data privacy, lifecycle management, quality assurance, and security. Interns will work with both PII (Personally Identifiable Information) and non-PII datasets to understand how to manage sensitive data responsibly.

## 📚 Resources

- [What is a database administrator (DBA)? – Oracle India](https://www.oracle.com/in/database/what-is-a-database-administrator/)
- [Roles and Responsibilities of Database Administrator](https://data-flair.training/blogs/database-administrator-responsibilities/)
- [Database Life Cycle – Informatics](https://informatics.nic.in/database-life-cycle/)
- [The Most Popular Databases for 2022](https://db-engines.com/en/ranking)
- [Database Administrator Roles & Responsibilities in The Big Data Age – BMC Software](https://www.bmc.com/blogs/database-administrator-dba/)

## To do list

- Create and populate both PII and non-PII versions of a dataset.
- Implement data archiving and deletion logic.
- Validate data quality by enforcing constraints and filtering out incomplete records.
- Review and document data access policies and security practices.

## Create non-PII / PII data

Create two versions of the same dataset: `data_nonpii` – A sanitized version without sensitive information, `data_pii` – A version containing personally identifiable information.

### Create non-PII data

To create non-PII version of the table data_nonpii use the code from `src/create_data_nonpii.sql` file. To insert non-PII data to the table use the code from `src/insert_data_nonpii.sql` file. To select non-PII data from the table use the code from `src/select_data_nonpii.sql` file.

### Create PII data

To create PII version of the table `data_pii` use the code from `src/create_data_nonpii.sql` file. To insert PII data to the table use the code from `src/insert_data_pii.sql` file. To select PII data from the table use the code from `src/select_data_pii.sql` file.

## Establish data life cycle

Implement data lifecycle management by archiving and purging old records from the `dim_rate` table. To create archive version of the data for `dim_rate` table use the code from `src/create_archive_rate.sql` file. To delete archived data from `dim_rate` table use the code from `src/delete_dim_rate.sql` file. To select archived data from `dim_rate_archive` table use the code from `src/select_current_rate.sql` file.

## Measure data quality

Ensure data quality by updating insert scripts to exclude records with NULL values. Use src/insert_data_nonpii.sql and src/insert_data_pii.sql files to ensure data quality by removing records that contain NULL values.

## Check data security

Review and apply data access policies as outlined in chapter_03_04, focusing on role-based access control and schema-level permissions.
