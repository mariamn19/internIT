INSERT INTO dim_currency (
    currency_code, country, currency, font_code, font_arial, unicode_decimal, unicode_hex
)
SELECT
    currency_code,
    country,
    currency,
    font_code,
    font_arial,
    unicode_decimal,
    unicode_hex
FROM staging.dim_currency;