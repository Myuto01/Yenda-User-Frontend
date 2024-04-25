from django.urls import path
from . import views

urlpatterns = [

    path('registeration/', views.user_registeration_view, name="user-registeration"),
    path('enter_otp/', views.registeration_otp_view, name="registeration-otp"),
    path('login/', views.user_login_view, name="login"),
    path('home/', views.user_home_view, name="home"),
    path('trip-search/', views.trip_search, name="trip-search"),
    path('trip-results/', views.trip_results_view, name="trip-results"),
    path('bus-details/', views.bus_details_view, name="bus-details"),
    path('enter-passenger-details/', views.enter_passenger_details_view, name="enter-passenger-details"),
    path('confirm-details', views.confirm_passenger_details_view, name='confirm-details'),
    path('bus_details.html', views.bus_details_view, name='bus_details'),
    path('tickets.html', views.tickets_view, name='tickets')

]
