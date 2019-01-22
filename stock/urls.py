from django.urls import path

from . import views

app_name = 'stock'
urlpatterns = [
    path('', views.checkData, name='checkData'),
    path('home', views.stock_welcome, name='stock_welcome'),
    path('<str:ticker>/', views.stock_detail, name='stock_detail'),
    path('top_20', views.StockTodayArchiveView.as_view(), name='top_20'),
    path('<str:ticker>/news/',views.individual_stock_news, name='individual_stock_news'),
]
