import pyodbc as pyodbc
from django.shortcuts import render
import pandas as pd

from web.contrains.base_url import base_url_model, conn
from web.model.ThongKeChung import ThongKeChung
from web.model.ThongKeDauTu import ThongKeDauTu
from web.view.indext import getYearFromTo, getThongDauTu
from web.view.phantich import DuDoanDauTuVND, DuDoanDauTuUSD, DuDoanDauTu_SX, DuDoanDauTu_DT_UT, DuDoanDauTu_DV, \
    DuDoanDauTu_PTHT, DuDoanDauTu_DT, DuDoanDauTu_KHAC, vThongKeXuatKhau, DuDoanXuatKhau, vThongKeNhapKhau, \
    DuDoanNhapKhau, vThongKeFDI, DuDoanFDI, vthongKeDauTuNoi, DuDoanDauTuNoi, vThongKeLaoDongChatLuongCao, \
    DuDoanNguoiLaoDong, thongKeLinhVucCNC_linhVuc_SL_, thongKeLinhVucCNC_linhvucCNC_SL
from web.view.thongke import thongketylechiRD, thongKeTyLeLoaiHinhDauTu, thongKeVonDauTuVND, thongKeVonDauTuSX, \
    thongKeVonDauTuPTHT, thongKeVonDauTuDV, thongKeVonDauTuKHAC, thongKeVonDauTuDT_UT
import pickle
from django.http import HttpResponseRedirect
import pandas as pd
import math
from fbprophet import Prophet

import pystan

import matplotlib.pyplot as plt
import base64
import io
import urllib
import json

# url(r'^createPost', CreatePost.as_view())

# from testapp.models import User
# from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     template = 'index.html'
#     return render(request, template)
#
#
# def create_user(request):
#     if request.method == "POST":
#         fname = request.POST['fname']
#         lname = request.POST['lname']


def index(request):
    # thong ke chung
    thongkeChung = pd.read_sql_query('EXEC [dbo].[SP_DASHBOARD_THONGKECHUNG]', conn)
    thongKeChungResult = [
        (ThongKeChung(row.SO_DU_AN_DT, row.DOANH_NGHIEP_HOAT_DONG, row.SO_DA_RD, row.LAO_DONG_CHAT_LUONG_CAO)) for
        index, row in thongkeChung.iterrows()]
    response = [vars(ob) for ob in thongKeChungResult]

    # thong ke vong dau tu
    from_to = getYearFromTo()

    val1 = request.POST.get("fname");
    val2 = request.POST.get("lname")

    if val1 is None or val1 == "":
        val1 = "2003"
    if val2 is None or val2 == "":
        val2 = "2020"

    val3 = str(val1)
    val4 = str(val2)

    query = ' SELECT TEN_DU_AN_TIENG_VIET, TEN_DU_AN_VIET_TAT,MUC_TIEU_HOAT_DONG,VON_DAU_TU_VND FROM dbo.GIAY_CNDT';
    data = pd.read_sql_query(query, conn)

    return render(request, 'indext.html', {"thongkechung": response[0],
                                           "thongkeDauTu": getThongDauTu(val3, val4)[0],
                                           "year_from_to": from_to,
                                           # "thongkeduandautu": thong_ke_du_an_dau_tu(),
                                           # "thong_ke_hoat_dong_rd": thong_ke_hoat_dong_rd(),
                                           # "thongkedoanhnghiephoatodng": thong_ke_doanh_nghiep_hoat_dong()
                                           })


def report(request):
    return render(request, 'report.html')


def thongke(request):
    # thong ke chung
    thongkeChung = pd.read_sql_query('EXEC [dbo].[SP_DASHBOARD_THONGKECHUNG]', conn)
    thongKeChungResult = [
        (ThongKeChung(row.SO_DU_AN_DT, row.DOANH_NGHIEP_HOAT_DONG, row.SO_DA_RD, row.LAO_DONG_CHAT_LUONG_CAO)) for
        index, row in thongkeChung.iterrows()]
    response = [vars(ob) for ob in thongKeChungResult]

    # Cai nay dung roi
    val1 = request.GET.get("a")
    val2 = request.GET.get("b")

    if val1 is None:
        val1 = "2010"
    if val2 is None:
        val2 = "2020"

    try:

        a = thongKeTyLeLoaiHinhDauTu()

        return render(request, 'thongke.html', {"thongkechung": response[0],
                                                "tylechiRd": thongketylechiRD(),
                                                "tyleloaihinhdautu": a})

    except Exception as e:
        print("Hieu tesst nef")
        print(e)
        pass
    # Khi mà viết một trang muốn sử dụng nhiều request thì nên dùng class-based view
    # Trong đố sẽ như sau
    return render(request, 'thongke.html')


