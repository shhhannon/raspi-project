from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, "welcome.html")

def receive_data_view(request):
    if request.method == 'POST':
        # Process the incoming data
        received_data = request.POST.get('data', None)
        # Process the data as needed
        print(received_data)
        reading = reading(airQuality =  received_data[co2Quality_data], dateTime = received_data[dateTime_data], numDoses = receieved_data[numDoses_data])
        readings = model.objects.get(reading)
                          
        return render(request, "data.html", context={'readings':readings})
