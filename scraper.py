import requests
from bs4 import BeautifulSoup

url = "https://kalimatimarket.gov.np/price#"

r=requests.get(url)
htmlcontent=r.content
soup = BeautifulSoup(htmlcontent, 'html.parser')
headers = {
 
}


data = {
    "_token": "9slDhETlgGng6kfAR6inODZD07MaC9J2UH1MYjNd",
    "datePricing": "2024-02-01",
}

response = requests.get(url,headers=headers,data=data)



# =============================================================================
# 
# desired_string ="गोलभेडा"
# # Assuming the second column is the one you want to check
# table=[]
# for row in soup.select("tr")[2:]:
#     cells = row.select("td")
#     
#     # Check if the desired string is in the second column (index 1)
#     if len(cells) > 1 and desired_string in cells[1].get_text():
#         table.append([td.get_text() for td in cells])
# 
# =============================================================================


# =============================================================================
# table = []
# for row in soup.select("tr")[1:]:
#     table.append([td.get_text() for td in row.select("td")])
# 
# column_names = [
#     td.get_text(strip=True) for td in soup.select_one("tr").select("th")
# ]
# 
# #print(column_names)
# print(table)
# 
# =============================================================================

print (response.text)
# =============================================================================
# 
# curl "https://kalimatimarket.gov.np/price" \
#   -H "authority: kalimatimarket.gov.np" \
#   -H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8" \
#   -H "accept-language: en-US,en;q=0.6" \
#   -H "cache-control: max-age=0" \
#   -H "content-type: application/x-www-form-urlencoded" \
#   -H "cookie: twk_idm_key=rCfVY7GWANfMtMRrAkK_P; XSRF-TOKEN=eyJpdiI6InludGlqamFGRytWaUVhRzErbHhtcmc9PSIsInZhbHVlIjoiK2cyVHlQNkVVSzlFTXJsZ01pbEc3Q09YUncyQlNwRDF0em9CdHFMeE80N1FVakg4b3RoMmtxMlBYc3NGM1NrNmlyNG93YkVnYmhzNHliWXBzb2hxWStHSlVkM2tuYVhVUXh1ckVUM3ltNTcvWjV5cHFtbENXTHBhVS9YY1FuMDAiLCJtYWMiOiI0NDk5OTk2MjZjZmU3NGRhZWM0NGYxMzFkNWRjOTQyZTc5NjQ5ZWYwMjZiMDQ1YTdmNmE2ZjI0ODMyZTcxNmIxIiwidGFnIjoiIn0%3D; kalimati_fruits_and_vegetable_market_development_board_session=eyJpdiI6IkF6ajRveU1rVjdHK25DY2czTk12aFE9PSIsInZhbHVlIjoialhQeCtpejZCNUcvenZEenA2ZWFzMm1RTk1VQmp6UEphYjRPVjRYazhKL1BCaSszdjU0Z0U1MVlBZmFVdVRrVDRnOGtDR21Dc0VibG1YbkxWNUVJblBDbmdqU0ZCWDR1NFNWdFU0TERRd1MyRmFST2xEbUl1Y04yS1c5Q0pBTEoiLCJtYWMiOiJkMzdkY2VjODQ5Yjk5OGUyYzAyMzA3ZDk2NGY2ZjcxM2Q5YWFiOWM4NjY3M2E1NWNiZDBjOWQ3Y2Y5MTM1ZTgzIiwidGFnIjoiIn0%3D; TawkConnectionTime=0; twk_uuid_62b413377b967b11799613cd=%7B%22uuid%22%3A%221.gNC9g2ov8zghQETFNgEMsKdtAPOvSzY6VepPrwVCZCWr2nlM6MDLJ47jsIE7miFmkdiyPWqf2DoE9kp1OUrRHb8m2vOKaxLcRnGbrgcx2XHJa0oKZELs8peSNWJ3lyAhT%22%2C%22version%22%3A3%2C%22domain%22%3A%22kalimatimarket.gov.np%22%2C%22ts%22%3A1707737955124%7D" \
#   -H "origin: https://kalimatimarket.gov.np" \
#   -H "referer: https://kalimatimarket.gov.np/price" \
#   -H "sec-ch-ua: \"Not A(Brand\";v=\"99\", \"Brave\";v=\"121\", \"Chromium\";v=\"121\"" \
#   -H "sec-ch-ua-mobile: ?0" \
#   -H "sec-ch-ua-platform: \"Windows\"" \
#   -H "sec-fetch-dest: document" \
#   -H "sec-fetch-mode: navigate" \
#   -H "sec-fetch-site: same-origin" \
#   -H "sec-fetch-user: ?1" \
#   -H "sec-gpc: 1" \
#   -H "upgrade-insecure-requests: 1" \
#   -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36" \
#   --data-raw "_token=tZr8h5hKHCByCnQecfZiqBtMt8crgELfXRigOnb9&datePricing=2024-02-01" \
#   --compressed
# =============================================================================
