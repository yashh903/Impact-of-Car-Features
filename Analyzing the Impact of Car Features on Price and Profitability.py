#importing libaries
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

#importing dataset
df=pd.read_excel(r"C:\Users\YASH\Downloads\Car_data 1.xlsx")

#regression analysis
x=df[['Engine HP','Engine Cylinders','Number of Doors','highway MPG','city mpg','Popularity']]
y=df.MSRP
x = sm.add_constant(x)
r=sm.OLS(y,x).fit()
r.summary()

#plotting graph
z={'Engine HP':320.4942,'Engine Cylinders':7578.7913,'Number of Doors':-4980.2100,'highway MPG':503.5835,'city mpg':1253.4681,'Popularity':-3.5534}
variables = list(z.keys())
values = list(z.values())

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')
        
plt.bar(variables, values)
addlabels(variables,values)
plt.xticks(rotation=45)
plt.title('coefficient values for each variable')
plt.show()

