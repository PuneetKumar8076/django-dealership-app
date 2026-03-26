from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse


# 🔥 GLOBAL REVIEW STORAGE (OLD + NEW COMBINED)
reviews_data = {
    1: [{"review": "Excellent service"}, {"review": "Very good experience"}],
    2: [{"review": "Nice dealer"}],
    3: [{"review": "Mind blowing experience"}]
}


# 🔥 Q17 - NORMAL DEALERS
def get_dealers(request):
    dealers = [
        {"id": 1, "name": "BMW Delhi", "city": "Delhi"},
        {"id": 2, "name": "Audi Mumbai", "city": "Mumbai"},
        {"id": 3, "name": "Tesla Bangalore", "city": "Bangalore"},
    ]

    return render(request, 'dealers.html', {
        'dealers': dealers
    })


# 🔥 Q18 - LOGIN REQUIRED DEALERS
@login_required
def get_dealers_loggedin(request):
    dealers = [
        {"id": 1, "name": "BMW Delhi", "city": "Delhi"},
        {"id": 2, "name": "Audi Mumbai", "city": "Mumbai"},
        {"id": 3, "name": "Tesla Bangalore", "city": "Bangalore"},
    ]

    return render(request, 'dealers.html', {
        'dealers': dealers,
        'user': request.user
    })


# 🔥 Q18 - FILTER BY STATE
@login_required
def get_dealers_by_state(request, state):
    dealers = [
        {"id": 1, "name": "BMW Delhi", "city": "Delhi"},
        {"id": 2, "name": "Audi Mumbai", "city": "Mumbai"},
        {"id": 3, "name": "Tesla Bangalore", "city": "Bangalore"},
    ]

    filtered = [d for d in dealers if d["city"].lower() == state.lower()]

    return render(request, 'dealers.html', {
        'dealers': filtered,
        'user': request.user
    })


# 🔥 Q19 - DEALER DETAILS + REVIEWS (UPDATED)
@login_required
def dealer_details(request, dealer_id):
    dealers = [
        {"id": 1, "name": "BMW Delhi", "city": "Delhi"},
        {"id": 2, "name": "Audi Mumbai", "city": "Mumbai"},
        {"id": 3, "name": "Tesla Bangalore", "city": "Bangalore"},
    ]

    dealer = next((d for d in dealers if d["id"] == dealer_id), None)

    # 🔥 OLD + NEW reviews combined
    reviews = reviews_data.get(dealer_id, [])

    return render(request, 'dealer_details.html', {
        'dealer': dealer,
        'reviews': reviews,
        'user': request.user
    })


# 🔥 Q20 - ADD REVIEW PAGE (FIXED)
@login_required
def add_review(request, dealer_id):
    if request.method == "POST":
        review = request.POST.get("review")

        # 🔥 SAVE REVIEW
        if dealer_id not in reviews_data:
            reviews_data[dealer_id] = []

        reviews_data[dealer_id].append(review)

        return redirect(f"/dealer/{dealer_id}/")

    return render(request, 'add_review.html', {
        'dealer_id': dealer_id
    })


# 🔥 EXTRA PAGES (UNCHANGED)
def about(request):
    return render(request, 'About.html')


def contact(request):
    return render(request, 'Contact.html')


# 🔥 CREATE USER (UNCHANGED)
def create_user(request):
    if not User.objects.filter(username='puneet').exists():
        User.objects.create_superuser('puneet', 'test@gmail.com', '0002')
        return HttpResponse("User created successfully")

    return HttpResponse("User already exists")