from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('chart',views.chart, name="chart"),
    path('User_count',views.get_data, name="UserCount"),
    path('get_data/cat',views.get_cat_data, name="getdatacat"),
    path('update_item/',views.updateItem, name=""),
    path('update_fav/',views.updateFav, name=""),
    path('detail/<int:product_id>/',views.details),
    path('cart',views.carts),
    path('checkout',views.checkout),
    path('contactus',views.contactus),
    path('favorite',views.favorite),
    path('profile',views.profile),
    path('about',views.about),
    path('status/<int:orderid>/',views.status),
    path('payment',views.payment),
    path('complate',views.complate,name="sucess"),
    path('order/success/<int:id>/<str:trasection_id>',views.order_sucess,name="sucess"),
]
