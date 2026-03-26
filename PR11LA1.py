import pandas as pd
import matplotlib.pyplot as plt
data = {
    'month': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    'facecream': [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900],
    'facewash': [1500,1200,1340,1130,1740,1550,1120,1650,1420,1870,2100,1760],
    'toothpaste': [5200,5100,4550,5870,6000,5200,6100,6500,7000,6800,7200,7500],
    'bathingsoap': [9200,6100,9550,8870,9960,8100,9200,10300,11200,9800,10500,11000],
    'shampoo': [1200,2100,3550,1870,1560,1890,1780,2100,2300,2400,1800,2000],
    'total_profit': [211000,183300,224400,258700,273800,235600,234000,266000,312000,298000,321000,345000]
}

df = pd.DataFrame(data)
# (a) Line Plot – Total Profit
plt.plot(df['month'], df['total_profit'], marker='o')
plt.title("Total Profit Per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid()
plt.show()

# (b) Multiline Plot – All Products
plt.plot(df['month'], df['facecream'], label='Face Cream')
plt.plot(df['month'], df['facewash'], label='Face Wash')
plt.plot(df['month'], df['toothpaste'], label='Toothpaste')

plt.title("Product Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

# (c) Bar Chart – Face Cream & Face Wash
import numpy as np

x = np.arange(len(df['month']))

plt.bar(x - 0.2, df['facecream'], width=0.4, label='Face Cream')
plt.bar(x + 0.2, df['facewash'], width=0.4, label='Face Wash')

plt.xticks(x, df['month'])
plt.title("Face Cream vs Face Wash Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

# (d) Pie Chart – Total Yearly Sales
total_sales = [
    df['facecream'].sum(),
    df['facewash'].sum(),
    df['toothpaste'].sum(),
    df['bathingsoap'].sum(),
    df['shampoo'].sum()
]

labels = ['Face Cream','Face Wash','Toothpaste','Bathing Soap','Shampoo']

plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title("Total Sales Distribution")
plt.show()
