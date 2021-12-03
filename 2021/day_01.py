import pandas as pd
from pathlib import Path
import numpy as np

# save https://adventofcode.com/2021/day/1/input as .txt file
# solution 1
data = Path('data/day_01')

df = pd.read_csv(data.joinpath('input.txt'), names=['depths'])
df['lead'] = df['depths'].shift(1)
df['increased'] = np.where(df['depths'] - df['lead'] > 0, 1, 0)

sum(df['increased'])

# solution 2
df = pd.read_csv(data.joinpath('input.txt'), names=['depths'])
df['lead'] = df['depths'].shift(1)
df['lead2'] = df['lead'].shift(1)

df['sum'] = df['depths'] + df['lead'] + df['lead2']
df['sum_lead'] = df['sum'].shift(1)
df['increased'] = np.where(df['sum'] - df['sum_lead'] > 0, 1, 0)

sum(df['increased'])






