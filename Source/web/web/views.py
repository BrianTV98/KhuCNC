import pyodbc as pyodbc
from django.shortcuts import render
import pandas as pd

from web.contrains.base_url import base_url_model, conn
from web.model.ThongKeChung import ThongKeChung
from web.model.ThongKeDauTu import ThongKeDauTu
from web.view.indext import getYearFromTo, getThongDauTu
from web.view.phantich import DuDoanDauTuVND, DuDoanDauTuUSD, DuDoanDauTu_SX, DuDoanDauTu_DT_UT, DuDoanDauTu_DV, \
    DuDoanDauTu_PTHT, DuDoanDauTu_DT, thongKeVonDauTuVND
from web.view.thongke import thongketylechiRD, thongKeTyLeLoaiHinhDauTu
import pickle
from django.http import HttpResponseRedirect
import pandas as pd

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

    print(val3)
    print(val4)

    return render(request, 'indext.html', {"thongkechung": response[0],
                                           "thongkeDauTu": getThongDauTu(val3, val4)[0],
                                           "year_from_to": from_to})


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
        'image_dau_tu_VND': DuDoanDauTuVND(),
        'thong_ke_dau_tu_VND': thongKeVonDauTuVND(),
        'image_dau_tu_USD': DuDoanDauTuUSD(),
        'image_dau_tu_SX': DuDoanDauTu_SX(),
        'image_dau_tu_DT_UT': DuDoanDauTu_DT_UT(),
        'image_dau_tu_DV': DuDoanDauTu_DV(),
        'image_dau_tu_PTHT': DuDoanDauTu_PTHT(),

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