def phantich(request):
    # m = pickle.load(open(base_url_model + '/VonDauTuVND.pickle', 'rb'))
    # future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    # future.tail()
    # forecast = m.predict(future)
    # forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    # fig1 = m.plot(forecast, xlabel='Năm', ylabel='Vốn đầu tư')
    # ax = fig1.gca()
    # ax.set_title("Biểu đồ thể nguồn vốn đầu tư và dự đoán đầu tư", size=28)
    # # fig1.show()
    #
    # buf = io.BytesIO()
    # fig1.savefig(buf, format='png')
    # buf.seek(0)
    # string = base64.b64encode(buf.read())
    # uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    #

    # duDoanDauTuUSD_uri = DuDoanDauTuUSD()
    # DuDoanDauTu_SX_uri = DuDoanDauTu_SX()
    # duDoanDauTu_DT_UT_uri = DuDoanDauTu_DT_UT()

    # buf2 = io.BytesIO()
    # fig2 = m.plot_components(forecast)
    # fig2.savefig(buf2, format='png')
    # buf2.seek(0)
    # string2 = base64.b64encode(buf2.read())
    # uri2 = 'data:image/png;base64,' + urllib.parse.quote(string2)
    #
    # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    # sizes = [15, 30, 45, 10]
    # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #
    # fig1, ax1 = plt.subplots()
    # ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    #         shadow=True, startangle=90)
    # ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    #
    # tyleloaihinhdautu = thongKeTyLeLoaiHinhDauTu(conn)

    #
    # # test

    # test

    query = 'Exec SP_THONGKE_TY_LE_DAU_TU'

    data = pd.read_sql_query(query, conn)

    lable = [desc.strip() for desc in data['HINH_THUC_DAU_TU']]
    value = [desc for desc in data['SO_LUONG']]

    args = {
        # 'image_dau_tu_VND': DuDoanDauTuVND(),
        # # Cần làm
        # 'thong_ke_dau_tu_VND': thongKeVonDauTuVND(),
        # 'image_dau_tu_USD': DuDoanDauTuUSD(),
        # 'image_dau_tu_SX': DuDoanDauTu_SX(),
        # 'image_dau_tu_DT_UT': DuDoanDauTu_DT_UT(),
        # 'image_dau_tu_DV': DuDoanDauTu_DV(),
        # 'image_dau_tu_PTHT': DuDoanDauTu_PTHT(),

        # 'image_dau_tu_DT': DuDoanDauTu_DT(),
        # 'image_dau_tu_VDT': DuDoanDauTu_VDT(),
        # 'image_dau_tu_KHAC': DuDoanDauTu_SX_uri,

        "lable": lable,
        "value": value}
    return render(request, 'phantich.html', args)


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


# new 19/11/2020

def vonVND(request):
    return render(request, "phantich_von_dt_vnd.html", {'thongke': thongKeVonDauTuVND(),
                                                        'phantich': DuDoanDauTuVND()})


# 5 cai

def vonSX(request):
    return render(request, "phantich_von_dt_SX.html", {'thongke': thongKeVonDauTuSX(),
                                                       'phantich': DuDoanDauTu_SX()})


def vonPTHT(request):
    return render(request, "phantich_von_dt_PTHT.html", {'thongke': thongKeVonDauTuPTHT(),
                                                         'phantich': DuDoanDauTu_PTHT()})


def vonDV(request):
    return render(request, "phantich_von_dt_DV.html", {'thongke': thongKeVonDauTuDV(),
                                                       'phantich': DuDoanDauTu_DV()})


def vonKhac(request):
    return render(request, "phantich_von_dt_Khac.html", {'thongke': thongKeVonDauTuKHAC(),
                                                         'phantich': DuDoanDauTu_KHAC()})


def vonDT_UT(request):
    return render(request, "phantich_von_dt_DT_UT.html", {'thongke': thongKeVonDauTuDT_UT(),
                                                          'phantich': DuDoanDauTu_DT_UT()})


# thong_ke_
def thongKe_kinh_phi(request):
    return render(request, "thongke_kinh_phi.html", {"thongke": thongketylechiRD()})


def thongke_tile_ld_clc_tham_gia_rd(request):
    return render(request, "thongke_lao_dong_clc_tham_gia_rd.html", {"thongke": thongketylechiRD()})


