from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Django Dealership App")

def contact(request):
    return HttpResponse("Contact us at support@dealership.com")
