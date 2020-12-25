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
import numpy as np
import matplotlib.dates as mdates
import datetime
import matplotlib.pyplot as plt

# read data
# VonDauTuVND
from web.model.ThongKeLinhVucCNC import ThongKeLinhVucCNC
from web.model.XuatNhapKhau import XuatNhapKhau

dataVonDauTuVND = pd.read_sql_query('SELECT NGAY_DANG_KY, VON_DAU_TU_VND FROM dbo.GIAY_CNDT',
                                    base_url.conn)  # get data from db
dataVonDauTuVND = dataVonDauTuVND.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_VND': 'y'})  # rename
dataVonDauTuVND.head()

# VonDauTuUSD
dataVonDauTuUSD = pd.read_sql_query('SELECT NGAY_DANG_KY,VON_DAU_TU_USD FROM dbo.GIAY_CNDT',
                                    base_url.conn)  # get data from db
dataVonDauTuUSD = dataVonDauTuUSD.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_USD': 'y'})  # rename
dataVonDauTuUSD.head()


def DuDoanDauTuVND():
    m = pickle.load(open(base_url.base_url_model + '\\VonDauTuVND.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    thongKeTyLeChiRDResult = [
        (SoLieuThongKe(pd.to_datetime(row.ds).date().isoformat(), row.yhat)) for
        index, row in forecast.iterrows()]
    thongKeTyLeChiRDResponse = [vars(ob) for ob in thongKeTyLeChiRDResult]
    print(thongKeTyLeChiRDResponse)
    return thongKeTyLeChiRDResponse


def DuDoanDauTuUSD():
    m = pickle.load(open(base_url.base_url_model + '\\VonDauTuUSD.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)

    phanTichArray = [
        (SoLieuThongKe(pd.to_datetime(row.ds).date().isoformat(), row.yhat)) for
        index, row in forecast.iterrows()]
    phanTichJson = [vars(ob) for ob in phanTichArray]
    return phanTichJson


def DuDoanDauTu_SX():
    m = pickle.load(open(base_url.base_url_model + '\\linhVucDauTu_SX.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    phanTichArray = [
        (SoLieuThongKe(pd.to_datetime(row.ds).date().isoformat(), row.yhat)) for
        index, row in forecast.iterrows()]
    phanTichJson = [vars(ob) for ob in phanTichArray]
    return phanTichJson


def DuDoanDauTu_DT_UT():
    m = pickle.load(open(base_url.base_url_model + '\\linhVucDauTu_DT_UT.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)

    phanTichArray = [
        (SoLieuThongKe(pd.to_datetime(row.ds).date().isoformat(), row.yhat)) for
        index, row in forecast.iterrows()]
    phanTichJson = [vars(ob) for ob in phanTichArray]
    return phanTichJson


def DuDoanDauTu_DT_UT():
    m = pickle.load(open(base_url.base_url_model + '\\linhVucDauTu_DT_UT.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)

    phanTichArray = [
        (SoLieuThongKe(pd.to_datetime(row.ds).date().isoformat(), row.yhat)) for
        index, row in forecast.iterrows()]
    phanTichJson = [vars(ob) for ob in phanTichArray]
    return phanTichJson


def DuDoanDauTu_DV():
    m = pickle.load(open(base_url.base_url_model + '\\linhVucDauTu_DV.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    phanTichArray = [
        (SoLieuThongKe(pd.to_datetime(row.ds).date().isoformat(), row.yhat)) for
        index, row in forecast.iterrows()]
    phanTichJson = [vars(ob) for ob in phanTichArray]
    return phanTichJson


def DuDoanDauTu_PTHT():
    m = pickle.load(open(base_url.base_url_model + '\\linhVucDauTu_PTHT.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    phanTichArray = [
        (SoLieuThongKe(pd.to_datetime(row.ds).date().isoformat(), row.yhat)) for
        index, row in forecast.iterrows()]
    phanTichJson = [vars(ob) for ob in phanTichArray]
    return phanTichJson


def DuDoanDauTu_DT():
    m = pickle.load(open(base_url.base_url_model + '\\linhVucDauTu_DT.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    phanTichArray = [
        (SoLieuThongKe(pd.to_datetime(row.ds).date().isoformat(), row.yhat)) for
        index, row in forecast.iterrows()]
    phanTichJson = [vars(ob) for ob in phanTichArray]
    return phanTichJson


def DuDoanDauTu_DVCNC():
    m = pickle.load(open(base_url.base_url_model + '\\linhVucDauTu_DT.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    phanTichArray = [
        (SoLieuThongKe(pd.to_datetime(row.ds).date().isoformat(), row.yhat)) for
        index, row in forecast.iterrows()]
    phanTichJson = [vars(ob) for ob in phanTichArray]
    return phanTichJson


def DuDoanDauTu_KHAC():
    m = pickle.load(open(base_url.base_url_model + '\\linhVucDauTu_KHAC.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    phanTichArray = [
        (SoLieuThongKe(pd.to_datetime(row.ds).date().isoformat(), row.yhat)) for
        index, row in forecast.iterrows()]
    phanTichJson = [vars(ob) for ob in phanTichArray]
    return phanTichJson


def thongKeVonDauTuVND():
    query = "Select * From V_VonDauTuVND"
    dataVonDauTuVND = pd.read_sql_query(query,
                                        base_url.conn)
    thongKeArray = [
        (SoLieuThongKe(row.ds, row.yhat)) for
        index, row in dataVonDauTuVND.iterrows()]
    thongKeJson = [vars(ob) for ob in thongKeArray]
    return thongKeJson;


class SoLieuThongKe:
    def __init__(self, ds, yhat):
        self.ds = ds
        self.yhat = yhat

        #####--------------------------------- Du Bao FDI


def vThongKeXuatKhau():
    query = " Exec SP_THONGKE_XUAT_NHAP_KHAU 'X'"
    thongKeXuatKhau = pd.read_sql_query(query,
                                        base_url.conn)
    thongKeArray = [
        (XuatNhapKhau(row.SO_CNDKKD, row.TEN_DN, pd.to_datetime(row.NGAY_DANG_KY).date().isoformat(),
                      row.KIM_NGACH_VND)) for
        index, row in thongKeXuatKhau.iterrows()]
    thongKeJson = [vars(ob) for ob in thongKeArray]
    return thongKeJson;


#
def DuDoanXuatKhau():
    m = pickle.load(open(base_url.base_url_model + '\\tinhHinhXuatKhau.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    phanTichArray = [
        (SoLieuThongKe(pd.to_datetime(row.ds).date().isoformat(), row.yhat)) for
        index, row in forecast.iterrows()]
    phanTichJson = [vars(ob) for ob in phanTichArray]
    return phanTichJson


## ---- Thong Ke Nhap Khauu

def vThongKeNhapKhau():
    query = " Exec SP_THONGKE_XUAT_NHAP_KHAU 'N'"
    thongKeXuatKhau = pd.read_sql_query(query,
                                        base_url.conn)
    thongKeArray = [
        (XuatNhapKhau(row.SO_CNDKKD, row.TEN_DN, pd.to_datetime(row.NGAY_DANG_KY).date().isoformat(),
                      row.KIM_NGACH_VND)) for
        index, row in thongKeXuatKhau.iterrows()]
    thongKeJson = [vars(ob) for ob in thongKeArray]
    return thongKeJson;


#
#
#
def DuDoanNhapKhau():
    m = pickle.load(open(base_url.base_url_model + '\\tinhHinhNhapKhau.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    phanTichArray = [
        (SoLieuThongKe(pd.to_datetime(row.ds).date().isoformat(), row.yhat)) for
        index, row in forecast.iterrows()]
    phanTichJson = [vars(ob) for ob in phanTichArray]
    return phanTichJson


# thongke dau tu ngoai FDI
def vThongKeFDI():
    query = "Select datepart(yyyy, GIAY_CNDT.NGAY_DANG_KY) as NGAY_DANG_KY, Sum(VON_DAU_TU_VND) as VonDauTu From GIAY_CNDT JOIN DOANHNGHIEP on GIAY_CNDT.SO_CNDKKD = DOANHNGHIEP.SO_CNDKKD where MA_LH ='FDI' group by datepart(yyyy, GIAY_CNDT.NGAY_DANG_KY)"

    thongKeXuatKhau = pd.read_sql_query(query,
                                        base_url.conn)
    thongKeArray = [
        (SoLieuThongKe( pd.to_datetime(row.NGAY_DANG_KY).date().isoformat(),
                      row.VonDauTu)) for
        index, row in thongKeXuatKhau.iterrows()]
    thongKeJson = [vars(ob) for ob in thongKeArray]
    return thongKeJson;


def DuDoanFDI():
    m = pickle.load(open(base_url.base_url_model + '\\dautuFDI.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    phanTichArray = [
        (SoLieuThongKe(pd.to_datetime(row.ds).date().isoformat(), row.yhat)) for
        index, row in forecast.iterrows()]
    phanTichJson = [vars(ob) for ob in phanTichArray]
    return phanTichJson


def vthongKeDauTuNoi():
    query = "Select datepart(yyyy, GIAY_CNDT.NGAY_DANG_KY) as NGAY_DANG_KY, Sum(VON_DAU_TU_VND) as VonDauTu From GIAY_CNDT JOIN DOANHNGHIEP on GIAY_CNDT.SO_CNDKKD = DOANHNGHIEP.SO_CNDKKD where MA_LH ='VN' group by datepart(yyyy, GIAY_CNDT.NGAY_DANG_KY)"

    thongKeXuatKhau = pd.read_sql_query(query,
                                        base_url.conn)
    thongKeArray = [
        (SoLieuThongKe( pd.to_datetime(row.NGAY_DANG_KY).date().isoformat(),
                      row.VonDauTu)) for
        index, row in thongKeXuatKhau.iterrows()]
    thongKeJson = [vars(ob) for ob in thongKeArray]
    return thongKeJson

def DuDoanDauTuNoi():
    m = pickle.load(open(base_url.base_url_model + '\\dautuVN.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    phanTichArray = [
        (SoLieuThongKe(pd.to_datetime(row.ds).date().isoformat(), row.yhat)) for
        index, row in forecast.iterrows()]
    phanTichJson = [vars(ob) for ob in phanTichArray]
    return phanTichJson


def vThongKeLaoDongChatLuongCao():
    query = "SELECT cast(cast(NAM as varchar(8)) as date) as NGAY, SO_LD FROM DN_SO_LAO_DONG where MA_HV !='PTTH'"
    thongKe = pd.read_sql_query(query,
                                        base_url.conn)
    thongKeArray = [
        (SoLieuThongKe(pd.to_datetime(row.NGAY).date().isoformat(),
                      row.SO_LD)) for
        index, row in thongKe.iterrows()]
    thongKeJson = [vars(ob) for ob in thongKeArray]
    return thongKeJson

def DuDoanNguoiLaoDong():
    m = pickle.load(open(base_url.base_url_model + '\\laodongchatluongcao.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    phanTichArray = [
        (SoLieuThongKe(pd.to_datetime(row.ds).date().isoformat(), row.yhat)) for
        index, row in forecast.iterrows()]
    phanTichJson = [vars(ob) for ob in phanTichArray]
    return phanTichJson

def thongKeLinhVucCNC_linhVuc_SL_():
    thongKe = pd.read_sql_query("EXEC SP_THONGKE_DAU_TU_THEO_LINH_VUC_ALL",
                                base_url.conn)
    from web.model.ThongKeLinhVucAll import ThongKeLinhVucAll
    thongKeArray = [
        (ThongKeLinhVucAll(row.MA_CTHTDT, row.TONGSO,
                           row.VONDAUTU)) for
        index, row in thongKe.iterrows()]

    for x in thongKeArray:
        x.MA_CTHTDT = x.MA_CTHTDT[0]
    thongKeJson = [vars(ob) for ob in thongKeArray]
    return thongKeJson


def thongKeLinhVucCNC_linhvucCNC_SL():
    thongKe = pd.read_sql_query("EXEC SP_THONGKE_DAU_TU_THEO_LINH_VUC_CNC",
                                base_url.conn)
    thongKeArray = [
        (ThongKeLinhVucCNC(row.MA_LVCNC,row.DIEN_GIAI,row.TONGSO,
                           row.VONDAUTU)) for
        index, row in thongKe.iterrows()]
    thongKeJson = [vars(ob) for ob in thongKeArray]
    return thongKeJson






