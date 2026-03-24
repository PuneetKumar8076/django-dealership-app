from django.shortcuts import render

def home(request):
    return render(request, 'Home.html')

def about(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'Contact.html')


# ✅ Q16 / Q17 MAIN FUNCTION
def get_dealers(request):
    dealers = [
        {"name": "BMW Delhi", "city": "Delhi"},
        {"name": "Audi Mumbai", "city": "Mumbai"},
        {"name": "Tesla Bangalore", "city": "Bangalore"},
    ]

    return render(request, 'Home.html', {'dealers': dealers})
