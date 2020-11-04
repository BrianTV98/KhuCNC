import pyodbc
import pandas as pd

from web.model.RD_ViewModel import RD_ViewModel

conn = pyodbc.connect('Driver={SQL Server};'  # connect with SQL server
                      'Server=DESKTOP-05ICLAS\\SERVER2;'
                      'Database=DUAN_KHUCNC;'
                      'Trusted_Connection=yes;')

def thongketylechiRD():
    sp = "SELECT* FROM V_RD"
    thongKeTyLeChiRD = pd.read_sql_query(sp, conn)
    thongKeTyLeChiRDResult = [
        (RD_ViewModel(row.TEN_DN, row.NAM, row.TY_LE_CHI_PHI_RD, row.TY_LE_DH_TREN_DH_THAM_GIA_RD, row.KINH_PHI)) for
        index, row in thongKeTyLeChiRD.iterrows()]
    print(thongKeTyLeChiRD)
    thongKeTyLeChiRDResponse = [vars(ob) for ob in thongKeTyLeChiRDResult]
    return thongKeTyLeChiRDResponse;