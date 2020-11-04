import pyodbc as pyodbc
from django.shortcuts import render
import pandas as pd

from web.contrains.base_url import base_url_model
from web.model.ThongKeChung import ThongKeChung
from web.model.ThongKeDauTu import ThongKeDauTu
from web.view.phantich import du_doan_tinh_hinh
from web.view.thongke import thongketylechiRD
import pickle

import pandas as pd
import pyodbc
from fbprophet import Prophet

import pystan

import matplotlib.pyplot as plt
import base64
import io
import urllib
import json

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

    # Cai nay dung roi
    val1 = request.GET.get("a")
    val2 = request.GET.get("b")

    if val1 is None:
        val1 = "2010"
    if val2 is None:
        val2 = "2020"

    try:
        sp = 'EXEC [dbo].[SP_DASHBOARD_THONGKE_VON_DAU_TU]' + " '" + val1 + "','" + val2 + "'"
        thongkeDauTu = pd.read_sql_query(sp, conn)
        thongkegDauTuResult = [
            (ThongKeDauTu(row.TONGVONDAUTU_FDI, row.TONGVONDAUTU_VN, row.SOLUONG_FDI, row.SOLUONG_VN)) for
            index, row in thongkeDauTu.iterrows()]
        thongkeDauTuresponse = [vars(ob) for ob in thongkegDauTuResult]

        test = thongketylechiRD
        print(test)
        return render(request, 'thongke.html', {"thongkechung": response[0],
                                                "thongkeDauTu": thongkeDauTuresponse,
                                                "tylechiRd": test})
    except Exception as e:
        print(e)
        pass
    # Khi mà viết một trang muốn sử dụng nhiều request thì nên dùng class-based view
    # Trong đố sẽ như sau
    return render(request, 'thongke.html')


def phantich(request):
    # dataVonDauTuVND = pd.read_sql_query('SELECT NGAY_DANG_KY, VON_DAU_TU_VND FROM dbo.GIAY_CNDT',
    #                                     conn)  # get data from db
    # dataVonDauTuVND = dataVonDauTuVND.rename(columns={'NGAY_DANG_KY': 'ds', 'VON_DAU_TU_VND': 'y'})  # rename
    # dataVonDauTuVND.head()
    # print(dataVonDauTuVND)
    #
    # model_code = 'parameters {real y;} model {y ~ normal(0,1);}'
    # model = pystan.StanModel(model_code=model_code)  # this will take a minute
    # y = model.sampling(n_jobs=1).extract()['y']
    # y.mean()  # should be close to 0
    # m = Prophet(daily_seasonality=True)
    # m.fit(dataVonDauTuVND)
    # future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    # future.tail()
    # forecast = m.predict(future)
    # forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    m = pickle.load(open(base_url_model + '/VonDauTuVND.pickle', 'rb'))
    future = m.make_future_dataframe(periods=12, freq='M')  # so ngay can du bao
    future.tail()
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    fig1 = m.plot(forecast, xlabel='Năm', ylabel='Vốn đầu tư')
    ax = fig1.gca()
    ax.set_title("Biểu đồ thể nguồn vốn đầu tư và dự đoán đầu tư", size=28)
    # fig1.show()

    buf = io.BytesIO()
    fig1.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)

    buf2 = io.BytesIO()
    fig2 = m.plot_components(forecast)
    fig2.savefig(buf2, format='png')
    buf2.seek(0)
    string2 = base64.b64encode(buf2.read())
    uri2 = 'data:image/png;base64,' + urllib.parse.quote(string2)
    # fig = plt.gcf()
    # buf = io.BytesIO()
    # fig.savefig(buf, format='png')
    # buf.seek(0)
    # string = base64.b64encode(buf.read())
    #
    # uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    #
    args = {'image': uri, 'image2': uri2}
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
