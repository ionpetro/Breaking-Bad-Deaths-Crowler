import pprint
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description='Add the path where you want to save the data')
parser.add_argument('path', help='an integer for the accumulator')


r = requests.get('https://breakingbad.fandom.com/wiki/List_of_deaths_on_Breaking_Bad')
html = r.content
soup = BeautifulSoup(html, 'html.parser' )
tables = soup.findAll('h2')
My_table = soup.findAll('table',{'class':'article-table'})
My_table.pop(0)
My_table.pop(-1)

season1 = My_table[0]
th = season1.find_all('th')

columns = []
for column in th:
    columns.append(column.get_text().strip())
columns[0] = 'Dead'
columns.append('Season')

records = []
seas = 1
for season in My_table:
    lines = season.find_all('tr')
    for line in lines[1:]:
        td = line.find_all('td')
        for values in td:
            records.append(values.get_text().strip())
        records.append(seas)
    seas+=1

result = np.asarray(records)
result = result.reshape(-1,5)
df_result = pd.DataFrame(result, columns=columns)

bbd = df_result.to_csv(r'C:\Users\Ion\Desktop\bbd.csv', index=False, header=True)