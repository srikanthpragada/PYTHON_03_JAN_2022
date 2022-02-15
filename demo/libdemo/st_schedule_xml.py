import requests
from bs4 import BeautifulSoup
from datetime import *

URL = "http://www.srikanthtechnologies.com/schedule.xml"
response = requests.get(URL)
if response.status_code != 200:
    print("Sorry! Could not get details!!!")
    exit(1)

bs = BeautifulSoup(response.text, "lxml-xml")

batches = bs.find_all('batch')

for batch in batches:
    print(batch['subject'])
    print('http://www.srikanthtechnologies.com/' + batch['syllabuslink'])
    print(batch['link'])
    print('-' * 50)