from django.shortcuts import render
from .models import readings

def welcome(request):
    #Get readings from database
    all_data = readings.objects.all()
    
    #Pass this data to the template
    context = {
        'readings':all_data
    }

    return render(request, "welcome.html", context)

