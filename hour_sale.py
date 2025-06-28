# importing the libraries
import pandas as pd
import matplotlib.pyplot as plt

# reading the sorted csv file
df=pd.read_csv(r'C:\Users\Akhil Pathak\Desktop\um internship files\busiest_hour.csv')

# plotting the graph
plt.bar(df['hour'],df['total_money'],color='c',edgecolor='black',linewidth=1.5)
plt.title("Hourly Sales Performance Analysis", fontsize=15)
plt.xlabel("Time",fontsize=13)
plt.ylabel("Money", fontsize=13)
plt.legend()
plt.xticks(range(7, 23))
plt.show()