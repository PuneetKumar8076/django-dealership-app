from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Dealer


def home(request):
    return render(request, 'Home.html')


def about(request):
    return render(request, 'About.html')


def contact(request):
    return render(request, 'Contact.html')


#  Q17 FINAL FUNCTION
@login_required
def get_dealers_loggedin(request):
    dealers = Dealer.objects.all()

    return render(request, 'dealers.html', {
        'dealers': dealers,
        'user': request.user
    })
