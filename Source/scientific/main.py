# import thư viện
# ket nối csdl
# trend với prophet
# ham tao thư viện
# ghi tep binary

import pandas as pd
import pyodbc
from fbprophet import Prophet
import pickle

from base import base_url_model

conn = pyodbc.connect('Driver={SQL Server};'  # connect with SQL server
                      'Server=DESKTOP-05ICLAS\\SERVER2;'
                      'Database=DUAN_KHUCNC;'
                      'Trusted_Connection=yes;')
# cursor = conn.cursor() # ham nay chua dung

# read data
# VonDauTuVND
dataVonDauTuVND = pd.read_sql_query('SELECT NGAY_DANG_KY, VON_DAU_TU_VND FROM dbo.GIAY_CNDT', conn)  # get data from db
dataVonDauTuVND = dataVonDauTuVND.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_VND': 'y'})  # rename
dataVonDauTuVND.head()

# VonDauTuUSD
dataVonDauTuUSD = pd.read_sql_query('SELECT NGAY_DANG_KY,VON_DAU_TU_USD FROM dbo.GIAY_CNDT', conn)  # get data from db
dataVonDauTuUSD = dataVonDauTuUSD.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_USD': 'y'})  # rename
dataVonDauTuUSD.head()

# Ti le lao dong

# m = Prophet(seasonality_mode='multiplicative')  # init prophet
m = Prophet()
# create model and save model
m.fit(dataVonDauTuVND)
pickle.dump(m, open(base_url_model + '/VonDauTuVND.pickle', 'wb'))
#
# m = Prophet()
# m.fit(dataVonDauTuUSD)
# pickle.dump(m, open(base_url_model + '/VonDauTuUSD.pickle', 'wb'))

## ---------------------- Funtion test result Prophet----------------------------------------

future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
future.tail()

# dong ket noi sqlserver
# cursor.close()
conn.close()
forecast = m.predict(future)
# forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

fig1 = m.plot(forecast, xlabel='Năm', ylabel='Vốn đầu tư' )
ax = fig1.gca()
ax.set_title("Biểu đồ thể nguồn vốn đầu tư và dự đoán đầu tư", size=28)

fig1.show()

fig2 = m.plot_components(forecast)
fig2.show()

print(forecast)
print(dataVonDauTuVND)

from fbprophet.plot import add_changepoints_to_plot

fig_air = m.plot(forecast)
a = add_changepoints_to_plot(fig_air.gca(), m, forecast)
