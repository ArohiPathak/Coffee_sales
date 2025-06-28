# importing libraries
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt


# reading the csv files
df=pd.read_csv(r'C:\Users\Akhil Pathak\Desktop\um internship files\coffee.csv')

# changing the datatype
le = LabelEncoder()
df['coffee_name_encoded'] = le.fit_transform(df['coffee_name'])
df['cash_type_encoded'] = le.fit_transform(df['cash_type'])
df['date_encoded'] = le.fit_transform(df['date'])
df['datetime_encoded'] = le.fit_transform(df['datetime'])
X= df.drop(columns=["card","cash_type","date","datetime","coffee_name","cash_type_encoded"])
y= df['cash_type_encoded']

# splitting up the data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=52, test_size=0.3)

# applying various algorithms
lr1 = LinearRegression()
lr1.fit(X_train, y_train)
lr1.score(X_train, y_train)
lr1.score(X_test, y_test)
y_pred1 = lr1.predict(X_test)
lr1_acc=r2_score(y_test, y_pred1)*100

lr2=RandomForestClassifier()
lr2.fit(X_train, y_train)
lr2.score(X_train, y_train)
lr2.score(X_test, y_test)
y_pred2 = lr2.predict(X_test)
lr2_acc=r2_score(y_test, y_pred2)*100

lr4=GradientBoostingClassifier()
lr4.fit(X_train, y_train)
lr4.score(X_train, y_train)
lr4.score(X_test, y_test)
y_pred4 = lr4.predict(X_test)
lr4_acc=r2_score(y_test, y_pred4)*100


lr6 = DecisionTreeClassifier()
lr6.fit(X_train, y_train)
lr6.score(X_train, y_train)
lr6.score(X_test, y_test)
y_pred6 = lr6.predict(X_test)
lr6_acc=r2_score(y_test, y_pred6)*100

# plotting the accuracy of all the algorithms
x_lr = [lr1_acc, lr2_acc, lr4_acc, lr6_acc]
algorithms = ['Logistic Regression', 'Random Forest', 'Gradient Boosting', 'Decision Tree']
plt.figure(figsize=(8, 5))
plt.bar(algorithms, x_lr, color='orange',width=0.4,edgecolor="black")
plt.title("Accuracy at Different Stages",fontsize=15)
plt.xlabel("Training Progress (%)",fontsize=13)
plt.ylabel("Accuracy",fontsize=13)
plt.ylim(0, 100)  
plt.tight_layout()
plt.show()

