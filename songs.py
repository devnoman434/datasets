import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('songs.csv')

print(df.head())

songs = df.filter(["track_name","track_popularity"])

songs = songs.sort_values(by="track_popularity", ascending=False)

songs = songs.head(10)

plt.figure(figsize=(12,7))
sns.barplot(x="track_name", y="track_popularity", data=songs, color="blue")

plt.xticks(rotation=45)
plt.xlabel("Track Name")
plt.ylabel("Popularity")
plt.title("Top 10 Songs")
plt.savefig('top_10_songs.png')