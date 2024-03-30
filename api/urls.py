from django.urls import path
from api import views
urlpatterns = [
    path("",views.home,name="home"),
    path("create/",views.AddresSerializerCView.as_view(),name="Create"),
    path("read/",views.AddresSerializerRView.as_view(),name="Read"),
    path("readt/<str:pk>/",views.AddresSerializerRtView.as_view(),name="Read"),
    path("update/<str:pk>/",views.AddresSerializerUView.as_view(),name="Update"),
    path("delete/<str:pk>/",views.AddresSerializerDView.as_view(),name="Delete"),
]
