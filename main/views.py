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

def profile_view(request):
    return render(request, 'profile_tab.html')