import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
  
data = pd.read_csv('Comphrehensive_Environment_Pollution_Index_For_Critically_Polluted_Industrial_Area_Clusters_1.csv')
df = pd.DataFrame(data)
  
X = list(df.iloc[:, 1])
Ywater = list(df.iloc[:, 2])
Yland = list(df.iloc[:, 3])

lineStart = np.asarray(X).min()
lineEnd = np.asarray(X).max()

plt.scatter(X, Ywater, color='b',label='Water Pollution Index')
plt.scatter(X, Yland, color='y',label='Land Pollution Index')
plt.plot([lineStart, lineEnd], [lineStart, lineEnd], 'k-', color = 'r')
plt.title("Relation between Pollution Indices in Industrial Areas")
plt.xlabel("Air Pollution Index")
plt.ylabel("Water/Land Pollution Index")
plt.grid()
plt.legend()

plt.show()