from django.shortcuts import render

def appointments(request): 
  return render(request, 'appointments/appointments.html')