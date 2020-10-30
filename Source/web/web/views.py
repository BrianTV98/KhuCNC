import pyodbc as pyodbc
from django.shortcuts import render
import pandas as pd
from django.views import View
from pyodbc import DatabaseError

from web.model.Company import Company
from web.model.ThongKeChung import ThongKeChung
from web.model.ThongKeDauTu import ThongKeDauTu

conn = pyodbc.connect('Driver={SQL Server};'  # connect with SQL server
                      'Server=DESKTOP-05ICLAS\\SERVER2;'
                      'Database=DUAN_KHUCNC;'
                      'Trusted_Connection=yes;')


def index(request):
    return render(request, 'indext.html')


def report(request):
    return render(request, 'report.html')


def thongke(request):
    # thong ke chung
    thongkeChung = pd.read_sql_query('EXEC [dbo].[SP_DASHBOARD_THONGKECHUNG]', conn)
    thongKeChungResult = [
        (ThongKeChung(row.SO_DU_AN_DT, row.DOANH_NGHIEP_HOAT_DONG, row.SO_DA_RD, row.LAO_DONG_CHAT_LUONG_CAO)) for
        index, row in thongkeChung.iterrows()]
    response = [vars(ob) for ob in thongKeChungResult]

    # thong ke tinh hinh dau tu

    # Cai nay dung roi
    val1 = request.GET.get("a")
    val2 = request.GET.get("b")

    if val1 is None:
        val1 = "2010"
    if val2 is None:
        val2 = "2020"

    try:
        sp = 'EXEC [dbo].[SP_DASHBOARD_THONGKE_VON_DAU_TU]' + " '" + val1 + "','" + val2+"'"
        thongkeDauTu = pd.read_sql_query(sp, conn)
        thongkegDauTuResult = [
            (ThongKeDauTu(row.TONGVONDAUTU_FDI, row.TONGVONDAUTU_VN, row.SOLUONG_FDI, row.SOLUONG_VN)) for
            index, row in thongkeDauTu.iterrows()]
        thongkeDauTuresponse = [vars(ob) for ob in thongkegDauTuResult]
        return render(request, 'thongke.html', {"thongkechung": response,
                                                "thongkeDauTu": thongkeDauTuresponse})
    except Exception as e:
        print(e)
        pass
    # Khi mà viết một trang muốn sử dụng nhiều request thì nên dùng class-based view
    # Trong đố sẽ như sau
    return render(request, 'thongke.html')
# class ThongKe(View):
#     def get(self, request, *args, **kwargs):
#         # Trong ddaay trar ve template
#         pass
#     def post(self, request, *ergs, **kwargs):
#         # Nhaajn ket qua tu request den cung trang
#         pass


def testData(request):
    thongkeChung = pd.read_sql_query('EXEC[dbo].[SP_DASHBOARD_THONGKECHUNG]', conn)
    thongKeChungResult = [
        (ThongKeChung(row.SO_DU_AN_DT, row.DOANH_NGHIEP_HOAT_DONG, row.SO_DA_RD, row.LAO_DONG_CHAT_LUONG_CAO)) for
        index, row in thongkeChung.iterrows()]
    response = [vars(ob) for ob in thongKeChungResult]
    return render(request, "testdata.html", {'thongkechung': response[0]})
