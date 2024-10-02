import pandas as pd

path = './Sesión_2/Online_Retail.csv'

sales_data = pd.read_csv(path, encoding='latin1')

print(sales_data.head(2))

#Quedamos en la página 37 del material de apoyo paso 17