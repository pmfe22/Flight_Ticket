from django.shortcuts import render, redirect  
from .models import Flight  
from .forms import FlightForm  

def flight_list(request):  
    flights = Flight.objects.all()  
    return render(request, 'flight_list.html', {'flights': flights})  

def flight_create(request):  
    if request.method == 'POST':  
        form = FlightForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('flight_list')  
    else:  
        form = FlightForm()  
    return render(request, 'flight_form.html', {'form': form})