#Pandas
import pandas as pd
print (pd.__version__)

a = pd.DataFrame({ 'name' : ['Ali','Hassan','Akif'],
                  'Age' : [16,20,34],

                   })
print(a)
print(a.Age)
print(a.size)
print(a.shape)
print(a.info)
print(a.columns)
print(a.dtypes)