import pandas as pd
import pyodbc
from web.contrains.base_url import base_url_model, conn
from web.model.ThongKeDauTu import ThongKeDauTu
from web.model.YearFromTo import YearFromTo


def getYearFromTo():
    data = pd.read_sql_query('Exec SP_DASHBOARD_THONGKE_GET_YEAR', conn)  # get dat
    result = [
        (YearFromTo(row.MinYear, row.MaxYear)) for
        index, row in data.iterrows()]
    result_to_json = [vars(ob) for ob in result]
    return result_to_json[0]


def getThongDauTu(val1, val2):
    sp = 'EXEC [dbo].[SP_DASHBOARD_THONGKE_VON_DAU_TU]' + " '" + val1 + "','" + val2 + "'"
    thongkeDauTu = pd.read_sql_query(sp, conn)
    thongkegDauTuResult = [
        (ThongKeDauTu(row.TONGVONDAUTU_FDI, row.TONGVONDAUTU_VN, row.SOLUONG_FDI, row.SOLUONG_VN)) for
        index, row in thongkeDauTu.iterrows()]
    thongkeDauTuresponse = [vars(ob) for ob in thongkegDauTuResult]

    return thongkeDauTuresponse


def thongKeDanhNghiepHoatDong():
    query = "SELECT  SO_CNDKKD, TEN_DN FROM dbo.DOANHNGHIEP  WHERE dbo.DOANHNGHIEP.DA_GIAI_THE =0"
    thongkeDauTu = pd.read_sql_query(query, conn)


    return thongkeDauTu



