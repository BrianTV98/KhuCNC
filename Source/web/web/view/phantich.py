# import thư viện
# ket nối csdl
# trend với prophet
# ham tao thư viện
# ghi tep binary

import pandas as pd
import pyodbc
import web.contrains.base_url as base_url
from fbprophet import Prophet
import pickle
import base64
import io
import urllib

# read data
# VonDauTuVND
dataVonDauTuVND = pd.read_sql_query('SELECT NGAY_DANG_KY, VON_DAU_TU_VND FROM dbo.GIAY_CNDT',
                                    base_url.conn)  # get data from db
dataVonDauTuVND = dataVonDauTuVND.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_VND': 'y'})  # rename
dataVonDauTuVND.head()

# VonDauTuUSD
dataVonDauTuUSD = pd.read_sql_query('SELECT NGAY_DANG_KY,VON_DAU_TU_USD FROM dbo.GIAY_CNDT',
                                    base_url.conn)  # get data from db
dataVonDauTuUSD = dataVonDauTuUSD.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_USD': 'y'})  # rename
dataVonDauTuUSD.head()


# Trend Model Truc Tiep Tu DB
# def du_doan_tinh_hinh():
#     dataVonDauTuVND = pd.read_sql_query('SELECT NGAY_DANG_KY, VON_DAU_TU_VND FROM dbo.GIAY_CNDT',base_url.conn)  # get data from db
#     dataVonDauTuVND = dataVonDauTuVND.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_VND': 'y'})  # rename
#     dataVonDauTuVND.head()
#     print(dataVonDauTuVND)
#     m = Prophet(daily_seasonality=True)
#     m.fit(dataVonDauTuVND)
#     future = m.make_future_dataframe(periods=1, freq='Y')  # so ngay can du bao
#     future.tail()
#     forecast = m.predict(future)
#     forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
#
#     return forecast
#
# def DuDoanDauTu_USD(soNam):
#     dataVonDauTuVND = pd.read_sql_query('SELECT NGAY_DANG_KY, VON_DAU_TU_USD FROM dbo.GIAY_CNDT',
#                                         base_url.conn)  # get data from db
#     dataVonDauTuVND = dataVonDauTuVND.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_USD': 'y'})  # rename
#     dataVonDauTuVND.head()
#     m = Prophet(daily_seasonality=True)
#     m.fit(dataVonDauTuVND)
#     future = m.make_future_dataframe(periods=1, freq='Y')  # so ngay can du bao
#     future.tail()
#     forecast = m.predict(future)
#     forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
#
#     return forecast


def DuDoanDauTuVND():
    m = pickle.load(open(base_url.base_url_model + '/VonDauTuVND.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    fig1 = m.plot(forecast, xlabel='Năm', ylabel='Vốn đầu tư VND')

    buf = io.BytesIO()
    fig1.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    return uri


def DuDoanDauTuUSD():
    m = pickle.load(open(base_url.base_url_model + '/VonDauTuUSD.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    fig1 = m.plot(forecast, xlabel='Năm', ylabel='Vốn đầu tư USD')

    buf = io.BytesIO()
    fig1.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    return uri

def DuDoanDauTu_SX():
    m = pickle.load(open(base_url.base_url_model + '/linhVucDauTu_SX.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    fig1 = m.plot(forecast, xlabel='Năm', ylabel='Vốn đầu tư Sản Xuất')

    buf = io.BytesIO()
    fig1.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    return uri


def DuDoanDauTu_DT_UT():
    m = pickle.load(open(base_url.base_url_model + '/linhVucDauTu_DT_UT.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    fig1 = m.plot(forecast, xlabel='Năm', ylabel='Vốn đầu tư R&D Đào Tạo-Ương tạo')

    buf = io.BytesIO()
    fig1.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    return uri

def DuDoanDauTu_DT_UT():
    m = pickle.load(open(base_url.base_url_model + '/linhVucDauTu_DT_UT.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    fig1 = m.plot(forecast, xlabel='Năm', ylabel='Vốn đầu tư R&D Đào Tạo-Ương tạo')

    buf = io.BytesIO()
    fig1.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    return uri

def DuDoanDauTu_DV():
    m = pickle.load(open(base_url.base_url_model + '/linhVucDauTu_DV.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    fig1 = m.plot(forecast, xlabel='Năm', ylabel='Vốn đầu tư Dịch Vụ')

    buf = io.BytesIO()
    fig1.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    return uri

def DuDoanDauTu_PTHT():
    m = pickle.load(open(base_url.base_url_model + '/linhVucDauTu_PTHT.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    fig1 = m.plot(forecast, xlabel='Năm', ylabel='Vốn đầu tư Phát triển hạ tầng')

    buf = io.BytesIO()
    fig1.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    return uri


def DuDoanDauTu_DT():
    m = pickle.load(open(base_url.base_url_model + '/linhVucDauTu_DT.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    fig1 = m.plot(forecast, xlabel='Năm', ylabel='Vốn đầu tư R&D Đào Tạo')

    buf = io.BytesIO()
    fig1.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    return uri

def DuDoanDauTu_DVCNC():
    m = pickle.load(open(base_url.base_url_model + '/linhVucDauTu_DT.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    fig1 = m.plot(forecast, xlabel='Năm', ylabel='Vốn đầu tư R&D Đào Tạo')

    buf = io.BytesIO()
    fig1.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)

    return uri


def DuDoanDauTu_KHAC():
    m = pickle.load(open(base_url.base_url_model + '/linhVucDauTu_KHAC.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    fig1 = m.plot(forecast, xlabel='Năm', ylabel='Vốn đầu tư vào lĩnh vực khác')

    buf = io.BytesIO()
    fig1.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    return uri
