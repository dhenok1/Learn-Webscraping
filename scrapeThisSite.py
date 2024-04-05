from bs4 import BeautifulSoup
import requests
import pandas as pd
from os import replace

masterDF = pd.DataFrame()
i = 1
while (True):
    url = "https://www.scrapethissite.com/pages/forms/?page_num=" + str(i)
    page = requests.get(url)


    soup = BeautifulSoup(page.text, features="html.parser")


    data = soup.find_all('tr', class_ = 'team')
    if len(data) == 0:
        break
    dataList = []
    for row in data:
        teamList = []
        for col in row:
            text = col.text
            text = " ".join(text.split())
            if text != '':
                temp = text
                teamList.append(int(text) if text.isnumeric() else (float(text) if temp.replace('.', '').isnumeric() else text))
        if len(teamList) == 8:
            teamList.insert(4, 0)
        dataList.append(teamList)

    
    headers = soup.find_all('th')
    headersList = []
    for head in headers:
        text = head.text
        text = " ".join(text.split())
        headersList.append(text)
    df = pd.DataFrame(data = dataList, columns = headersList)
    masterDF = pd.concat([masterDF, df], ignore_index=True)
    i+=1

print(masterDF)