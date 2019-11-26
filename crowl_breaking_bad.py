import pprint
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import argparse


parser = argparse.ArgumentParser(description='Add the path where you want to save the data. Path example: C:\<name>\<directory>\outcome.csv')
parser.add_argument('path', help='dont forget to add filename in the end (output.csv)')
args = parser.parse_args()
path = args.path
print(path)

try:
    r = requests.get('https://breakingbad.fandom.com/wiki/List_of_deaths_on_Breaking_Bad')
except requests.exceptions.HTTPError as he:
    print(he)
except requests.exceptions.ConnectionError as ce:
    print(ce)
else:
    print("Page retrieval OK!")


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
    try:
        df_result.to_csv(path, index=False, header=True)
    except TimeoutError as te:
        print(te)
    else:
        print('Dataset created successfully!')