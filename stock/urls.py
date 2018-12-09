from django.urls import path

from . import views

app_name = 'stock'
urlpatterns = [
    path('', views.StockTodayArchiveView.as_view(), name='top_20'),
    path('<str:ticker>/', views.stock_detail, name='stock_detail'),

]
