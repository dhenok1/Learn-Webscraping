from bs4 import BeautifulSoup
import requests
import pandas as pd
from os import replace

url = "https://www.forbes.com/billionaires/"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")