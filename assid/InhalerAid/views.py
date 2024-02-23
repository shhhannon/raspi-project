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
        return render(request, "data.html")
