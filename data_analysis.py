#This is just code from following along with this tutorial: https://www.youtube.com/watch?v=DamIIzp41Jg&list=PLQVvvaa0QuDfSfqQuee6K8opKtZsh7sA9&index=2

import pandas as pd
import matplotlib.pyplot as plt

df  = pd.read_csv("D:/sandbox/datasets/avocado.csv")
df['Date'] = pd.to_datetime(df['Date'])
albany_df = df[df['region'] == 'Albany']
albany_df.set_index("Date", inplace = True)
albany_df.sort_index(inplace = True)
plt.plot(albany_df['AveragePrice'].rolling(25).mean())
plt.show()
