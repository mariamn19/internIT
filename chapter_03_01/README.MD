# Data Warehousing

## Scenario

You are a Data Engineer in the InternIT company. The InternIt company is a Romanian StartUp **in online banking** and offers banking services for the customers.

## Business requirements

InternIT company provides financial platform for consultancy transactions for their customers.

## Core Business Goals

1. **Crypto currencies analysis** - Aggregate currencies evolution.
2. **Crypto currencies insights** - Track trends in  currencies demand.
3. **Prices trends** - Provide brenchmarks for different  currencies.
4. **Crypto currencies popularity** - Determine which  currencies are most in demand.

## Reports

Buy Transactions by currency.\
Sell Transactions by currency.\
Price Evolution of top 10 currencies vs InterCoin.

### DashBoards

Current RON price vs other currencies
Maximum and minimum price on current day
Historical price evolution of the InterCoin.

#### KPIs

Total currencies transactions.\
Average transaction amount.\
Top 10 amount transactions on buy.\
Top 10 amount transaction on sell.

## Data Warehouse Design

It has a server InternIT and a database named 'internit_db'.

### Sources

The data sources for the company are:

- InternIt - Own Platform data.
- [ExchangeRate](https://www.exchangerate-api.com/) - Partner Platform for today traditional currencies rates.
- [XE](https:/www.xe.com/symbols/) - Partner Platform for currencies names and symbols.

#### InternIT source

`internit_data`

| Column Name | Data Type | Description |
|-----|-----|-----|
| transaction_id | INT | Unique identifier of the transaction |
| first_name | VARCHAR(255) | Customer firt name |
| last_name | VARCHAR(255) | Customer last name |
| user_id | VARCHAR(20) | Platform user identifier name |
| personal_nuber | VARCHAR(13) | Personal numerical identifier |
| birth_date | TIMESTAMP | Birth date |
| city | VARCHAR(50) | User's city |
| iban | INT | Bank account number |
| amount | DECIMAL | Amount of  money of the transaction |
| currency | VARCHAR(3) | Currency code used in the transaction |
| currency_to | VARCHAR(3) | Currency code in exchange transaction|
| type | VARCHAR(15) | Type of the transaction |
| timestamp | TIMESTAMP | Date of transaction |

### Exchange source

`exchange_data`

| Column Name | Data Type | Description |
|-----|-----|-----|
| time_last_update_unix | TIMESTAMP | Unix timestamp from when data are available |
| time_next_update_unix | TIMESTAMP | Unix timestamp when when data are available |
| currency_code | VARCHAR(3) | Standard currency code |
|currency_rate | DECIMAL | price of the currency vs reference currency |

#### XE source

`xe_data`

| Column Name | Data Type | Description |
|-----|-----|-----|
| county_and_currency | VARHCAR(3) | COuntry and their currency name |
| currency_code | VARCHAR(3) | STandard currency code |
| font_Code | TEXT | Symbol of the currency in Code 2000 |
|font_arial| TEXT | Symbl of the currency in Arial |
| unicode_decimal | TEXT | Decimal unicode of the currency |
|unicode_hex | TEXT | Hex unicode of the currency |

## Resources

- [What is a Data Warehouse? by IBM](https://www.ibm.com/think/topics/data-warehouse)
- [Evolution of the Modern Data Warehouse by Paige Roberts on Medium](https://medium.com/@paigeonthewing/evolution-of-the-modern-data-warehouse-f8b8d616149d)
- [Top 6 Data Warehouses and Best Picks for a Modern Data Stack on Weld Blog](https://weld.app/blog/top-5-data-warehouses)
- [Data Lake vs Data Warehouse vs Data Mart - Difference Between Cloud Storage Solutions by AWS](https://aws.amazon.com/compare/the-difference-between-a-data-warehouse-data-lake-and-data-mart/)
- [OLAP vs. OLTP: The Differences by Snowflake](https://www.snowflake.com/guides/olap-vs-oltp)
- [Data Warehouse Concepts: Kimball vs. Inmon Approach on Astera](https://www.astera.com/type/blog/data-warehouse-concepts/)
