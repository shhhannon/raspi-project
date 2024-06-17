from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from InhalerAid.models import readings
from datetime import datetime

@csrf_exempt #exempts the view from CSRF verification
def save_reading(request):
    if request.method == 'POST':
        co2 = float(request.POST.get('CO2'))
        date_time = datetime.fromisoformat(request.POST.get('dateTime'))
        doses = readings.objects.last().doses - 2 if readings.objects.exists() else 200 #decrement doses by 2 every time asthma pump is used
        readings.objects.create(
            date=date_time.date(),
            time=date_time.time(),
            co2=co2,
            doses=doses
        ) #creates row of new data from the asthma attack
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure', 'reason': 'Invalid method'}, status=405) #gives status of successful updates to database

def readings_table(request):
    all_readings = readings.objects.all()
    return render(request, 'data.html', {'readings': all_readings}) #adds new row of data to database


