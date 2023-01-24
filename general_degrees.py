# %%
import pandas as pd
import numpy as np
import math
from util import DegreeSeeker
from statsmodels.stats.power import tt_ind_solve_power
from imdb_scraping import df_names_1000
import seaborn as sns

# %%
df_people = pd.read_csv('large/people.csv', sep=',')
df_people

# %%

df_for_test = df_names_1000.merge(df_people, on='name', how='left')

# %%

df_for_test = df_for_test.loc[~df_for_test['name'].duplicated()].dropna(subset=['id']).reset_index(drop=True).copy()

# %%

list_for_stars = df_for_test['id'].unique().tolist()

# %%
df_stars = pd.read_csv('large/stars.csv', sep=',')
df_stars

# %% 

df_stars_for_test = df_stars.loc[df_stars['person_id'].isin(list_for_stars)].reset_index(drop=True).copy()

# %%
dg_seeker = DegreeSeeker()

# %%
dg_seeker.neighbors_for_person(3699941, df_stars)

# %%
dg_seeker.shortest_path(47, 102, df_stars, 10)

# %%
stars_list = df_stars_for_test['person_id'].unique().tolist()

# %%

def sample_size(population, margin_error, confidence):
    z = 1.96 # standard normal score for 95% confidence level
    p = 0.5 # proportion of the population with the characteristic of interest (assumed as 0.5 for estimation)
    e = margin_error
    n = (z**2 * p * (1-p)) / (e**2)
    return math.ceil(n)

population = 540000
confidence = 0.90
margin_error = 0.03

print("Minimum Sample Size:", sample_size(population, margin_error, confidence))

# %%
dict_degree = {actor: dg_seeker.shortest_path(102, actor, df_stars_for_test, 120) for actor in stars_list[0:10]}

# %%

df_degree = pd.DataFrame.from_dict(dict_degree, orient='index').reset_index().rename(columns={'index':'person_id', 0:'separation_degree'})

# %%

df_degree_without_zeros = df_degree.loc[df_degree['separation_degree']>0].reset_index(drop=True).copy()

mg_error = 1.96*(df_degree_without_zeros['separation_degree'].std())/(math.sqrt(len(stars_list))) 

# %%
mean = df_degree_without_zeros['separation_degree'].mean()

# %%

import scipy.stats as ss

ss.norm.interval(alpha=0.90, loc = mean, scale=ss.sem(df_degree_without_zeros['separation_degree']))

# %%

list_of_means = []

for i in range(10000):
    mean = np.random.choice(df_degree_without_zeros['separation_degree'],size = 10000, replace=True).mean()
    list_of_means.append(mean)
mean_array_from_list = np.array(list_of_means)

# %%

import matplotlib.pyplot as plt

sns.histplot(mean_array_from_list)
#sns.histplot(df_means_pos_sem_receita, kde=True)
plt.axvline(mean_array_from_list.mean(), color='r', linestyle='dashed', linewidth=1)
min_ylim, max_ylim= plt.xlim()
plt.text(mean_array_from_list.mean()*0.995, max_ylim*230 ,'Média: {:.2f}'.format(mean_array_from_list.mean()))
plt.show()

# %%
