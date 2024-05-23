from django.urls import path
from . import views

urlpatterns = [

    path('registeration/', views.user_registeration_view, name="user-registeration"),
    path('enter_otp/', views.registeration_otp_view, name="registeration-otp"),
    path('login/', views.user_login_view, name="login"),
    path('', views.user_home_view, name="home"),
    path('trip-search/', views.trip_search, name="trip-search"),
    path('trip-results/', views.trip_results_view, name="trip-results"),
    path('bus-details/', views.bus_details_view, name="bus-details"),
    path('enter-passenger-details/', views.enter_passenger_details_view, name="enter-passenger-details"),
    path('confirm-details/', views.confirm_passenger_details_view, name='confirm-details'),
    path('bus_details.html/', views.bus_details_view, name='bus_details'),
    path('tickets.html', views.tickets_view, name='tickets'),
    path('profile/', views.profile_main_view, name='profile-main'),
    path('account-info/', views.profile_view, name='account-info'),
    path('password-reset/', views.password_reset_view, name="password-reset"),
    path('password-reset-otp/', views.password_reset_otp, name="password-reset-otp"),
    path('password-reset-confirmation/', views.password_reset_confirmation, name="password-reset-confirm"),
    path('about-info/', views.about_info_view, name='about-info'),
    path('help-&-support/', views.help_support_view, name='help-&-support'),
    path('settings/', views.settings_view, name='settings')
]
