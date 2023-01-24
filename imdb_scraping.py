# %%
import pandas as pd 
import numpy as np
from bs4 import BeautifulSoup
import urllib.request

# %%

html_page = urllib.request.urlopen('https://www.imdb.com/list/ls058011111/')
soup_imdb = BeautifulSoup(html_page, "html.parser")

list_hrefs_imdb_100 = []

for link in soup_imdb.findAll('a'):
    if 'name' in link.get('href'):
        list_hrefs_imdb_100.append(link.get_text())
    else:
        continue

# %%

list_urls = ['https://www.imdb.com/list/ls058011111/', 'https://www.imdb.com/list/ls058011111/?sort=list_order,asc&mode=detail&page=2', 'https://www.imdb.com/list/ls058011111/?sort=list_order,asc&mode=detail&page=3', 'https://www.imdb.com/list/ls058011111/?sort=list_order,asc&mode=detail&page=4', 'https://www.imdb.com/list/ls058011111/?sort=list_order,asc&mode=detail&page=5', 'https://www.imdb.com/list/ls058011111/?sort=list_order,asc&mode=detail&page=6', 'https://www.imdb.com/list/ls058011111/?sort=list_order,asc&mode=detail&page=7', 'https://www.imdb.com/list/ls058011111/?sort=list_order,asc&mode=detail&page=8', 'https://www.imdb.com/list/ls058011111/?sort=list_order,asc&mode=detail&page=9', 'https://www.imdb.com/list/ls058011111/?sort=list_order,asc&mode=detail&page=10']

# %%

list_hrefs_imdb = []

for url in list_urls:
    html_page = urllib.request.urlopen(url)
    soup_imdb = BeautifulSoup(html_page, "html.parser")

    for link in soup_imdb.findAll('a'):
        if 'name' in link.get('href'):
            list_hrefs_imdb.append(link.get_text())
        else:
            continue
# %%

df_names_1000 = pd.DataFrame(list_hrefs_imdb).rename(columns={0:'name'})
# %%
df_names_1000.replace(' \n', np.nan, inplace=True)

# %%

df_names_1000 = df_names_1000.dropna().reset_index(drop=True).copy()

# %%

df_names_1000['name'] = df_names_1000['name'].apply(lambda x : x.strip())

# %%

df_names_1000.loc[df_names_1000['name'].duplicated()]
# %%
df_names_1000 =  df_names_1000.drop_duplicates().reset_index(drop=True).copy()
# %%
