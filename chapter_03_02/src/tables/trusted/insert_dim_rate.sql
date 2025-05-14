INSERT INTO dim_rate (
    currency_code, valid_from, valid_to, currency_rate
)
SELECT
    currency_code,
    valid_from,
    valid_to,
    currency_rate
FROM staging.dim_rate;