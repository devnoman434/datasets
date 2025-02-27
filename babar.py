import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('babar.csv')


print(df.head())

print(df.describe())

babar = df.filter(["Runs","Opposition"])

babar = babar.groupby("Opposition").sum(["Runs"])

babar = babar.sort_values(by="Runs", ascending=False)

babar = babar.head(10)

plt.figure(figsize=(12,7))
sns.barplot(x="Opposition", y="Runs", data=babar)
plt.xticks(rotation=45)
plt.xlabel("4s")
plt.ylabel("Runs")
plt.title("Babar Azam")
plt.savefig('babar.png')