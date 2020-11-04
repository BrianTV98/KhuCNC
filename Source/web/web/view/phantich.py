# import thư viện
# ket nối csdl
# trend với prophet
# ham tao thư viện
# ghi tep binary

import pandas as pd
import pyodbc
from fbprophet import Prophet


conn = pyodbc.connect('Driver={SQL Server};'  # connect with SQL server
                      'Server=DESKTOP-05ICLAS\\SERVER2;'
                      'Database=DUAN_KHUCNC;'
                      'Trusted_Connection=yes;')

# read data
# VonDauTuVND
dataVonDauTuVND = pd.read_sql_query('SELECT NGAY_DANG_KY, VON_DAU_TU_VND FROM dbo.GIAY_CNDT', conn)  # get data from db
dataVonDauTuVND = dataVonDauTuVND.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_VND': 'y'})  # rename
dataVonDauTuVND.head()

# VonDauTuUSD
dataVonDauTuUSD = pd.read_sql_query('SELECT NGAY_DANG_KY,VON_DAU_TU_USD FROM dbo.GIAY_CNDT', conn)  # get data from db
dataVonDauTuUSD = dataVonDauTuUSD.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_USD': 'y'})  # rename
dataVonDauTuUSD.head()

def du_doan_tinh_hinh():
    dataVonDauTuVND = pd.read_sql_query('SELECT NGAY_DANG_KY, VON_DAU_TU_VND FROM dbo.GIAY_CNDT',conn)  # get data from db
    dataVonDauTuVND = dataVonDauTuVND.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_VND': 'y'})  # rename
    dataVonDauTuVND.head()
    print(dataVonDauTuVND)
    m = Prophet(daily_seasonality=True)
    m.fit(dataVonDauTuVND)
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

    return forecast
