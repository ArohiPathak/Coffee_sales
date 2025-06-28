# importing libraries
import pandas as pd
import matplotlib.pyplot as plt

# reading the sorted csv file
df = pd.read_csv(r'C:\Users\Akhil Pathak\Desktop\um internship files\cash_card.csv')

# plotting a donut chart
plt.pie(df['number'],labels=df['payment_method'],
        autopct='%1.1f%%',pctdistance=0.75, 
        colors= ['green','yellow'],
        startangle=180, textprops={'fontsize':10},
        wedgeprops={'linewidth':2,'width':0.495,'edgecolor':'black'} )
plt.axis('equal')
plt.legend()
plt.title("Payment Menthod", y=1.025, fontsize=13)
plt.show()