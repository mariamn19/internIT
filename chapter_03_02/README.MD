# Architecture of Data Warehousing and Normalization

## Architecture of Data Warehousing

In `intinit_db` database are created 3 layers:

* **raw** --> source data
* **staging** --> transformed data
* **trusted** --> consumption data

### Raw layer

#### Create layer

To create `raw` layer use the SQL query from `src/schemas/raw.sql` file.

#### Create table

**intinit_data**\
To create internit_data table use the code from src/tables/raw/create_internit_table.sql file.

**exchange_data**\
To create exchange_data table use the code from src/tables/raw/create_exchange_table.sql file.

**xe_data**\
To create xe_data table use the code from src/extract/src/tables/raw/create_xe_table.sql file.

#### Insert data

**intinit_data**\
To extract data for `intinit_data` table use the code from `src/tables/raw/insert_internit_table.sql` file.

**exchange_data**\
To extract data for `exchange_data` table use the code from `src/tables/raw/insert_exchange_table.sql` file.

**xe_data**\
To extract data for `xe_data` table use the code from `src/extract/src/tables/raw/insert_xe_table.sql` file.

#### Select data

**intinit_data**\
To select data from internit_data table use the code from src/tables/raw/select_internit_table.sql file.

**exchange_data**\
To select data from exchange_data table use the code from src/tables/raw/select_exchange_table.sql file.

**xe_data**\
To select data from xe_data table use the code from src/extract/src/tables/raw/select_xe_table.sql file.

### Staging layer

#### fact_transaction

| Column Name    | Data Type         | Description                                |
|----------------|-------------------|--------------------------------------------|
| transaction_id | VARCHAR(50)       | PRIMARY KEY - raw/internit_data/transaction_id |
| user_id        | VARCHAR(20)       | FOREIGN KEY - raw/internit_data/user_id    |
| currency_id    | VARCHAR(3)        | FOREIGN KEY - raw/xe_data/currency_code    |
| rate_id        | VARCHAR(3)        | FOREIGN KEY - raw/exchange_data/currency_code |
| amount         | INT               | raw/internit_data/amount                   |
| currency_to    | VARCHAR(3)        | raw/internit_data/currency_to             |
| type           | VARCHAR(15)       | raw/internit_data/type                     |
| time           | TIMESTAMP         | raw/internit_data/time                     |

### dim_user

| Column Name     | Data Type     | Description                             |
|-----------------|---------------|-----------------------------------------|
| user_id         | VARCHAR(20)   | PRIMARY KEY - raw/internit_data/user_id |
| first_name      | VARCHAR(255)  | raw/internit_data/first_name            |
| last_name       | VARCHAR(255)  | raw/internit_data/last_name             |
| personal_number | INT           | raw/internit_data/personal_number       |
| birth_date      | DATE          | raw/internit_data/birth_date            |
| city            | VARCHAR(50)   | raw/internit_data/city                  |
| iban            | VARCHAR(25)   | raw/internit_data/iban                  |

### dim_rate

| Column Name   | Data Type | Description                                   |
|---------------|-----------|-----------------------------------------------|
| currency_code | VARCHAR(3) | PRIMARY KEY - raw/exchange_data/currency_code |
| valid_from    | TIMESTAMP | raw/exchange_data/time_last_update_unix       |
| valid_to      | TIMESTAMP | raw/exchange_data/time_next_update_unix       |
| currency_rate | DECIMAL   | raw/exchange_data/currency_rate               |

### dim_currency

| Column Name     | Data Type   | Description                               |
|------------------|-------------|-------------------------------------------|
| currency_code    | VARCHAR(3)  | PRIMARY KEY - raw/xe_data/currency_code   |
| country          | VARCHAR(50) | raw/xe_data/country_and_currency          |
| currency         | VARCHAR(50) | raw/xe_data/country_and_currency          |
| font_code        | TEXT        | raw/xe_data/font_code                     |
| font_arial       | TEXT        | raw/xe_data/font_arial                    |
| unicode_decimal  | TEXT        | raw/xe_data/unicode_decimal               |
| unicode_hex      | TEXT        | raw/xe_data/unicode_hex                   |

### Trusted layer

## Normalization

....To be reviewed...

For normalization operation use Star Schema presented in src/star_schema.drawio that can be viewed in VS Code or using [Drawio in browser](https://www.drawio.com/).

For normalization, we apply the **Star Schema** methodology, which structures data into **fact** and **dimension** tables to improve query performance and eliminate redundancy.

You can view the schema diagram in the `src/star_schema.drawio` file using Visual Studio Code (with the Draw.io plugin) or directly in the [Draw.io online editor](https://app.diagrams.net/).

### Create tables

To create the normalized tables, use the SQL scripts provided in the following paths:

**fact_transaction**  
  Use: `src/tables/trusted/create_fact_transaction.sql`

**dim_user**  
  Use: `src/tables/trusted/create_dim_user.sql`

**dim_currency**  
  Use: `src/tables/trusted/create_dim_currency.sql`

**dim_rate**  
  Use: `src/tables/trusted/create_dim_rate.sql`

### Insert data into Trusted Layer

To populate the trusted layer tables with cleaned and transformed data from the **staging layer**, use the following scripts:

**fact_transaction**  
  Use: `src/tables/trusted/insert_fact_transaction.sql`

**dim_user**  
  Use: `src/tables/trusted/insert_dim_user.sql`

**dim_currency**  
  Use: `src/tables/trusted/insert_dim_currency.sql`

**dim_rate**  
  Use: `src/tables/trusted/insert_dim_rate.sql`

### Select data for Trusted Layer

You can validate the data and perform analysis by querying each table using:

**fact_transaction**  
  Use: `src/tables/trusted/select_fact_transaction.sql`

**dim_user**  
  Use: `src/tables/trusted/select_dim_user.sql`

**dim_currency**  
  Use: `src/tables/trusted/select_dim_currency.sql`

**dim_rate**  
  Use: `src/tables/trusted/select_dim_rate.sql`

## Resources

[Data Warehouse Architecture Layers, Principles & Practices to Know on StreamSets](https://streamsets.com/blog/data-warehouse-architecture/)\
[Modern Data Warehouses: Functions, Architecture, & Examples on Estuary](https://www.estuary.dev/modern-data-warehouse/)\
[How to evaluate and optimize data warehouse performance on TechTarget](https://www.techtarget.com/searchdatamanagement/tip/How-to-evaluate-and-optimize-data-warehouse-performance)\
[What is Normalization in DBMS (SQL)? 1NF, 2NF, 3NF Example on guru99.com](https://www.guru99.com/database-normalization.html)\
[The Problem of Redundancy in Database on GeeksforGeeks](https://www.geeksforgeeks.org/redundancy-in-databases/)\
[Anomalies in Relational Model on GeeksforGeeks](https://www.geeksforgeeks.org/anomalies-in-dbms/)\
[Data Cleaning Challenge: Scale and Normalize Data on Kaggle](https://www.kaggle.com/code/residentmario/data-cleaning-challenge-scale-and-normalize-data)
