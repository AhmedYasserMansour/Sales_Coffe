import numpy as np
import pandas as pd
import datetime

df1 = pd.read_csv(r'C:\Users\Ahmed Yasser\Desktop\Sales_Coffe\raw_data\index_1.csv')
df2 = pd.read_csv(r'C:\Users\Ahmed Yasser\Desktop\Sales_Coffe\raw_data\index_2.csv')

df2['card'] = 'N/A'
df2 = df2[df1.columns]

df1['date'] = pd.to_datetime(df1['date'], errors='coerce')
df2['date'] = pd.to_datetime(df2['date'], errors='coerce')
df1['datetime'] = pd.to_datetime(df1['datetime'], errors='coerce')
df2['datetime'] = pd.to_datetime(df2['datetime'], errors='coerce')

df = pd.concat([df1,df2],ignore_index=True) # merged_data
df['card'] = df['card'].fillna('N/A') 


df['hour'] = df['datetime'].dt.hour
df['day_Of_Week'] = df['datetime'].dt.day_name()
df['month'] = df['datetime'].dt.month_name()
df['month_year'] = df['datetime'].dt.to_period('M').astype(str)
df['year'] = df['datetime'].dt.year



def time_of_day(hour) :
    if 6 < hour < 12:
        return 'morning' 
    elif 12 <= hour < 18 :
        return 'at noon'
    else :
        return 'evening'

df['time_of_day'] = df['hour'].apply(time_of_day)

df.columns = [col.capitalize() for col in df.columns]


# print(df.sample(5)) # Check

df.to_csv(r'C:\Users\Ahmed Yasser\Desktop\Sales_Coffe\clean&analysis\cleaning_data.csv',index=False)


