# importing the libraries
import pandas as pd
import matplotlib.pyplot as plt

# reading the csv file
df=pd.read_csv(r'C:\Users\Akhil Pathak\Desktop\um internship files\coffee.csv')

# coverting to required datatype
df['date'] = pd.to_datetime(df['date'])
df['Month'] = df['date'].dt.to_period('M')
df['MonthName'] = df['date'].dt.strftime('%b')  
df['MonthOrder'] = df['date'].dt.month 
monthly_sales = df.groupby(['MonthOrder', 'MonthName', 'coffee_name']).size().unstack(fill_value=0)
monthly_sales = monthly_sales.sort_index()

x_labels = monthly_sales.index.get_level_values(1) 

# plotting the graph
plt.figure(figsize=(12, 6))
for coffee in monthly_sales.columns:
    plt.plot(x_labels, monthly_sales[coffee], marker='o', label=coffee)

plt.title('Monthly Coffee Sales by Type',fontsize=13)
plt.xlabel('Month',fontsize=11)
plt.ylabel('Number of Sales',fontsize=11)
plt.xticks(rotation=0)
plt.legend(title='Coffee Type')
plt.grid(True)
plt.tight_layout()
plt.show()
