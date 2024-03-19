#test django
import requests

doses = 200
url = 'http://your-django-website.com/receive_data/'
data = {'data': str(doses)}

response = requests.post(url, data=data)