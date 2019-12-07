import pandas as pd

import os

data = pd.read_csv('outputrefactor.csv', sep='|', header=-1)

# Suffle
data = data.sample(frac=1)

train_ratio = 0.8
train_index = int(train_ratio * len(data))

with open('training.txt', 'w') as fd:
    for i, fname in enumerate(data[0][:train_index]):
        fd.write('{}|{}\n'.format(os.path.join(os.getcwd(), fname), data[1][i]))

with open('testing.txt', 'w') as fd:
    for i, fname in enumerate(data[0][train_index:]):
        fd.write('{}|{}\n'.format(os.path.join(os.getcwd(), fname), data[1][i]))
