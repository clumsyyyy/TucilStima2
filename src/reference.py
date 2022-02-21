#%%

import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
from sklearn import datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


plt.figure(figsize = (10, 6))
colors = ['r', 'g', 'b']

plt.title('Petal Width vs Petal Length')


data = datasets.load_iris()
df = pd.DataFrame(data.data, columns = data.feature_names)
df['Target'] = pd.DataFrame(data.target)

plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])

#%%
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i].iloc[:, [0, 1]].values
    hull = ConvexHull(bucket)

# plt.scatter(bucket[:, 0], bucket[:, 1], label = data.target_names[i])

#%%
for simplex in hull.simplices:
    print(simplex)
    plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
plt.legend()

# %%
