import requests
from bs4 import BeautifulSoup
from datetime import *

URL = "http://www.srikanthtechnologies.com"
response = requests.get(URL)
if response.status_code != 200:
    print("Sorry! Could not get details!!!")
    exit(1)

bs = BeautifulSoup(response.text, "html.parser")

table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
if table is None:
    print("Sorry! Could not retrieve data as required table is missing!")
    exit(2)


for row in table.find_all("tr")[1:]:  # Take from 2nd row onwards
    cols = row.find_all("td")
    course = cols[0].text
    timings = cols[1].text
    stdate = cols[2].text

    cd = datetime.now()
    sd = datetime.strptime(f"{stdate}-{cd.year}", '%d-%b-%Y')
    gap = sd - cd
    if gap.days > 0:  # sd is after sysdate
        days = f"{gap.days:2} days to go"
    else:
        days = f"{abs(gap.days):2} days old"

    print(f"{course:50} {timings:15} {stdate:10} {days}")