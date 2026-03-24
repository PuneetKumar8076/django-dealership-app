from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# 🔥 HOME / NORMAL DEALERS (Q17)
def get_dealers(request):
    dealers = [
        {"name": "BMW Delhi", "city": "Delhi"},
        {"name": "Audi Mumbai", "city": "Mumbai"},
        {"name": "Tesla Bangalore", "city": "Bangalore"},
    ]

    return render(request, 'dealers.html', {
        'dealers': dealers
    })


# 🔥 LOGIN REQUIRED DEALERS (Q18)
@login_required
def get_dealers_loggedin(request):
    dealers = [
        {"name": "BMW Delhi", "city": "Delhi"},
        {"name": "Audi Mumbai", "city": "Mumbai"},
        {"name": "Tesla Bangalore", "city": "Bangalore"},
    ]

    return render(request, 'dealers.html', {
        'dealers': dealers,
        'user': request.user
    })


# 🔥 FILTER BY STATE (Q18)
@login_required
def get_dealers_by_state(request, state):
    dealers = [
        {"name": "BMW Delhi", "city": "Delhi"},
        {"name": "Audi Mumbai", "city": "Mumbai"},
        {"name": "Tesla Bangalore", "city": "Bangalore"},
    ]

    filtered = [d for d in dealers if d["city"].lower() == state.lower()]

    return render(request, 'dealers.html', {
        'dealers': filtered,
        'user': request.user
    })


# 🔥 NEW (Q19) → DEALER DETAILS + REVIEWS
@login_required
def dealer_details(request, dealer_id):
    dealers = [
        {"id": 1, "name": "BMW Delhi", "city": "Delhi"},
        {"id": 2, "name": "Audi Mumbai", "city": "Mumbai"},
        {"id": 3, "name": "Tesla Bangalore", "city": "Bangalore"},
    ]

    dealer = next((d for d in dealers if d["id"] == dealer_id), None)

    reviews = [
        {"review": "Excellent service"},
        {"review": "Very good experience"},
    ]

    return render(request, 'dealer_details.html', {
        'dealer': dealer,
        'reviews': reviews,
        'user': request.user
    })


# 🔥 ABOUT PAGE
def about(request):
    return render(request, 'About.html')


# 🔥 CONTACT PAGE
def contact(request):
    return render(request, 'Contact.html')
