import requests
import random
import csv
from bs4 import BeautifulSoup
from datetime import datetime
import sys

today = datetime.today().strftime('%Y-%m-%d')
page_no = 1
file = open('out.csv', 'w')
writer = csv.writer(file, delimiter='\t')
data = ['source','meaning']
writer.writerow(data)

from fake_useragent import UserAgent

#open file using open file mode
fp1 = open(sys.argv[1], "r", encoding='utf-8') # Open file on read mode -- input file
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

def GET_UA():
    uastrings = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"\
                ]

    return random.choice(uastrings)

#glosbe_dicts_array = {
 #   "glosbe":["https://glosbe.com/sa/te/", 1]
#}
meanings = []
for line in lines:
    url = "https://glosbe.com/sa/te/"
    #print("Hello",url,pages)
   
    headers = {'User-Agent': GET_UA()}
    #headers = {'User-Agent': UserAgent()}
    #Redmi
    #1-5
    #url = 'https://www.amazon.in/s?i=electronics&bbn=1389432031&rh=n%3A1389432031%2Cp_89%3ARedmi&dc&qid=1637256738&rnid=3837712031&ref='+string
    url2 = url + line
    print ('Fetching data from ',url2)
    response = requests.get(url2, headers=headers)
    print(response.content)
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup)
    basicwrap = soup.find_all(class_='translation dense')
    #print(basicwrap)
    for i in basicwrap:
        #print(i)
        try:
            meaning = (i.find('span').get_text().strip())
            #print(name)
        except:
            meaning = ('Not available')
        meanings.append(meaning)

    meanings = ",".join(meanings)
    data = [line, meanings]
    meanings = []
    writer.writerow(data)
