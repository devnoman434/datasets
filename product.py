import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('product.csv')


product = df.get(["name","discount_price"])

product = product.sort_values(by="discount_price", ascending=False)
product=product.drop_duplicates(subset="discount_price")

product = product.head(10)
print(product)
plt.figure(figsize=(12,7))
sns.barplot(x="name", y="discount_price", data=product, color="blue")
plt.xticks(rotation=45)
plt.xlabel("Product Name")
plt.ylabel("Discounted Price")
plt.title("Top 10 Products")
plt.savefig('discounted_price.png')