def thongke_doanh_nghiep_hoat_dong(request):
    query = ' SELECT TEN_DU_AN_TIENG_VIET, TEN_DU_AN_VIET_TAT,MUC_TIEU_HOAT_DONG,VON_DAU_TU_VND FROM dbo.GIAY_CNDT';
    data = pd.read_sql_query(query, conn)

    dataResult = [
        (DoanhNghiepHoatDong(row.SO_CNDKKD, row.TEN_DU_AN_TIENG_VIET, row.TEN_DU_AN_VIET_TAT, row.MUC_TIEU_HOAT_DONG,
                             row.VON_DAU_TU_VND)) for
        index, row in data.iterrows()]
    response = [vars(ob) for ob in dataResult]

    return render(request, "thong_ke_doanh_nghiep_hoat_dong.html", {"thongke": response})


def thong_ke_du_an_dau_tu(request):
    # query = 'SELECT TEN_DU_AN_TIENG_VIET, TEN_DU_AN_VIET_TAT,MUC_TIEU_HOAT_DONG,VON_DAU_TU_VND FROM dbo.GIAY_CNDT'
    query = 'EXEC [dbo].[Test]'

    data = pd.read_sql_query(query, conn)

    dataResult = [
        (DoanhNghiepHoatDong(row.SO_CNDKKD, row.TEN_DN, row.TEN_DU_AN_TIENG_VIET, row.TEN_DU_AN_VIET_TAT,
                             row.MUC_TIEU_HOAT_DONG,
                             row.VON_DAU_TU_VND)) for
        index, row in data.iterrows()]
    # fix bug
    for x in dataResult:
        x.SO_CNDKKD = x.SO_CNDKKD[0]
        x.TEN_DN = x.TEN_DN[0]
        x.VON_DAU_TU_VND = x.VON_DAU_TU_VND[0]

    response = [vars(ob) for ob in dataResult]

    return render(request, "thong_ke_du_an_dau_tu.html", {"thongke": response})


# trang nay cua dashboard
def thong_ke_doanh_nghiep_hoat_dong(request):
    query = 'SET NOCOUNT ON; SELECT GIAY_CNDT.SO_CNDKKD,TEN_DN,TEN_DU_AN_TIENG_VIET,TEN_DU_AN_VIET_TAT,MUC_TIEU_HOAT_DONG,VON_DAU_TU_VND FROM dbo.DOANHNGHIEP   Left join GIAY_CNDT on GIAY_CNDT.SO_CNDKKD =DOANHNGHIEP.SO_CNDKKD WHERE dbo.DOANHNGHIEP.DA_GIAI_THE =0';
    # query = 'EXEC [dbo].[Test]'
    data = pd.read_sql_query(query, conn)

    dataResult = [
        (DoanhNghiepHoatDong(row.SO_CNDKKD, row.TEN_DN, row.TEN_DU_AN_TIENG_VIET, row.TEN_DU_AN_VIET_TAT,
                             row.MUC_TIEU_HOAT_DONG,
                             row.VON_DAU_TU_VND)) for
        index, row in data.iterrows()]

    # fix bug
    for x in dataResult:
        x.TEN_DN = x.TEN_DN[0]
        x.SO_CNDKKD = x.SO_CNDKKD[0]
        x.VON_DAU_TU_VND = x.VON_DAU_TU_VND[0]
    response = [vars(ob) for ob in dataResult]

    return render(request, "thong_ke_doanh_nghiep_hoat_dong.html", {"thongke": response})


def thong_ke_hoat_dong_rd(request):
    query = "SELECT GIAY_CNDT.SO_GCNDT,GIAY_CNDT.TEN_DU_AN_TIENG_VIET,GIAY_CNDT.TEN_DU_AN_VIET_TAT,GIAY_CNDT.NGAY_DANG_KY,GCNDT_DANG_KY_HOAT_DONG_RD.NOI_DUNG,GCNDT_DANG_KY_HOAT_DONG_RD.HINH_THUC_RD   FROM DBO.GCNDT_DANG_KY_HOAT_DONG_RD JOIN GIAY_CNDT ON GIAY_CNDT.SO_GCNDT = GCNDT_DANG_KY_HOAT_DONG_RD.SO_GCNDT"
    data = pd.read_sql_query(query, conn)

    dataResult = [
        (HoatDongRD(row.SO_GCNDT, row.TEN_DU_AN_TIENG_VIET, row.TEN_DU_AN_VIET_TAT,
                    pd.to_datetime(row.NGAY_DANG_KY).date().isoformat(),
                    row.NOI_DUNG, row.HINH_THUC_RD
                    ))
        for
        index, row in data.iterrows()]

    # fix bug
    for x in dataResult:
        x.SO_GCNDT = x.SO_GCNDT[0]
        x.TEN_DU_AN_TIENG_VIET = x.TEN_DU_AN_TIENG_VIET[0]
        x.HINH_THUC_RD = x.HINH_THUC_RD[0]

    response = [vars(ob) for ob in dataResult]

    return render(request, "thong_ke_hoat_dong_rd.html", {"thongke": response})


