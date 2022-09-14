import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
  
data = pd.read_csv('Per_Capita_Income_at_Current_Prices.csv')
df = pd.DataFrame(data)

df = df.drop(['S. No','District'], axis=1)
df.columns = df.columns.str.rstrip(' (In Rupees)')
df.columns = df.columns.str.rstrip(' (P')
df.columns = df.columns.str.rstrip(' (Q')
df.boxplot()
plt.title("Yearly Per Capita Income at Current Prices")
plt.xlabel("Years")
plt.ylabel("Per Capita Income(Rs.))")
plt.grid()
plt.xticks(rotation = 45,ha='right')

plt.show()