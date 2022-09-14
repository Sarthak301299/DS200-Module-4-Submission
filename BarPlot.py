import matplotlib.pyplot as plt
import pandas as pd
  
data = pd.read_csv('HESCOM_Category_wise_installations_and_Consumption_for_June_2022.csv')
df = pd.DataFrame(data)
  
X = list(df.iloc[:, 1])
Y = list(df.iloc[:, 2])

plt.bar(X, Y, color='g')
plt.title("Low Tension HESCOM Installations for June 2022")
plt.xlabel("Category")
plt.ylabel("Number of Installations")
plt.grid()
plt.xticks(rotation = 45,ha='right')

plt.show()