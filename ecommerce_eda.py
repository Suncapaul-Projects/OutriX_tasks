# IMPORT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# LOAD DATASET
file_path = r"C:\Users\DELL\OneDrive\Desktop\commerce.eda\Online Retail.xlsx"
df = pd.read_excel(file_path)

# DISPLAY BASIC INFO
print("First 5 rows")
print(df.head())

print("\nDataset Info")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

# DATA CLEANING

# Remove rows with missing CustomerID
df = df.dropna(subset=['CustomerID'])

# Remove negative quantity (returns)
df = df[df['Quantity'] > 0]

# Remove negative price
df = df[df['UnitPrice'] > 0]

# CREATE TOTAL SALES COLUMN
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

print("\nCleaned Data Shape:", df.shape)

# EXPLORATORY DATA ANALYSIS

# figure - 1 TOP 10 SELLING PRODUCTS
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title("Top 10 Selling Products")
plt.xlabel("Quantity Sold")
plt.ylabel("Product")
plt.show()

# figure - 2 SALES BY COUNTRY
country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=country_sales.values, y=country_sales.index)
plt.title("Top Countries by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Country")
plt.show()

# figure - 3 MONTHLY SALES TREND
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Month'] = df['InvoiceDate'].dt.to_period('M')

monthly_sales = df.groupby('Month')['TotalPrice'].sum()

plt.figure(figsize=(12,6))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

# figure - 4 CUSTOMER PURCHASE DISTRIBUTION
customer_spending = df.groupby('CustomerID')['TotalPrice'].sum()

plt.figure(figsize=(8,5))
sns.histplot(customer_spending, bins=50)
plt.title("Customer Spending Distribution")
plt.xlabel("Total Spending")
plt.show()

# figure - 5 CORRELATION HEATMAP
plt.figure(figsize=(6,4))
sns.heatmap(df[['Quantity','UnitPrice','TotalPrice']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()