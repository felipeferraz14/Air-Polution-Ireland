# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:09:45 2020

@author: felip
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
plt.style.use('seaborn-whitegrid')



df = pd.ExcelFile('air_polution_data.xls')
df_pm10 = pd.read_excel(df,'PM10',header= 0)
df_pm25 = pd.read_excel(df,'PM2.5',header= 0)
df_so2 = pd.read_excel(df,'SO2',header= 0)
df_o3 = pd.read_excel(df,'O3',header= 0)
df_no2 = pd.read_excel(df,'NO2',header= 0)



columnsnames = df_pm10.iloc[:1]
columnsnames = columnsnames.values.tolist()

columnsnames = columnsnames[0]
columnsnames[1] = "Month"
columnsnames[0] = "Year"

df_pm10 = df_pm10.drop(df_pm10.index[0])
df_pm25 = df_pm25.drop(df_pm25.index[0])
df_so2 = df_so2.drop(df_so2.index[0])
df_o3 = df_o3.drop(df_o3.index[0])
df_no2 = df_no2.drop(df_no2.index[0])



df_pm10.columns = columnsnames
df_pm25.columns = columnsnames
df_so2.columns = columnsnames
df_o3.columns = columnsnames
df_no2.columns = columnsnames


df_pm10 = pd.melt(df_pm10, id_vars = ('Year', 'Month'),var_name = "Day", value_name = "PM10" )
df_pm25 = pd.melt(df_pm25, id_vars = ('Year', 'Month'),var_name = "Day", value_name = "PM25" )
df_so2 = pd.melt(df_so2, id_vars = ('Year', 'Month'),var_name = "Day", value_name = "SO2" )
df_o3 = pd.melt(df_o3, id_vars = ('Year', 'Month'),var_name = "Day", value_name = "O3" )
df_no2 = pd.melt(df_no2, id_vars = ('Year', 'Month'),var_name = "Day", value_name = "NO2" )

df_pm10 = df_pm10.dropna()
df_pm25 = df_pm25.dropna()
df_so2 = df_so2.dropna()
df_o3 = df_o3.dropna()
df_no2 = df_no2.dropna()



df_pm10.loc[df_pm10.Month == "January", "Month"] = 1
df_pm10.loc[df_pm10.Month == "February", "Month"] = 2
df_pm10.loc[df_pm10.Month == "March", "Month"] = 3
df_pm10.loc[df_pm10.Month == "April", "Month"] = 4
df_pm10.loc[df_pm10.Month == "May", "Month"] = 5

df_pm25.loc[df_pm25.Month == "January", "Month"] = 1
df_pm25.loc[df_pm25.Month == "February", "Month"] = 2
df_pm25.loc[df_pm25.Month == "March", "Month"] = 3
df_pm25.loc[df_pm25.Month == "April", "Month"] = 4
df_pm25.loc[df_pm25.Month == "May", "Month"] = 5

df_so2.loc[df_so2.Month == "January", "Month"] = 1
df_so2.loc[df_so2.Month == "February", "Month"] = 2
df_so2.loc[df_so2.Month == "March", "Month"] = 3
df_so2.loc[df_so2.Month == "April", "Month"] = 4
df_so2.loc[df_so2.Month == "May", "Month"] = 5

df_o3.loc[df_o3.Month == "January", "Month"] = 1
df_o3.loc[df_o3.Month == "February", "Month"] = 2
df_o3.loc[df_o3.Month == "March", "Month"] = 3
df_o3.loc[df_o3.Month == "April", "Month"] = 4
df_o3.loc[df_o3.Month == "May", "Month"] = 5

df_no2.loc[df_no2.Month == "January", "Month"] = 1
df_no2.loc[df_no2.Month == "February", "Month"] = 2
df_no2.loc[df_no2.Month == "March", "Month"] = 3
df_no2.loc[df_no2.Month == "April", "Month"] = 4
df_no2.loc[df_no2.Month == "May", "Month"] = 5

df_pm10["date"] = pd.to_datetime(df_pm10[["Year", "Month", "Day"]])
df_pm25["date"] = pd.to_datetime(df_pm25[["Year", "Month", "Day"]])
df_so2["date"] = pd.to_datetime(df_so2[["Year", "Month", "Day"]])
df_o3["date"] = pd.to_datetime(df_o3[["Year", "Month", "Day"]])
df_no2["date"] = pd.to_datetime(df_no2[["Year", "Month", "Day"]])

