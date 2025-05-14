CREATE TABLE IF NOT EXISTS trusted.fact_transaction (
    transaction_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(20),
    currency_id VARCHAR(3),
    rate_id VARCHAR(3),
    amount INT,
    currency_to VARCHAR(3),
    type VARCHAR(15),
    time TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES dim_user(user_id),
    FOREIGN KEY (currency_id) REFERENCES dim_currency(currency_code),
    FOREIGN KEY (rate_id) REFERENCES dim_rate(currency_code)
);