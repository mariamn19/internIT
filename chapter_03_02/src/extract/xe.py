import requests
from bs4 import BeautifulSoup

def crawl_data():
    response = requests.get("https://www.xe.com/symbols/")
    soup = BeautifulSoup(response.content, "html.parser")
    rows = soup.find_all("li", class_="sc-d9d8d44-8 knzHHe")
    data = []
    for row in rows:
        fields = row.find_all("div", class_="sc-d9d8d44-9 tlqHE")
        records={
            "country_and_currency": fields[0].get_text(strip=True),
            "currency_code": fields[1].get_text(strip=True),
            "font_code": fields[2].get_text(strip=True),
            "font_arial": fields[3].get_text(strip=True),
            "unicode_decimal": fields[4].get_text(strip=True),
            "unicode_hex": fields[5].get_text(strip=True),
        }
        data.append(records)
    return data


if __name__ == "__main__":
    data = crawl_data()
    for row in data:
        print(row)