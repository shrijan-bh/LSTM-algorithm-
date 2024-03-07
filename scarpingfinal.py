import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd 

from datetime import datetime, timedelta

start_date = datetime(2014, 1, 1)
end_date = datetime(2024, 2, 13)

current_date = start_date
count=0
# =============================================================================
# while (current_date <= end_date):
#     # print(current_date.strftime('%Y-%m-%d'))
#     current_date += timedelta(days=1)
#     date =current_date.strftime('%Y-%m-%d')
# =============================================================================

csv_file = "outputdataset.csv"

url = 'https://kalimatimarket.gov.np/price'

headers = {
    'Host': 'kalimatimarket.gov.np',
    'Cookie': '_ga_EMKDTWG87G=GS1.1.1707906662.3.1.1707906765.0.0.0; _ga=GA1.3.573895635.1707743655; twk_uuid_62b413377b967b11799613cd=%7B%22uuid%22%3A%221.gNC9mWT2cUWmHsbAkhAL2mNYGD6ittCRYPytOFzJGa26fusRw37nQUcx1nkEZkGponXo7gqVITGvPdOGJqrBHQ2NDCxypenkCF6KapOhXJN5JuzlN8dg8hAKJ0kXcsnMO%22%2C%22version%22%3A3%2C%22domain%22%3A%22kalimatimarket.gov.np%22%2C%22ts%22%3A1707906767158%7D; _gid=GA1.3.158065559.1707898198; XSRF-TOKEN=eyJpdiI6InE1aTJqRUZOU2sxanROMUFLaHFzUHc9PSIsInZhbHVlIjoicUp1aEQ4cG5PNysycG14Qzhtb1JjbFlCUE9GS29mMWZGcjh1T1JXekswcFRnODlqa0VXM0VqT0F4TG0xSGtMcTRLR3hxaHVVVGpLQVdINk1ldnRBT1pJalloTFVnVkhSNWdHa3NHeU9WM3lnNGFvbURtRG53ZzhvTy9lT3JpUGgiLCJtYWMiOiJiZWE4ZDJiYWVkZTJhMGY0MzA3MTEyYzBiODg2MWFhMzkyYzYyYWQ2ZDU3Y2M5NzM1YmRlODQ5ODkyYTI0OWU0IiwidGFnIjoiIn0%3D; kalimati_fruits_and_vegetable_market_development_board_session=eyJpdiI6InFWR0QyUHJzdzJwZVZPekxKWEswb2c9PSIsInZhbHVlIjoieUF4RzU0U3J2THFrSDRQWStzQkZYbHNXdWlvR2puSWJmQ1Vhb2tncWJqQ2hwRVJVeDBVeDhhSVorb0VPM2FIV29HemQyMmR2OG0veFdBaVpHNEJ3VVNmMlZidENCOU12eW1rK25kTmRZRTd5ck1OUTZ2SmhTU2NzVi9oWU5RejYiLCJtYWMiOiIxZDVlZWI5YjhlZWE0ZGI0MDMwYThkYTQyZTlkZTA2MDczMWY2YWUzN2UyYjQ5NzQxZTgzNGQ3NTM1NzdlMTAyIiwidGFnIjoiIn0%3D; TawkConnectionTime=0; _gat_gtag_UA_231777614_1=1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '70',
    'Origin': 'https://kalimatimarket.gov.np',
    'Referer': 'https://kalimatimarket.gov.np/price',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Te': 'trailers',
}

while (current_date <= end_date):
    # print(current_date.strftime('%Y-%m-%d'))
    current_date += timedelta(days=1)
    date =current_date.strftime('%Y-%m-%d')
    count+=1

    data = {
        '_token': 'B4rIpGPLHWWwhA5YlEctHlmyC84HYJZoAkNy7Hsf',
        'datePricing': date,
    }
    for date in date:
        def response():
            response = requests.post(url, headers=headers, data=data)
            soup=BeautifulSoup(response.text, 'html.parser')
            table = []
            for row in soup.select("tr")[1:2]:
                table.append([td.get_text() for td in row.select("td")])
                column_names = [
                    td.get_text(strip=True) for td in soup.select_one("tr").select("th")
                    ]
            print(table)
            df = pd.DataFrame(table, columns=['Name', 'Category', 'Price 1', 'Price 2', 'Price 3'])
            csv_file = "output_pandas.csv"
            df.to_csv(csv_file, mode='a', header=False, index=False, encoding='utf-8')
    # =============================================================================
    #         with open(csv_file, mode='w', newline='' ,encoding='utf-8') as file:
    #             writer = csv.writer(file)
    #             writer.writerows(table)        
    # =============================================================================
    response()
        
    
print("done")
    
