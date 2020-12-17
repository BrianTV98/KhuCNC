# import thư viện
# ket nối csdl
# trend với prophet
# ham tao thư viện
# ghi tep binary

import pandas as pd
import pyodbc
from fbprophet import Prophet
import datetime
from fbprophet.plot import add_changepoints_to_plot
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

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
dataVonDauTuVND['y'] = dataVonDauTuVND['y']
dataVonDauTuVND.head()
m = Prophet()
# create model and save model
m.fit(dataVonDauTuVND)
pickle.dump(m, open(base_url_model + '/VonDauTuVND.pickle', 'wb'))

# VonDauTuUSD
# dataVonDauTuUSD = pd.read_sql_query('SELECT NGAY_DANG_KY,VON_DAU_TU_USD FROM dbo.GIAY_CNDT', conn)  # get data from db
# dataVonDauTuUSD = dataVonDauTuUSD.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_USD': 'y'})  # rename
# dataVonDauTuUSD.head()
#
# # Linh Vuc Dau tU
# #SX, R&D_ĐT_UT, DV, PTHT, R&D_ĐT, DVCNC,VĐT
#
# #SX
linhVucDauTu_SX = pd.read_sql_query('EXEC SP_THONGKE_VON_DAU_TU_THEO_TUNG_LINH_VUC ' + "SX", conn)  # get data from db
linhVucDauTu_SX = linhVucDauTu_SX.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_USD': 'y'})  # rename

linhVucDauTu_SX.head()
m = Prophet()
m.fit(linhVucDauTu_SX)
pickle.dump(m, open(base_url_model + '/linhVucDauTu_SX.pickle', 'wb'))

#
# #R&D_ĐT_UT
linhVucDauTu_DT_UT = pd.read_sql_query("EXEC SP_THONGKE_VON_DAU_TU_THEO_TUNG_LINH_VUC N'R&D_ĐT_UT'",
                                       conn)  # get data from db
linhVucDauTu_DT_UT = linhVucDauTu_DT_UT.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_USD': 'y'})  # rename
linhVucDauTu_DT_UT.head()

m = Prophet()
m.fit(linhVucDauTu_DT_UT)
pickle.dump(m, open(base_url_model + '/linhVucDauTu_DT_UT.pickle', 'wb'))

#
# #DV
linhVucDauTu_DV = pd.read_sql_query('EXEC SP_THONGKE_VON_DAU_TU_THEO_TUNG_LINH_VUC ' + "DV", conn)  # get data from db
linhVucDauTu_DV = linhVucDauTu_DV.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_USD': 'y'})  # rename
linhVucDauTu_DV.head()
m = Prophet()
m.fit(linhVucDauTu_DV)

pickle.dump(m, open(base_url_model + '/linhVucDauTu_DV.pickle', 'wb'))

#
# #PTHT
linhVucDauTu_PTHT = pd.read_sql_query('EXEC SP_THONGKE_VON_DAU_TU_THEO_TUNG_LINH_VUC ' + "PTHT",
                                      conn)  # get data from db
linhVucDauTu_PTHT = linhVucDauTu_DV.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_USD': 'y'})  # rename
linhVucDauTu_PTHT.head()
m = Prophet()
m.fit(linhVucDauTu_PTHT)
pickle.dump(m, open(base_url_model + '/linhVucDauTu_PTHT.pickle', 'wb'))

#
# #R&D_ĐT
linhVucDauTu_DT = pd.read_sql_query("EXEC SP_THONGKE_VON_DAU_TU_THEO_TUNG_LINH_VUC N'R&D_ĐT'", conn)  # get data from db
linhVucDauTu_DT = linhVucDauTu_DT.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_USD': 'y'})  # rename
linhVucDauTu_DT.head()
if linhVucDauTu_DT.empty:
    print('linhVucDauTu_DT rong')
else:
    m = Prophet()
    m.fit(linhVucDauTu_DT)
    pickle.dump(m, open(base_url_model + '/linhVucDauTu_DT.pickle', 'wb'))

#
# #DVCNC
linhVucDauTu_DVCNC = pd.read_sql_query("EXEC SP_THONGKE_VON_DAU_TU_THEO_TUNG_LINH_VUC N'DVCNC'",
                                       conn)  # get data from db
linhVucDauTu_DVCNC = linhVucDauTu_DVCNC.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_USD': 'y'})  # rename
linhVucDauTu_DVCNC.head()

if linhVucDauTu_DVCNC.empty:
    print('linhVucDauTu_DVCNC rong')
