from django.urls import path

from KCNC import views

urlpatterns = [
    path("", views.index, name="index"),
    path("report", views.report, name="report")

]
