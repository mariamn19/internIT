CREATE TABLE IF NOT EXISTS raw.exchange_data(
    time_last_update TIMESTAMP
    ,time_next_update_unix TIMESTAMP
    ,currency_code VARCHAR(3)
    ,currency_rate DECIMAL(10,6)
);