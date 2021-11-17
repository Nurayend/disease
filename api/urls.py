from django.urls import path
from . import views
from .views import DiseaseCreate, DiseaseUpdate, DiseaseDelete

urlpatterns = [
    path('', views.DiseaseTableView, name="home"),
    path('create/', DiseaseCreate.as_view(), name="create"),
    path('update/<int:pk>', DiseaseUpdate.as_view(), name='dis_update'),
    path('delete/<int:pk>', DiseaseDelete.as_view(), name='dis_delete'),
]
