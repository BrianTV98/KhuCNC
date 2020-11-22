import pyodbc
import pandas as pd
import web.contrains.base_url as base_url

from web.model.RD_ViewModel import RD_ViewModel
from web.model.TyLeLoaiHinhDauTu import TyLeLoaiHinhDauTu
from web.view.phantich import SoLieuThongKe


def thongketylechiRD():
    sp = "SELECT * FROM V_RD"
    thongKeTyLeChiRD = pd.read_sql_query(sp, base_url.conn)
    thongKeTyLeChiRDResult = [
        (RD_ViewModel(row.TEN_DN, row.NAM, row.TY_LE_CHI_PHI_RD, row.TY_LE_DH_TREN_DH_THAM_GIA_RD, row.KINH_PHI)) for
        index, row in thongKeTyLeChiRD.iterrows()]
    thongKeTyLeChiRDResponse = [vars(ob) for ob in thongKeTyLeChiRDResult]

    return thongKeTyLeChiRDResponse


def thongKeTyLeLoaiHinhDauTu():
    try:
        query = 'Exec SP_THONGKE_TY_LE_DAU_TU'

        data = pd.read_sql_query(query, base_url.conn)

        tyleloaihinhdautu = [
            (TyLeLoaiHinhDauTu(row.MA_HTDT, row.HINH_THUC_DAU_TU, row.SO_LUONG, row.TY_LE_PHAN_TRAM))
            for index, row in data.iterrows()
        ]

        tyleloaihinhdautuResult = [vars(ob) for ob in tyleloaihinhdautu]
        a = [desc.strip() for desc in data['MA_HTDT']]
        print(a)

        return a
    except Exception as e:
        print("err")
        print(e)
        return
    pass


#### Thong Ke
def thongKeVonDauTuVND():
    query = "Select * From V_VonDauTuVND"
    dataVonDauTuVND = pd.read_sql_query(query,
                                        base_url.conn)
    thongKeArray = [
        (SoLieuThongKe(row.ds, row.yhat)) for
        index, row in dataVonDauTuVND.iterrows()]
    thongKeJson = [vars(ob) for ob in thongKeArray]
    return thongKeJson


def thongKeVonDauTuSX():
    query = "Select * From V_VonDauTuSX"
    dataVonDauTuVND = pd.read_sql_query(query,
                                        base_url.conn)
    thongKeArray = [
        (SoLieuThongKe(row.ds, row.yhat)) for
        index, row in dataVonDauTuVND.iterrows()]
    thongKeJson = [vars(ob) for ob in thongKeArray]
    return thongKeJson


def thongKeVonDauTuPTHT():
    query = "Select * From V_VonDauTuPTHT"
    dataVonDauTuVND = pd.read_sql_query(query,
                                        base_url.conn)
    thongKeArray = [
        (SoLieuThongKe(row.ds, row.yhat)) for
        index, row in dataVonDauTuVND.iterrows()]
    thongKeJson = [vars(ob) for ob in thongKeArray]
    return thongKeJson


def thongKeVonDauTuKHAC():
    query = "Select * From V_VonDauTuKhac"
    dataVonDauTuVND = pd.read_sql_query(query,
                                        base_url.conn)
    thongKeArray = [
        (SoLieuThongKe(row.ds, row.yhat)) for
        index, row in dataVonDauTuVND.iterrows()]
    thongKeJson = [vars(ob) for ob in thongKeArray]
    return thongKeJson


def thongKeVonDauTuDV():
    query = "Select * From V_VonDauTuDV"
    dataVonDauTuVND = pd.read_sql_query(query,
                                        base_url.conn)
    thongKeArray = [
        (SoLieuThongKe(row.ds, row.yhat)) for
        index, row in dataVonDauTuVND.iterrows()]
    thongKeJson = [vars(ob) for ob in thongKeArray]
    return thongKeJson


def thongKeVonDauTuDT_UT():
    query = "Select * From V_VonDauTuDT_UT"
    dataVonDauTuVND = pd.read_sql_query(query,
                                        base_url.conn)
    thongKeArray = [
        (SoLieuThongKe(row.ds, row.yhat)) for
        index, row in dataVonDauTuVND.iterrows()]
    thongKeJson = [vars(ob) for ob in thongKeArray]
    return thongKeJson
