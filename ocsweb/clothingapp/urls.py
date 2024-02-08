from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('', views.allstorepro, name="AllStorePro"),
    path('<slug:c_slug>/', views.allstorepro, name="Pro_By_Cat"),
    path('<slug:c_slug>/<slug:pro_slug>/', views.prodetails, name="ProDetails"),
]