else:
    m = Prophet()
    m.fit(linhVucDauTu_DVCNC)
    pickle.dump(m, open(base_url_model + '/linhVucDauTu_DVCNC.pickle', 'wb'))

#
#
# #VĐT
linhVucDauTu_VDT = pd.read_sql_query("EXEC SP_THONGKE_VON_DAU_TU_THEO_TUNG_LINH_VUC N'VĐT'", conn)  # get data from db
linhVucDauTu_VDT = linhVucDauTu_VDT.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_USD': 'y'})  # rename
linhVucDauTu_VDT.head()

if linhVucDauTu_VDT.empty:
    print('linhVucDauTu_VDT rong')
else:
    m = Prophet()
    m.fit(linhVucDauTu_VDT)
    pickle.dump(m, open(base_url_model + '/linhVucDauTu_VDT.pickle', 'wb'))

#
# #Khac
linhVucDauTu_KHAC = pd.read_sql_query("EXEC SP_THONGKE_VON_DAU_TU_THEO_TUNG_LINH_VUC N'KHAC'", conn)  # get data from db
linhVucDauTu_KHAC = linhVucDauTu_KHAC.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_USD': 'y'})  # rename
linhVucDauTu_KHAC.head()
m = Prophet()
m.fit(linhVucDauTu_KHAC)
pickle.dump(m, open(base_url_model + '/linhVucDauTu_KHAC.pickle', 'wb'))

# dau tu FDI
dauTuFDI = pd.read_sql_query("SELECT NGAY_DANG_KY,VON_DAU_TU_VND from  GIAY_CNDT WHERE MA_LH='FDI'",
                             conn)  # get data from db
dauTuFDI = dauTuFDI.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_VND': 'y'})  # rename
dauTuFDI.head()
m = Prophet()
m.fit(dauTuFDI)
pickle.dump(m, open(base_url_model + '/dautuFDI.pickle', 'wb'))

# dau tu VND
dauTuVN = pd.read_sql_query("SELECT NGAY_DANG_KY,VON_DAU_TU_VND from  GIAY_CNDT WHERE MA_LH='VN'",
                            conn)  # get data from db
dauTuVN = dauTuVN.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_VND': 'y'})  # rename
dauTuVN.head()
m = Prophet()
m.fit(dauTuVN)
pickle.dump(m, open(base_url_model + '/dautuVN.pickle', 'wb'))

# Tinh Hinh Dau TU Xuat Khau
tinhHinhXuatKhau = pd.read_sql_query(
    "SELECT CONVERT(DATETIME,CONCAT(NAM,'-',THANG,'-',01)) as NGAY_DANG_KY, KIM_NGACH_VND FROM GCNDT_LOAI_HINH_XNK_THEO_THANG JOIN LOAI_HINH_XNK on LOAI_HINH_XNK.MA_LOAI_HINH_XNK = GCNDT_LOAI_HINH_XNK_THEO_THANG.MA_LOAI_HINH_XNK WHERE LOAI_HINH_XNK.LOAI_HINH='X'",
    conn)  # get data from db
tinhHinhXuatKhau = tinhHinhXuatKhau.rename(columns={'NGAY_DANG_KY': 'ds', 'KIM_NGACH_VND': 'y'})  # rename
tinhHinhXuatKhau.head()
m = Prophet()
m.fit(tinhHinhXuatKhau)
pickle.dump(m, open(base_url_model + '/tinhHinhXuatKhau.pickle', 'wb'))

# Tinh Hinh Dau Tu nhap khau
tinhHinhNhapKhau = pd.read_sql_query(
    "SELECT CONVERT(DATETIME,CONCAT(NAM,'-',THANG,'-',01)) as NGAY_DANG_KY, KIM_NGACH_VND FROM GCNDT_LOAI_HINH_XNK_THEO_THANG JOIN LOAI_HINH_XNK on LOAI_HINH_XNK.MA_LOAI_HINH_XNK = GCNDT_LOAI_HINH_XNK_THEO_THANG.MA_LOAI_HINH_XNK WHERE LOAI_HINH_XNK.LOAI_HINH='N'",
    conn)  # get data from db
tinhHinhNhapKhau = tinhHinhNhapKhau.rename(columns={'NGAY_DANG_KY': 'ds', 'KIM_NGACH_VND': 'y'})  # rename
tinhHinhNhapKhau.head()
m = Prophet()
m.fit(tinhHinhNhapKhau)
pickle.dump(m, open(base_url_model + '/tinhHinhNhapKhau.pickle', 'wb'))

