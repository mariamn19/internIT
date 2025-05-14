import requests
import psycopg2

def extract_data():
    """ Extract data from the API Endpoint. """
    data = {}
    response = requests.get("https://open.er-api.com/v6/latest/RON")
    api_data = response.json()
    data["time_last_update_unix"] = api_data["time_last_update_unix"]
    data["time_next_update_unix"] = api_data["time_next_update_unix"]
    data["currency_code"] = list(api_data["rates"].keys())
    data["currency_rate"] = list(api_data["rates"].values())
    return data
def parse_data(input_data: dict, index: int):
    data = {}
    data["time_last_update_unix"] = input_data["time_last_update_unix"]
    data["currency_code"] = input_data["currency_code"][index]
    data["currency_rate"] = input_data["currency_rate"][index]
    return data

def load_data(data:list) -> None:
    """
    Connects to the PostgreSQL database and loads the extracted data into the specified table.
    """
    conn = psycopg2.connect(
        dbname="internit",
        user="postgres",
        password="Zaqwsxdc123",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    sql = """ 
    INSERT INTO raw.internit_data(
        time_last_update
    ,time_next_update_unix
    ,base_code
    ,currency_code
    ,currency_rate
    ) VALUES ( )
    """
    cursor.execute(sql, (
        data["time_last_update_unix"],
        data["time_next_update_unix"],
        data["currency_code"],
        data["currency_rate"]
    ))
    conn.commit()

    if __name__ == "__main__":
        api_data=extract_data()
        for index in range(list(api_data["currency_code"])):
            parsed_data = parse_data(api_data, index)
            load_data(parsed_data)
            
