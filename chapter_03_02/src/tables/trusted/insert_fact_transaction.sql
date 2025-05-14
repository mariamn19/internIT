INSERT INTO fact_transaction (
    transaction_id, user_id, currency_id, rate_id, amount, currency_to, type, time
)
SELECT
    transaction_id,
    user_id,
    currency_id,
    rate_id,
    amount,
    currency_to,
    type,
    time
FROM staging.fact_transaction;