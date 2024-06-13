from django.shortcuts import render

def user_registeration_view(request):
    return render(request, 'registration.html')

def registeration_otp_view(request):
    return render(request, 'registeration_otp_entry.html')

def user_login_view(request):
    return render(request, 'login.html')

def user_home_view(request):
    return render(request, 'home.html')

def trip_search(request):
    return render(request, 'trip_search.html')

def trip_results_view(request):
    return render(request, 'trip_results.html')

def bus_details_view(request):
    return render(request, 'bus_details.html')

def enter_passenger_details_view(request):
    return render(request, 'enter_passenger_details.html')

def confirm_passenger_details_view(request):
    return render(request, 'details_confirmation_page.html')

def tickets_view(request):
    return render(request, 'tickets.html')

def profile_main_view(request):
    return render(request, 'profile.html')

def profile_view(request):
    return render(request, 'profile_tab.html')

def about_info_view(request):
    return render(request, 'about_and_info.html')

def help_support_view(request):
    return render(request, 'help-support.html')

def settings_view(request):
    return render(request, 'settings.html')

def password_reset_view(request):
    return render(request, 'password_reset.html')
  
def password_reset_otp(request):
    return render(request, 'password_reset_otp.html')

def password_reset_confirmation(request):
    return render(request, 'password_reset_confirmation.html')

def ticket_success(request):
    return render(request, 'ticket_success.html')
    