df1 = df_pm10.groupby(["Year","Month"]).describe()
df2 = df_pm25.groupby(["Year","Month"]).describe()
df3 = df_so2.groupby(["Year","Month"]).describe()
df4 = df_o3.groupby(["Year","Month"]).describe()
df5 = df_no2.groupby(["Year","Month"]).describe()



full_df = pd.merge(df_pm10,df_pm25, how = 'outer', on =['date']) 
full_df = pd.merge(full_df,df_no2,how = 'outer', on =['date'])
full_df = pd.merge(full_df,df_o3, how = 'outer', on =['date'])
full_df = pd.merge(full_df,df_so2, how = 'outer', on =['date'])

full_df = full_df[["date", "PM10", "PM25", "NO2", "O3", "SO2"]]

total_describe = full_df.groupby([full_df.date.dt.year, full_df.date.dt.month]).describe()

dt = total_describe[total_describe["PM10"]]

# df_2018 = full_df[full_df["Year_x"] == 2018]
# df_2019 = full_df[full_df["Year_x"] == 2019]
# df_2020 = full_df[full_df["Year_x"] == 2020]

# x_dates = full_df['date'].dt.strftime('%Y-%m-%d').sort_values().unique()

# min_date = min(full_df['date'])
# max_date = max(full_df['date'])

fig, ax = plt.subplots(ncols = 3, nrows = 5 ,figsize = (12,12), sharey="row", sharex= "col")  


ax[0][0].scatter(x= df_pm10[df_pm10["Year"]==2018].date, y = df_pm10[df_pm10["Year"]==2018].PM10)
ax[0][1].scatter(x= df_pm10[df_pm10["Year"]==2019].date, y = df_pm10[df_pm10["Year"]==2019].PM10)
ax[0][2].scatter(x= df_pm10[df_pm10["Year"]==2020].date, y = df_pm10[df_pm10["Year"]==2020].PM10)


ax[1][0].scatter(x= df_pm25[df_pm25["Year"]==2018].date, y = df_pm25[df_pm25["Year"]==2018].PM25)
ax[1][1].scatter(x= df_pm25[df_pm25["Year"]==2019].date, y = df_pm25[df_pm25["Year"]==2019].PM25)
ax[1][2].scatter(x= df_pm25[df_pm25["Year"]==2020].date, y = df_pm25[df_pm25["Year"]==2020].PM25)


ax[2][0].scatter(x= df_so2[df_so2["Year"]==2018].date, y = df_so2[df_so2["Year"]==2018].SO2)
ax[2][1].scatter(x= df_so2[df_so2["Year"]==2019].date, y = df_so2[df_so2["Year"]==2019].SO2)
ax[2][2].scatter(x= df_so2[df_so2["Year"]==2020].date, y = df_so2[df_so2["Year"]==2020].SO2)


ax[3][0].scatter(x= df_o3[df_o3["Year"]==2018].date, y = df_o3[df_o3["Year"]==2018].O3)
ax[3][1].scatter(x= df_o3[df_o3["Year"]==2019].date, y = df_o3[df_o3["Year"]==2019].O3)
ax[3][2].scatter(x= df_o3[df_o3["Year"]==2020].date, y = df_o3[df_o3["Year"]==2020].O3)


ax[4][0].scatter(x= df_no2[df_no2["Year"]==2018].date, y = df_no2[df_no2["Year"]==2018].NO2)
ax[4][1].scatter(x= df_no2[df_no2["Year"]==2019].date, y = df_no2[df_no2["Year"]==2019].NO2)
ax[4][2].scatter(x= df_no2[df_no2["Year"]==2020].date, y = df_no2[df_no2["Year"]==2020].NO2)


ax[0][0].set(ylabel = "PM10")

ax[1][0].set(ylabel = "PM2.5")
ax[1][0].axhline(53,color='red',ls='--')
ax[1][1].axhline(53,color='red',ls='--')
ax[1][2].axhline(53,color='red',ls='--')
ax[2][0].set(ylabel = "SO2")
ax[3][0].set(ylabel = "O3")
ax[4][0].set(ylabel = "NO2")
fig.autofmt_xdate()






