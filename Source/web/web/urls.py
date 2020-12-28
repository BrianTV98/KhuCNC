"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("report", views.report, name="report"),
    path("thongke", views.thongke, name="thongke"),
    path("phantich", views.phantich, name="phantich"),
    path("testData", views.testData, name="testData"),

    path("phantichvonVND", views.vonVND, name="phantichvonVND"),
    path("phantichvonSX", views.vonSX, name="phantichvonSX"),
    path("phantichvonKhac", views.vonKhac, name="phantichvonKhac"),
    path("phantichvonPTHT", views.vonPTHT, name="phantichvonPTHT"),
    path("phantichvonDV", views.vonDV, name="phantichvonDV"),
    path("phantichvonDT_UT", views.vonDT_UT, name="phantichvonDT_UT"),
    path("thongke_kinh_phi", views.thongKe_kinh_phi, name="thongke_kinh_phi"),
    path("thongke_ti_le_ld_clc_tham_gia_rd", views.thongke_tile_ld_clc_tham_gia_rd, name="thongke_ti_le_ld_clc_tham_gia_rd"),

    path("thong_ke_du_an_dau_tu", views.thong_ke_du_an_dau_tu,name="thong_ke_du_an_dau_tu"),
    path("thong_ke_doanh_nghiep_hoat_dong", views.thong_ke_doanh_nghiep_hoat_dong,name="thong_ke_doanh_nghiep_hoat_dong"),
    path("thong_ke_hoat_dong_rd", views.thong_ke_hoat_dong_rd,name="thong_ke_hoat_dong_rd"),

    path("thong_ke_xuat_khau", views.thongKeXuatKhau,name="thong_ke_xuat_khau"),

    path("thong_ke_nhap_khau", views.thongKeNhapKhau,name="thong_ke_nhap_khau"),
    path("phan_tich_FDI", views.thongKeVonFDI, name="phan_tich_FDI"),
    path("phan_tich_VN", views.thongKeVonVND, name="phan_tich_VN"),
    path("phan_tich_lao_dong", views.thongKeLaoDong, name="phan_tich_lao_dong"),
    path("linh_vuc_dau_tu_CNC_SL", views.linh_vuc_dau_tu_CNC_SL, name ="linh_vuc_dau_tu_CNC_SL"), # cho nay chinh la la USD thay vi VND
    path("linh_vuc_dau_tu_CNC_VON", views.linh_vuc_dau_tu_CNC_VON, name ="linh_vuc_dau_tu_CNC_VON"),
    path("linh_vuc_dau_tu_CNC_SL_FDI", views.linh_vuc_dau_tu_CNC_SL_FDI, name="linh_vuc_dau_tu_CNC_SL_FDI"),
    path("thongKeVonDauTuChung", views.thongKeVonDauTuChung, name="thongKeVonDauTuChung"),
    path("thongKeVonDauTuChung2", views.thongKeVonDauTuChung2, name="thongKeVonDauTuChung2")

]




# urlpatterns = patterns('',
#                        url(r'^$', 'testapp.views.index'),
#                        url(r'^user/create/$', 'testapp.views.create_user'),
#                        url(r'^admin', include(admin.site.urls)),
#                        )
