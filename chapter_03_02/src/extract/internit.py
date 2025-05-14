from faker import Faker
import random
import psycopg2

def generate_synthetic_data() -> list:
    """Generate synthetic data for testing purposes."""
    synthetic = Faker("ro_RO")

    transaction_id = synthetic.uuid4()
    first_name = synthetic.first_name()
    last_name = synthetic.last_name()
    user_id = synthetic.user_name()
    personal_number = synthetic.ssn()
    birth_date = synthetic.date_of_birth(None, 18, 100)
    city = synthetic.city()
    iban = synthetic.iban()
    amount = synthetic.random_int(min=1, max=1000000)
    currency_code = synthetic.currency_code()
    currency_to = synthetic.currency_code()
    type = random.choice(["exchange", "pay", "transfer"])
    time = synthetic.date_time_between("-1y", "now")
    
    return {
        transaction_id, first_name, last_name, user_id, personal_number,
        birth_date, city, iban, amount, currency_code, currency_to, type, time
    }

def load_data():
    """
    """
    conn = psycopg2.connect(
        dbname="internit",
        user="postgres",
        password="Zaqwsxdc123",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    data = generate_synthetic_data()
    sql="""
INSERT INTO raw.internit_data(
    transaction_id
    ,first_name
    ,last_name
    ,user_id
    ,personal_number
    ,birth_date
    ,city
    ,iban
    ,amount
    ,currency_code
    ,currency_to
    ,type
    ,time
) VALUES (
    %s
    ,%s
    ,%s 
    ,%s
    ,%s
    ,%s
    ,%s
    ,%s
    ,%s
    ,%s
    ,%s
    ,%s
    ,%s
);"""
    cursor.execute(
    sql, (
    data[0],
    data[1],
    data[2],
    data[3],
    data[4],
    data[5],
    data[6],
    data[7],
    data[8],
    data[9],
    data[10],
    data[11],
    data[12]
        )
    )
    conn.commit()


if __name__ == "__main__":
    for _ in range(100):
        synthetic_data = generate_synthetic_data()
        load_data(synthetic_data)
