# %%
import pandas as pd
import numpy as np
import math
import timeit 
from util import DegreeSeeker, TimeLimited
from statsmodels.stats.power import tt_ind_solve_power

import seaborn as sns

# %%
df_people = pd.read_csv('small/people.csv', sep=',')
df_people

# %%
df_stars = pd.read_csv('large/stars.csv', sep=',')
df_stars

# %%
dg_seeker = DegreeSeeker()

# %%
dg_seeker.neighbors_for_person(3699941, df_stars)

# %%
next(dg_seeker.shortest_path(45, 102, df_stars))

# %%
stars_list = df_stars['person_id'].unique().tolist()

# %%

@TimeLimited
def min_degree(source, target):
    degree = next(dg_seeker.shortest_path(source, target, df_stars))
    return degree

# %%

def sample_size(population, margin_error, confidence):
    z = 1.96 # standard normal score for 95% confidence level
    p = 0.5 # proportion of the population with the characteristic of interest (assumed as 0.5 for estimation)
    e = margin_error
    n = (z**2 * p * (1-p)) / (e**2)
    return math.ceil(n)

population = 540000
confidence = 0.95
margin_error = 0.05

print("Minimum Sample Size:", sample_size(population, margin_error, confidence))

# %%
from statsmodels.stats.power import tt_ind_solve_power

effect_size = 0.2
alpha = 0.05
power = 0.8
sample_size = tt_ind_solve_power(effect_size=effect_size, nobs1=None, alpha=alpha, power=power, alternative='two-sided')
print(sample_size)

# %%
stars_sampled_list = np.random.choice(stars_list, size=385)

# %%

## Checking if Kvin Bacon was selected
102 in stars_sampled_list

# %%
dict_degree = {actor: next(min_degree(actor, 102)) for actor in stars_sampled_list}

# %%

df_degree = pd.DataFrame.from_dict(dict_degree, orient='index').reset_index().rename(columns={'index':'person_id', 0:'separation_degree'})

# %%