###---------------------------------------------------------------------------------------------------------------
# # Ti le lao dong

laodongchatluongcao = pd.read_sql_query("SELECT cast(cast(NAM as varchar(8)) as date) as NGAY_DANG_KY, SO_LD FROM DN_SO_LAO_DONG where MA_HV !='PTTH'",
    conn)  # get data from db
laodongchatluongcao = laodongchatluongcao.rename(columns={'NGAY_DANG_KY': 'ds', 'SO_LD': 'y'})  # rename
laodongchatluongcao.head()
m = Prophet()
m.fit(laodongchatluongcao)
pickle.dump(m, open(base_url_model + '/laodongchatluongcao.pickle', 'wb'))

# # m = Prophet(seasonality_mode='multiplicative')  # init prophet
m = Prophet()
# create model and save model
m.fit(dataVonDauTuVND)
pickle.dump(m, open(base_url_model + '/VonDauTuVND.pickle', 'wb'))

# # #
# m = Prophet()
# m.fit(dataVonDauTuUSD)
# # pickle.dump(m, open(base_url_model + '/VonDauTuUSD.pickle', 'wb'))
#
#
# m = Prophet()
# m.fit(linhVucDauTu_SX)
#
# pickle.dump(m, open(base_url_model + '/linhVucDauTu_SX.pickle', 'wb'))\
#
#
# m = Prophet()
# m.fit(linhVucDauTu_DT_UT)
# pickle.dump(m, open(base_url_model + '/linhVucDauTu_DT_UT.pickle', 'wb'))
#
#
# m = Prophet()
# m.fit(linhVucDauTu_DV)
#
# pickle.dump(m, open(base_url_model + '/linhVucDauTu_DV.pickle', 'wb'))
#
#
# m = Prophet()
# m.fit(linhVucDauTu_PTHT)
# pickle.dump(m, open(base_url_model + '/linhVucDauTu_PTHT.pickle', 'wb'))
#
# if linhVucDauTu_DT.empty:
#     print('linhVucDauTu_DT rong')
# else:
#     m = Prophet()
#     m.fit(linhVucDauTu_DT)
#     pickle.dump(m, open(base_url_model + '/linhVucDauTu_DT.pickle', 'wb'))
#
#
# m = Prophet()
# m.fit(linhVucDauTu_KHAC)
# pickle.dump(m, open(base_url_model + '/linhVucDauTu_KHAC.pickle', 'wb'))


# m = Prophet()
# m.fit(linhVucDauTu_DVCNC)
# pickle.dump(m, open(base_url_model + '/linhVucDauTu_DVCNC.pickle', 'wb'))
#
# m = Prophet()
# m.fit(linhVucDauTu_VDT)
# pickle.dump(m, open(base_url_model + '/linhVucDauTu_VDT.pickle', 'wb'))
## ---------------------- Funtion test result Prophet----------------------------------------

future = m.make_future_dataframe(periods=12 * 5, freq='M')  # so ngay can du bao
future.tail()

# dong ket noi sqlserver
# cursor.close()
conn.close()
forecast = m.predict(future)
# print(forecast)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
fig1 = m.plot(forecast, xlabel='Năm', ylabel='Vốn đầu tư', figsize=(10, 10))

ax = fig1.gca()

arr = np.array([datetime.datetime(i, 1, 1) for i in
                range(pd.to_datetime(min(forecast["ds"])).year, pd.to_datetime(max(forecast["ds"])).year + 2)])
fig1.suptitle("Biểu đồ thể nguồn vốn đầu tư và dự đoán đầu tư")
years = mdates.YearLocator()  # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)

fig1.autofmt_xdate()

ax.set_xticks(arr)
fig1.show()
plt.savefig('C:\\Users\\Mylov\\Desktop\\abc.png')

# a = add_changepoints_to_plot(fig1.gca(), m, forecast)

# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2 * np.pi * t)
#
fig, ax = plt.subplots()
ax.plot(forecast[["ds", "yhat"]].sort_values('ds', ascending=True))

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

#fig.savefig("test.png")
#plt.show()
#


# fig2 = m.plot_components(forecast)
# fig2.show()
# fig = m.plot_components(forecast)
# fig.get_children()[3].set_xlabel('Day of month')
# fig.get_children()[1].show()
# print(forecast)
# print(dataVonDauTuVND)

# from fbprophet.plot import add_changepoints_to_plot
#
# fig_air = m.plot(forecast)
