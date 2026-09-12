from django.shortcuts import render, redirect
from .models import Subscription, Contributor
from django.contrib.auth import get_user_model
User = get_user_model()

def subscribe_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        sub = Subscription.objects.create(email=email, amount=2000, paid=False)
        # For now mark as pending - later add Paystack
        return render(request, 'village/subscribe_success.html', {'sub': sub})
    
    total_paid = sum([s.amount for s in Subscription.objects.filter(paid=True)])
    leaders = Contributor.objects.order_by('-points')[:5]
    return render(request, 'village/subscribe.html', {
        'total': total_paid,
        'leaders': leaders,
        'sub_count': Subscription.objects.filter(paid=True).count()
    })

def leaderboard(request):
    contributors = Contributor.objects.order_by('-points')
    return render(request, 'village/leaderboard.html', {'contributors': contributors})