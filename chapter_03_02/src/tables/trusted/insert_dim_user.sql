INSERT INTO dim_user (
    user_id, first_name, last_name, personal_number, birth_date, city, iban
)
SELECT
    user_id,
    first_name,
    last_name,
    personal_number,
    birth_date,
    city,
    iban
FROM staging.dim_user;