import pandas as pd
import matplotlib.pyplot as plt
companies = ['Microsoft','Google','Amazon','IBM','Deloitte','Capgemini','ATOS','Amdocs']
recruitment = [120, 150, 180, 100, 90, 110, 70, 95]

# (a) Bar Chart
plt.bar(companies, recruitment)
plt.title("Company Recruitment")
plt.xlabel("Companies")
plt.ylabel("No. of Employees")
plt.xticks(rotation=30)
plt.show()

# (b) Pie Chart
plt.pie(recruitment, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

# (c) Customized Pie Chart
explode = [0,0.1,0,0,0,0,0,0]
plt.pie(recruitment, labels=companies, autopct='%1.1f%%', explode=explode, shadow=True)
plt.title("Customized Pie Chart")
plt.show()

# (d) Doughnut Chart
plt.pie(recruitment, labels=companies, autopct='%1.1f%%')
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()

# Comparison: IBM vs Amdocs
names = ['IBM','Amdocs']
values = [100,95]

plt.bar(names, values)
plt.title("IBM vs Amdocs Recruitment")
plt.ylabel("Employees")
plt.show()