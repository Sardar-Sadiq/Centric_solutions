import pandas as pd
import random

data = []

price = 100  # starting price

for day in range(1, 201):
    change = random.uniform(-2, 2)
    price = round(price + change, 2)

    data.append([day, price])

df = pd.DataFrame(data, columns=["Day", "Close"])
df.to_csv("stock_data.csv", index=False)

print("✅ stock_data.csv created!")