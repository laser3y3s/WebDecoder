
'''
Created on 3-August-2018
This script extracts main headings from NY Times website along with their URLs and prints them out.
If you like to ,help me to run this script on a webpage

'''

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,"html.parser")

heading = soup.find_all('h2' , class_="story-heading")



for i in heading:

    if i.find('a')==None:
        continue

    tx = i.find('a')
    for child in tx.children:
        if child==None:
            continue

        print(str(child).strip())

    print(tx.get('href').strip())
    print("\n")
