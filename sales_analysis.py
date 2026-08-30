import pandas as pd
import matplotlib.pyplot as plt
print("SALES DATA ANALYSIS")
print("=" * 30)

df = pd.read_csv("sales_data.csv")

df["Total_Sales"] = df["Quantity"] * df["Price"]

print(df)
print("\nTotal Revenue:", df["Total_Sales"].sum())
print("Average Sale:", df["Total_Sales"].mean())
print("Highest Sale:", df["Total_Sales"].max())
product_sales = df.groupby("Product")["Total_Sales"].sum()

print("\nSales by Product:")
print(product_sales)
top_product = product_sales.idxmax()

print("\nTop Product:", top_product)

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
category_sales = df.groupby("Category")["Total_Sales"].sum()

print("\nSales by Category:")
print(category_sales)
units_sold = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)

print("\nUnits Sold by Product:")
print(units_sold)

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
print("\nKEY FINDINGS")
print("-" * 30)
print("Top revenue product:", top_product)
print("Highest revenue category:", category_sales.idxmax())
print("Most units sold:", units_sold.idxmax())
