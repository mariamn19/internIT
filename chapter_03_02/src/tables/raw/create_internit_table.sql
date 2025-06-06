CREATE TABLE IF NOT EXISTS raw.internit_data(
    transaction_id VARCHAR(50)
    ,first_name VARCHAR(255)
    ,last_name VARCHAR(255)
    ,user_id VARCHAR(20)
    ,personal_number BIGINT
    ,birth_date DATE
    ,city VARCHAR(50)
    ,iban VARCHAR(50)
    ,amount DECIMAL(10,2)
    ,currency_code VARCHAR(3)
    ,currency_to VARCHAR(3)
    ,type VARCHAR(50)
    ,time TIMESTAMP
)