class HoatDongRD:
    def __init__(self, SO_GCNDT, TEN_DU_AN_TIENG_VIET, TEN_DU_AN_VIET_TAT, NGAY_DANG_KY, NOI_DUNG, HINH_THUC_RD):
        self.SO_GCNDT = SO_GCNDT,
        self.TEN_DU_AN_TIENG_VIET = TEN_DU_AN_TIENG_VIET,
        self.TEN_DU_AN_VIET_TAT = TEN_DU_AN_VIET_TAT
        self.NGAY_DANG_KY = NGAY_DANG_KY
        self.NOI_DUNG = NOI_DUNG
        self.HINH_THUC_RD = HINH_THUC_RD,


class DoanhNghiepHoatDong:
    def __init__(self, SO_CNDKKD, TEN_DN, TEN_DU_AN_TIENG_VIET, TEN_DU_AN_VIET_TAT, MUC_TIEU_HOAT_DONG, VON_DAU_TU_VND):
        if SO_CNDKKD is None:
            self.SO_CNDKKD = "",
        else:
            self.SO_CNDKKD = SO_CNDKKD,

        if TEN_DN is None:
            self.TEN_DN = "",
        else:
            self.TEN_DN = TEN_DN,

        if TEN_DU_AN_TIENG_VIET is None:
            self.TEN_DU_AN_TIENG_VIET = ""
        else:
            self.TEN_DU_AN_TIENG_VIET = TEN_DU_AN_TIENG_VIET

        if MUC_TIEU_HOAT_DONG is None:
            self.MUC_TIEU_HOAT_DONG = ""
        else:
            self.MUC_TIEU_HOAT_DONG = MUC_TIEU_HOAT_DONG

        if math.isnan(VON_DAU_TU_VND):
            self.VON_DAU_TU_VND = 0,
        else:
            self.VON_DAU_TU_VND = VON_DAU_TU_VND,

    def __str__(self):
        return self.SO_CNDKKD


####################----------thong Ke xuat nhap khau

def thongKeXuatKhau(request):
    return render(request, "thong_ke_xuat_khau.html",
                  {"thongke": vThongKeXuatKhau(),
                   "phantich": DuDoanXuatKhau()}
                  )


def thongKeNhapKhau(request):
    return render(request, "thong_ke_nhap_khau.html", {
        "thongke": vThongKeNhapKhau(),
        "phantich": DuDoanNhapKhau(),
    })


# dau tu ngoai
def thongKeVonFDI(request):
    return render(request, "phan_tich_FDI.html", {
        "thongke": vThongKeFDI(),
        "phantich": DuDoanFDI(),
    })


# dau tu noi
def thongKeVonVND(requesst):
    return render(requesst, "phan_tich_VN.html", {
        "thongke": vthongKeDauTuNoi(),
        "phantich": DuDoanDauTuNoi(),
    })


def thongKeLaoDong(request):
    return render(request, "thong_ke_nguon_lao_dong_chat_luong_cao.html",
                  {"thongke": vThongKeLaoDongChatLuongCao(),
                   "phantich": DuDoanNguoiLaoDong()
                   }
                  )


def linh_vuc_dau_tu_CNC_SL(request):
    return render(request, "thongKeLinhVucCNC_SL.html",
                  {"thongke_linh_vuc": thongKeLinhVucCNC_linhVuc_SL_(),
                   "thongke_linh_vuc_CNC": thongKeLinhVucCNC_linhvucCNC_SL()
                   }
                  )


def linh_vuc_dau_tu_CNC_VON(request):
    dataResult = thongKeLinhVucCNC_linhVuc_SL_()

    # for x in dataResult:
    #     x.MA_LVCNC = x.MA_LVCNC

    return render(request, "thongKeLinhVucCNC_VON.html",
                  {"thongke_linh_vuc": dataResult,
                   "thongke_linh_vuc_CNC": thongKeLinhVucCNC_linhvucCNC_SL()
                   }
                  )


def linh_vuc_dau_tu_CNC_SL_FDI(request):
    return render(request, "thongKeLinhVucCNC_SL_FDI.html",
                  {"thongke_linh_vuc": thongKeLinhVucCNC_linhVuc_SL_(),
                   "thongke_linh_vuc_CNC": thongKeLinhVucCNC_linhvucCNC_SL()
                   }
                  )
