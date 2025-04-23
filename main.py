import pandas as pd
import matplotlib.pyplot as plt

# Dataset for Company Comparison
comparison_data = {
    'Company': ['TechCorp', 'TechCorp', 'TechCorp', 'TechCorp', 'TechCorp', 'TechCorp',
                'Innovatek', 'Innovatek', 'Innovatek', 'Innovatek', 'Innovatek', 'Innovatek'],
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse',
                'Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse'],
    'Units Sold': [180, 320, 250, 160, 300, 280, 150, 290, 210, 140, 260, 250],
    'Unit Price': [750, 550, 320, 260, 45, 35, 700, 500, 300, 250, 40, 30]
}

# Create DataFrame
df = pd.DataFrame(comparison_data)

# Calculate total sales
df['Total Sales'] = df['Units Sold'] * df['Unit Price']

# Display Total Sales by Company and Product
print("\nTotal Sales by Product and Company:")
print(df[['Company', 'Product', 'Total Sales']])

# Calculate average total sales per company
average_sales = df.groupby('Company')['Total Sales'].mean()
print("\nAverage Total Sales per Company:")
print(average_sales)

# Save the DataFrame as CSV for record
df.to_csv("sales_data_comparison.csv", index=False)
print("\nData saved to sales_data_comparison.csv")

# Split company data
techcorp_df = df[df['Company'] == 'TechCorp']
innovatek_df = df[df['Company'] == 'Innovatek']

# Bar Chart: Total Sales by Product (both companies)
plt.figure(figsize=(8, 5))
plt.bar(df['Product'], df['Total Sales'], color='purple')
plt.title('Total Sales by Product (Both Companies)')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('bar1_total_sales.png')
plt.close()

# Bar Chart: TechCorp Units Sold
plt.figure(figsize=(8, 5))
plt.bar(techcorp_df['Product'], techcorp_df['Units Sold'], color='skyblue')
plt.title('TechCorp: Units Sold')
plt.xlabel('Product')
plt.ylabel('Units Sold')
plt.tight_layout()
plt.savefig('bar2_techcorp_units.png')
plt.close()

# Bar Chart: Innovatek Units Sold
plt.figure(figsize=(8, 5))
plt.bar(innovatek_df['Product'], innovatek_df['Units Sold'], color='orange')
plt.title('Innovatek: Units Sold')
plt.xlabel('Product')
plt.ylabel('Units Sold')
plt.tight_layout()
plt.savefig('bar3_innovatek_units.png')
plt.close()

# Bar Chart: Unit Price by Product
plt.figure(figsize=(8, 5))
plt.bar(df['Product'], df['Unit Price'], color='green')
plt.title('Unit Price by Product')
plt.xlabel('Product')
plt.ylabel('Unit Price')
plt.tight_layout()
plt.savefig('bar4_unit_price.png')
plt.close()

# Bar Chart: Company-wise Total Sales
sales_by_company = df.groupby('Company')['Total Sales'].sum()
plt.figure(figsize=(6, 5))
sales_by_company.plot(kind='bar', color=['blue', 'orange'])
plt.title('Company-wise Total Sales')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('bar5_company_total_sales.png')
plt.close()

# Pie Chart: Total Sales Share by Company
plt.figure(figsize=(6, 6))
plt.pie(sales_by_company, labels=sales_by_company.index, autopct='%1.1f%%')
plt.title('Total Sales Share by Company')
plt.savefig('pie1_total_sales_company.png')
plt.close()

# Pie Chart: TechCorp Product Sales Share
plt.figure(figsize=(6, 6))
plt.pie(techcorp_df['Total Sales'], labels=techcorp_df['Product'], autopct='%1.1f%%')
plt.title('TechCorp Sales Distribution')
plt.savefig('pie2_techcorp_sales.png')
plt.close()

# Pie Chart: Innovatek Product Sales Share
plt.figure(figsize=(6, 6))
plt.pie(innovatek_df['Total Sales'], labels=innovatek_df['Product'], autopct='%1.1f%%')
plt.title('Innovatek Sales Distribution')
plt.savefig('pie3_innovatek_sales.png')
plt.close()

# Pie Chart: Units Sold by Product (All)
units_by_product = df.groupby('Product')['Units Sold'].sum()
plt.figure(figsize=(6, 6))
plt.pie(units_by_product, labels=units_by_product.index, autopct='%1.1f%%')
plt.title('Units Sold by Product (All Companies)')
plt.savefig('pie4_units_by_product.png')
plt.close()

# Pie Chart: Unit Price Share by Product
unit_price_avg = df.groupby('Product')['Unit Price'].mean()
plt.figure(figsize=(6, 6))
plt.pie(unit_price_avg, labels=unit_price_avg.index, autopct='%1.1f%%')
plt.title('Unit Price Share by Product')
plt.savefig('pie5_unit_price_share.png')
plt.close()
