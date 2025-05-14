CREATE TABLE IF NOT EXISTS trusted.dim_rate (
    currency_code VARCHAR(3) PRIMARY KEY,
    valid_from TIMESTAMP,
    valid_to TIMESTAMP,
    currency_rate DECIMAL
);