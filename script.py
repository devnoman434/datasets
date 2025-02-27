import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('deliveries.csv')

print(df.filter(["batsman"]))

batsman = df.filter(["batsman","batsman_runs"])

batsman = batsman.groupby("batsman").sum(["batsman_runs"])

batsman = batsman.sort_values(by="batsman_runs", ascending=False)

batsman = batsman.head(10)

sns.barplot(x="batsman", y="batsman_runs", data=batsman)

plt.xticks(rotation=90)
plt.savefig('batsman.png')



print(batsman)


